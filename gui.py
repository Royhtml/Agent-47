import sys
import os
import subprocess
import platform
import shutil
import psutil

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QPushButton, QProgressBar,
                               QTextEdit, QMenu, QDialog, QMessageBox,
                               QSystemTrayIcon, QTextBrowser)
from PySide6.QtCore import Qt, QThread, Signal, QPropertyAnimation, QEasingCurve, QSize, QTimer
from PySide6.QtGui import QFont, QAction, QIcon

import pyqtgraph as pg
pg.setConfigOption('background', '#0a0c10')
pg.setConfigOption('foreground', '#a0aec0')

ICON_PATH = "47.ico"
SCRIPT_NAME = "data.py"

AGENT47_STORY = """
<h2 style="color:#fc8181;">AGENT 47</h2>
<p style="color:#e2e8f0;">
In a city mired in corruption, a mysterious hacker known only by the codename <b>"47"</b>
operates silently from the shadows. He is neither a celebrated hero nor an ordinary
criminal he is a phantom hunting down corrupt officials, unscrupulous tycoons,
and syndicates hiding behind the veil of power.
</p>
<p style="color:#e2e8f0;">
Armed with a keyboard and lines of code, 47 infiltrates secure servers,
exposes illicit accounts, and leaks evidence of wrongdoing to the public. Every
mission carries immense risk: a single slip up could reveal his identity and
bring it all to an end.
</p>
<p style="color:#e2e8f0;">
<b>Agent47</b> is a story of justice pursued through unconventional means a
silent digital resistance against those who believe themselves to be above the law.
</p>
"""


def find_script_path():
    p = os.path.abspath(SCRIPT_NAME)
    return p if os.path.exists(p) else None


