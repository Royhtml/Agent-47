
import os
import sys
import time
import random
import shutil
import subprocess

# ---------- Utility ----------
def term_width(default=60):
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, end="\n"):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)

def center(text):
    w = term_width()
    return text.center(w)

def loading_bar(label="LOADING", length=30, duration=2.5):
    steps = 40
    for i in range(steps + 1):
        filled = int(length * i / steps)
        bar = "█" * filled + "░" * (length - filled)
        percent = int(100 * i / steps)
        sys.stdout.write(f"\r{label} [{bar}] {percent:3d}%")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print()

def spinner(label="PROCESSING", duration=1.5):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{label}... {frames[i % len(frames)]}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{label}... done!{' ' * 10}\n")

def matrix_rain(duration=2.0, width=None):
    width = width or min(term_width(), 80)
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ$#%&@!*"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = "".join(random.choice(chars) for _ in range(width))
        print(line)
        time.sleep(0.03)

def fake_hacking_logs(duration=2.0):
    logs = [
        "Connecting to mainframe server...",
        "Bypassing firewall...",
        "Decrypting core modules...",
        "Reassembling binary data...",
        "Synchronizing security protocols...",
        "Activating graphics engine...",
        "Injecting game assets...",
        "Compiling shaders...",
        "Establishing secure tunnel...",
        "Compilation successful.",
    ]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        addr = "0x%08X" % random.randint(0, 0xFFFFFFFF)
        status = random.choice(["OK", "SYNC", "PASS", "READY"])
        print(f"[{addr}] {logs[i % len(logs)]:<38} ...{status}")
        i += 1
        time.sleep(0.15)

def scanning_bar(label="SCANNING SYSTEM", duration=1.5):
    width = 30
    end_time = time.time() + duration
    pos = 0
    direction = 1
    while time.time() < end_time:
        bar = ["-"] * width
        bar[pos] = "#"
        sys.stdout.write(f"\r{label} [{''.join(bar)}]")
        sys.stdout.flush()
        pos += direction
        if pos >= width - 1 or pos <= 0:
            direction *= -1
        time.sleep(0.03)
    print()

def ascii_logo():
    logo = r"""
   _____          __  __ ______   _        ___    _    _ _   _  _____ _    _ 
  / ____|   /\   |  \/  |  ____| | |      / _ \  | |  | | \ | |/ ____| |  | |
 | |  __   /  \  | \  / | |__    | |     | | | | | |  | |  \| | |    | |__| |
 | | |_ | / /\ \ | |\/| |  __|   | |     | | | | | |  | | . ` | |    |  __  |
 | |__| |/ ____ \| |  | | |____  | |____ | |_| | | |__| | |\  | |____| |  | |
  \_____/_/    \_\_|  |_|______| |______| \___/   \____/|_| \_|\_____|_|  |_|
    """
    print(logo)

def countdown(n=3):
    for i in range(n, 0, -1):
        print(center(f"[ {i} ]"))
        time.sleep(0.6)

def glitch_text(text, iterations=8):
    glitch_chars = "!@#$%^&*<>/\\|~"
    for _ in range(iterations):
        glitched = "".join(
            random.choice(glitch_chars) if random.random() < 0.3 else ch
            for ch in text
        )
        sys.stdout.write(f"\r{glitched}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\r{text}{' ' * 5}\n")

# ---------- Intro Sequence ----------
def play_intro():
    clear()
    typewriter(">> BOOTING SYSTEM CORE...", delay=0.02)
    time.sleep(0.3)

    spinner(label="INITIALIZING KERNEL", duration=1.2)
    print()

    matrix_rain(duration=1.8)
    clear()

    typewriter(">> RUNNING SECURITY SCAN...", delay=0.02)
    scanning_bar(duration=1.5)
    print()

    fake_hacking_logs(duration=2.2)
    print()

    loading_bar(label="LOADING GAME ASSETS", duration=2.5)
    print()

    clear()
    ascii_logo()
    time.sleep(0.5)

    glitch_text(center(">>> ACCESS GRANTED <<<"))
    time.sleep(0.3)

    typewriter(center("=" * 50), delay=0)
    typewriter(center("SYSTEM READY. LAUNCHING GAME..."), delay=0.03)
    typewriter(center("=" * 50), delay=0)
    print()

    countdown(3)
    clear()
def run_game():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "data.py")

    if not os.path.exists(data_path):
        print(f"ERROR: File '{data_path}' not found.")
        print("Make sure data.py is in the same folder as launcher.py")
        sys.exit(1)
    subprocess.run([sys.executable, data_path])

if __name__ == "__main__":
    play_intro()
    run_game()