class WorkerThread(QThread):
    log_signal = Signal(str)
    progress_signal = Signal(int)
    finished_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self._is_running = True
        self._install_process = None

    def stop(self):
        self._is_running = False
        if self._install_process and self._install_process.poll() is None:
            try:
                self._install_process.terminate()
            except Exception:
                pass

    def run(self):
        try:
            if os.path.exists("requirements.txt"):
                self.log_signal.emit("[INFO] requirements.txt found. Checking dependencies...")
                self.progress_signal.emit(20)

                self._install_process = subprocess.Popen(
                    [sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"],
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
                )

                for line in self._install_process.stdout:
                    if not self._is_running:
                        self._install_process.terminate()
                        self.log_signal.emit("[STOPPED] Installation aborted by user.")
                        self.finished_signal.emit(False)
                        return
                    cleaned_line = line.strip()
                    if cleaned_line:
                        self.log_signal.emit(cleaned_line)
                self._install_process.wait()

                if not self._is_running:
                    self.log_signal.emit("[STOPPED] Installation aborted by user.")
                    self.finished_signal.emit(False)
                    return

                if self._install_process.returncode != 0:
                    self.log_signal.emit("[ERROR] Dependency installation failed.")
                    self.progress_signal.emit(100)
                    self.finished_signal.emit(False)
                    return

                self.log_signal.emit("[SUCCESS] Dependencies are ready.")
            else:
                self.log_signal.emit("[INFO] requirements.txt not found. Skipping installation.")

            self.progress_signal.emit(80)

            if not find_script_path():
                self.log_signal.emit(f"[ERROR] {SCRIPT_NAME} not found in the current directory.")
                self.progress_signal.emit(100)
                self.finished_signal.emit(False)
                return

            if not self._is_running:
                self.log_signal.emit("[STOPPED] Launch aborted by user.")
                self.finished_signal.emit(False)
                return

            self.progress_signal.emit(100)
            self.finished_signal.emit(True)

        except Exception as e:
            self.log_signal.emit(f"[CRITICAL] Internal error: {str(e)}")
            self.progress_signal.emit(100)
            self.finished_signal.emit(False)


class HealthDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Realtime Health Monitor")
        self.setMinimumSize(480, 380)
        self.setStyleSheet("""
            QDialog { background-color: #12151c; border: 1px solid #2d3748; }
            QLabel { color: #68d391; }
        """)

        layout = QVBoxLayout(self)

        self.info_label = QLabel("Gathering system data...")
        self.info_label.setFont(QFont("Consolas", 9))
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)

        self.health_chart = pg.PlotWidget()
        self.health_chart.setBackground('#0a0c10')
        self.health_chart.showGrid(x=True, y=True, alpha=0.3)
        self.health_chart.setFixedHeight(240)
        self.health_chart.addLegend(offset=(60, 10))

        self.cpu_curve = self.health_chart.plot(pen=pg.mkPen(color='#fc8181', width=2), name='CPU %')
        self.ram_curve = self.health_chart.plot(pen=pg.mkPen(color='#63b3ed', width=2), name='RAM %')
        self.health_chart.setYRange(0, 100)

        layout.addWidget(self.health_chart)

        close_btn = QPushButton("CLOSE")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #2d3748; color: #e2e8f0; border-radius: 6px;
                padding: 8px; font-weight: bold;
            }
            QPushButton:hover { background-color: #4a5568; }
        """)
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)


class ModernLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drag_position = None
        self.current_size = "small"
        self.thread = None
        self.agent_process = None
        self.health_dialog = None
        self.setMinimumSize(500, 420)
        self.resize(580, 460)

        self.max_points = 60
        self.cpu_data = [0] * self.max_points
        self.ram_data = [0] * self.max_points

        self.init_ui()
        self.init_tray()
        self.init_timers()

    def init_ui(self):
        self.setWindowTitle("Agent47 - Core Control")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QIcon(ICON_PATH))

        main_widget = QWidget(self)
        main_widget.setObjectName("MainWidget")

        main_widget.setStyleSheet("""
            QWidget#MainWidget {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #0f1117, stop:1 #171c28);
                border: 2px solid #000000;
                border-radius: 14px;
            }
            QLabel { color: #e2e8f0; }
            QProgressBar {
                border: 1px solid #2d3748; border-radius: 6px;
                background-color: #0a0c10; text-align: center;
                color: #ffffff; font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c53030, stop:1 #975a16);
                border-radius: 5px;
            }
            QTextEdit {
                background-color: #0a0c10; border: 1px solid #1a202c;
                border-radius: 8px; color: #a0aec0;
                font-family: 'Consolas', 'Courier New', monospace; font-size: 11px;
            }
            QPushButton#LaunchBtn {
                background-color: #c53030; color: white; border-radius: 8px;
                font-weight: bold; font-size: 12px;
            }
            QPushButton#LaunchBtn:hover { background-color: #e53e3e; }
            QPushButton#LaunchBtn:disabled { background-color: #4a5568; color: #718096; }
            QPushButton#StopBtn {
                background-color: #744210; color: white; border-radius: 8px;
                font-weight: bold; font-size: 12px;
            }
            QPushButton#StopBtn:hover { background-color: #975a16; }
            QPushButton#StopBtn:disabled { background-color: #4a5568; color: #718096; }
            QPushButton#ControlBtn {
                background-color: transparent; color: #718096;
                font-size: 16px; border-radius: 6px;
            }
            QPushButton#ControlBtn:hover {
                color: #e2e8f0; background-color: rgba(255, 255, 255, 0.05);
            }
            QPushButton#UtilBtn {
                background-color: #1a202c; color: #a0aec0; border-radius: 6px;
                font-weight: bold; font-size: 10px; padding: 6px;
                border: 1px solid #2d3748;
            }
            QPushButton#UtilBtn:hover { color: #e2e8f0; background-color: #2d3748; }
            QMenu {
                background-color: #1a202c; color: #e2e8f0;
                border: 1px solid #2d3748; border-radius: 8px; padding: 5px;
            }
            QMenu::item { padding: 7px 25px; border-radius: 4px; }
            QMenu::item:selected { background-color: #c53030; }
        """)

        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(20, 15, 20, 20)

        title_layout = QHBoxLayout()

        icon_lbl = QLabel()
        if os.path.exists(ICON_PATH):
            icon_lbl.setPixmap(QIcon(ICON_PATH).pixmap(24, 24))
        else:
            icon_lbl.setText("🔴")
        icon_lbl.setStyleSheet("background: transparent;")

        title_label = QLabel("AGENT 47 ORDAL")
        title_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        title_label.setStyleSheet("letter-spacing: 2px; color: #fc8181; background: transparent;")

        self.size_btn = QPushButton()
        self.size_btn.setObjectName("ControlBtn")
        self.size_btn.setFixedSize(30, 30)
        self.size_btn.setToolTip("Change Window Size")
        self.size_btn.setText("⧉")
        self.size_btn.clicked.connect(self.show_size_menu)

        min_btn = QPushButton("—")
        min_btn.setObjectName("ControlBtn")
        min_btn.setFixedSize(30, 30)
        min_btn.setToolTip("Minimize to Tray")
        min_btn.clicked.connect(self.hide_to_tray)

        close_btn = QPushButton("X")
        close_btn.setObjectName("ControlBtn")
        close_btn.setFixedSize(30, 30)
        close_btn.setToolTip("Close Application")
        close_btn.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        close_btn.clicked.connect(self.quit_app)

        title_layout.addWidget(icon_lbl)
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        title_layout.addWidget(self.size_btn)
        title_layout.addWidget(min_btn)
        title_layout.addWidget(close_btn)
        layout.addLayout(title_layout)

        util_layout = QHBoxLayout()
        self.health_btn = QPushButton("HEALTH MONITOR")
        self.health_btn.setObjectName("UtilBtn")
        self.health_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.health_btn.clicked.connect(self.open_health_popup)

        self.story_btn = QPushButton("ABOUT AGENT47")
        self.story_btn.setObjectName("UtilBtn")
        self.story_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.story_btn.clicked.connect(self.open_story_popup)

        util_layout.addWidget(self.health_btn)
        util_layout.addWidget(self.story_btn)
        layout.addLayout(util_layout)

        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        layout.addWidget(self.log_view)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedHeight(10)
        layout.addWidget(self.progress_bar)

        btn_layout = QHBoxLayout()
        self.launch_btn = QPushButton("START PLAY GAME SYSTEM")
        self.launch_btn.setObjectName("LaunchBtn")
        self.launch_btn.setFixedHeight(40)
        self.launch_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.launch_btn.clicked.connect(self.start_process)

        self.stop_btn = QPushButton("STOP SYSTEM")
        self.stop_btn.setObjectName("StopBtn")
        self.stop_btn.setFixedHeight(40)
        self.stop_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.confirm_stop_process)

        btn_layout.addWidget(self.launch_btn)
        btn_layout.addWidget(self.stop_btn)
        layout.addLayout(btn_layout)

        self.setCentralWidget(main_widget)
        self.center_on_screen()

    def init_tray(self):
        if not QSystemTrayIcon.isSystemTrayAvailable():
            self.tray_icon = None
            return

        tray_icon_img = QIcon(ICON_PATH) if os.path.exists(ICON_PATH) else self.windowIcon()

        self.tray_icon = QSystemTrayIcon(tray_icon_img, self)
        self.tray_icon.setToolTip("Agent47 Launcher")

        tray_menu = QMenu()

        show_action = QAction("Show", self)
        show_action.triggered.connect(self.show_from_tray)
        tray_menu.addAction(show_action)

        hide_action = QAction("Hide", self)
        hide_action.triggered.connect(self.hide_to_tray)
        tray_menu.addAction(hide_action)

        tray_menu.addSeparator()

        about_action = QAction("About Agent47", self)
        about_action.triggered.connect(self.open_story_popup)
        tray_menu.addAction(about_action)

        tray_menu.addSeparator()

        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(self.quit_app)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_activated)
        self.tray_icon.show()

    def on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            if self.isVisible():
                self.hide_to_tray()
            else:
                self.show_from_tray()

    def hide_to_tray(self):
        self.hide()
        if getattr(self, "tray_icon", None):
            self.tray_icon.showMessage(
                "Agent47 Launcher",
                "The application is still running in the system tray.",
                QSystemTrayIcon.MessageIcon.Information,
                2000
            )

    def show_from_tray(self):
        self.showNormal()
        self.activateWindow()
        self.raise_()

    def quit_app(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread.wait(1000)
        if self.agent_process and self.agent_process.poll() is None:
            try:
                self.agent_process.terminate()
            except Exception:
                pass
        if getattr(self, "tray_icon", None):
            self.tray_icon.hide()
        QApplication.quit()

    def closeEvent(self, event):
        event.ignore()
        self.quit_app()

    def init_timers(self):
        self.tick_timer = QTimer(self)
        self.tick_timer.timeout.connect(self.on_tick)
        self.tick_timer.start(1500)

    def on_tick(self):
        self.check_agent_process()
        if self.health_dialog is not None and self.health_dialog.isVisible():
            self.update_health_data()

    def open_health_popup(self):
        if self.health_dialog is None:
            self.health_dialog = HealthDialog(self)
        self.health_dialog.show()
        self.health_dialog.raise_()
        self.health_dialog.activateWindow()
        self.update_health_data()

    def update_health_data(self):
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        temp = "N/A"

        try:
            battery = psutil.sensors_battery()
        except Exception:
            battery = None

        try:
            temps = psutil.sensors_temperatures()
            if temps:
                for entries in temps.values():
                    if entries:
                        temp = f"{entries[0].current}°C"
                        break
        except Exception:
            pass

        batt_text = f"{battery.percent}%" if battery else "N/A"
        status = "Charging" if battery and battery.power_plugged else ("Discharging" if battery else "N/A")

        self.cpu_data.append(cpu)
        self.ram_data.append(ram)
        if len(self.cpu_data) > self.max_points:
            self.cpu_data.pop(0)
            self.ram_data.pop(0)

        self.health_dialog.info_label.setText(
            f"CPU: {cpu}% | RAM: {ram}% | Temp: {temp} | Battery: {batt_text} ({status})"
        )
        self.health_dialog.cpu_curve.setData(self.cpu_data)
        self.health_dialog.ram_curve.setData(self.ram_data)

    def open_story_popup(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("About Agent47")
        dialog.setMinimumSize(440, 380)
        dialog.setStyleSheet("QDialog { background-color: #12151c; border: 1px solid #2d3748; }")

        layout = QVBoxLayout(dialog)
        text_browser = QTextBrowser()
        text_browser.setStyleSheet("background-color: #0a0c10; border: none;")
        text_browser.setHtml(AGENT47_STORY)
        layout.addWidget(text_browser)

        close_btn = QPushButton("CLOSE")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #2d3748; color: #e2e8f0; border-radius: 6px;
                padding: 8px; font-weight: bold;
            }
            QPushButton:hover { background-color: #4a5568; }
        """)
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)

        dialog.exec()

    def show_size_menu(self):
        menu = QMenu(self)
        menu.addAction(QAction("Small (Laptop)", self, triggered=lambda: self.change_size("small")))
        menu.addAction(QAction("Medium (Monitor)", self, triggered=lambda: self.change_size("medium")))
        menu.addAction(QAction("Large (Maximized)", self, triggered=lambda: self.change_size("large")))
        button_pos = self.size_btn.mapToGlobal(self.size_btn.rect().bottomLeft())
        menu.exec(button_pos)

    def change_size(self, size_type):
        self.current_size = size_type
        self.anim = QPropertyAnimation(self, b"size")
        self.anim.setDuration(300)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        if size_type == "small":
            self.anim.setEndValue(QSize(580, 460))
        elif size_type == "medium":
            self.anim.setEndValue(QSize(750, 550))
        elif size_type == "large":
            screen = QApplication.primaryScreen().geometry()
            self.anim.setEndValue(QSize(int(screen.width() * 0.9), int(screen.height() * 0.9)))

        self.anim.start()
        self.anim.finished.connect(self.center_on_screen)

    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)

    def start_process(self):
        self.launch_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.launch_btn.setText("PREPARING...")

        self.thread = WorkerThread()
        self.thread.log_signal.connect(self.update_log)
        self.thread.progress_signal.connect(self.progress_bar.setValue)
        self.thread.finished_signal.connect(self.process_finished)
        self.thread.start()

    def process_finished(self, ready_to_launch):
        if not ready_to_launch:
            self.reset_to_start()
            return
        self.launch_agent_terminal()

    def launch_agent_terminal(self):
        current_os = platform.system()
        script_path = find_script_path()

        if not script_path:
            self.update_log(f"[ERROR] {SCRIPT_NAME} not found!")
            self.reset_to_start()
            return

        env = os.environ.copy()
        env.pop("SDL_VIDEODRIVER", None)

        try:
            if current_os == "Windows":
                self.agent_process = subprocess.Popen(
                    [sys.executable, script_path],
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                    env=env
                )
                self.update_log("[ACTION] Opened Agent47 in a new console window.")

            elif current_os == "Darwin":
                cmd = f'"{sys.executable}" "{script_path}"'
                self.agent_process = subprocess.Popen([
                    "osascript", "-e",
                    f'tell application "Terminal" to do script "{cmd}"'
                ], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.update_log("[ACTION] Opened Agent47 in a new Terminal window.")

            else:
                if not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
                    self.update_log("[WARNING] No display detected. Running Agent47 in the background.")
                    self.agent_process = subprocess.Popen([sys.executable, script_path], env=env)
                else:
                    terminals = [
                        ("gnome-terminal", ["gnome-terminal", "--", sys.executable, script_path]),
                        ("konsole", ["konsole", "-e", sys.executable, script_path]),
                        ("xfce4-terminal", ["xfce4-terminal", "-e", f"{sys.executable} {script_path}"]),
                        ("mate-terminal", ["mate-terminal", "-e", f"{sys.executable} {script_path}"]),
                        ("xterm", ["xterm", "-e", sys.executable, script_path]),
                        ("x-terminal-emulator", ["x-terminal-emulator", "-e", sys.executable, script_path]),
                    ]
                    launched = False
                    for name, cmd in terminals:
                        if shutil.which(name):
                            self.agent_process = subprocess.Popen(cmd, env=env)
                            self.update_log(f"[ACTION] Opened Agent47 using {name}.")
                            launched = True
                            break

                    if not launched:
                        self.update_log("[WARNING] No terminal emulator found. Running in background.")
                        self.agent_process = subprocess.Popen([sys.executable, script_path], env=env)

            self.update_log("[SUCCESS] Agent47 launched successfully.")
            self.launch_btn.setText("SYSTEM RUNNING")
            self.launch_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)

        except Exception as e:
            self.update_log(f"[CRITICAL] Failed to launch Agent47: {str(e)}")
            self.reset_to_start()

    def check_agent_process(self):
        if self.agent_process is not None and self.agent_process.poll() is not None:
            self.update_log("[INFO] Agent47 terminal was closed.")
            self.agent_process = None
            self.reset_to_start()

    def confirm_stop_process(self):
        reply = QMessageBox.question(
            self,
            "Abort System",
            "Are you sure you want to abort Agent47?\nThis will stop the running process.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.stop_process()

    def stop_process(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread.wait(1000)

        if self.agent_process and self.agent_process.poll() is None:
            try:
                self.agent_process.terminate()
            except Exception:
                pass
        self.agent_process = None

        self.update_log("[WARNING] User initiated system stop.")
        self.reset_to_start()

    def reset_to_start(self):
        self.stop_btn.setEnabled(False)
        self.launch_btn.setEnabled(True)
        self.launch_btn.setText("START SYSTEM")
        self.progress_bar.setValue(0)

    def update_log(self, text):
        self.log_view.append(text)
        scrollbar = self.log_view.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = None
        event.accept()


if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = ModernLauncher()
    window.show()
    sys.exit(app.exec())