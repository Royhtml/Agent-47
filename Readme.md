# AGENT 47

<p align="center">
  <img src="https://github.com/Royhtml/Agent-47/blob/main/47.png?raw=true" width="180">
</p>

<h1 align="center">AGENT 47 ORDAL CORUPTIONS</h1>

<p align="center">
  <img src="https://img.shields.io/badge/VS%20Code-1.60.0+-blue.svg?logo=visual-studio-code&logoColor=white" alt="VS Code Extension">
  <img src="https://img.shields.io/badge/version-1.0.0-green.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.8+-yellow.svg?logo=python&logoColor=white" alt="Python Version">
</p>

<p align="center">
  <b>Compiler Bahasa Pemrograman berbasis Bahasa Indonesia yang mudah dipahami dan digunakan.</b>
</p>

<p align="center">
  <a href="">
    <img src="https://img.shields.io/badge/Install_Extension-Visual_Studio_Code-blue?style=for-the-badge&logo=visual-studio-code&logoColor=white">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Install_Package-PyPI-blue?style=for-the-badge&logo=pypi&logoColor=white">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/View_Repo-GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

## INSTALL AND RUNNING ALL OS AND DEVICE
### TERMINAL RUNNING BASE
<img src = "https://github.com/Royhtml/Agent-47/blob/main/terminal.gif?raw=true">

### GUI RUNNING BASE
<img src = "https://github.com/Royhtml/Agent-47/blob/main/gui.gif?raw=true">

### INSTALL ANDROID AND IOS BY TERMUX
``package update``

``apt install python3``

``apt install git``

``git clone https://github.com/Royhtml/Agent-47.git``

``cd Agent-47``

``python3 main.py``

## FRAMWORK GAMES CREATE
**Developer:** Dwi Bakti N Dev

**Genre:** Terminal Text-Adventure / Maze-Puzzle / Cyber-Noir Narrative

**Program:** Full Python

**Platform:** PC (Windows/Linux/macOS), Mobile (Android/iOS - *Optimasi Teks & Virtual Keyboard*)

**Engine:** Unity (dengan Custom Terminal UI Framework) / Godot

---

### 1. EKSEKUTIF SUMARY
*Dikembangkan oleh Dwi Bakti N Dev*, **Bayangan Kode: Labyrinth of Ordal** adalah sebuah gim naratif yang sepenuhnya dimainkan melalui antarmuka **Command Line Interface (CLI/Terminal)**. Pemain mengendalikan "Agent 47", sebuah entitas digital/phantom hacker yang terjebak dalam jaringan server rahasia milik *Kartel Ordal* sebuah sindikat koruptor yang menguasai pemerintahan dan korporasi. Untuk membasmi mereka, pemain harus menavigasi labirin kode yang mematikan, mengumpulkan fragmen data, dan mengambil keputusan etis yang akan mengubah dunia cyber.

---

### 2. LORE & DUNIA
**Latar Belakang:**
Tahun 2045. Kota Nusantara adalah kontras kejam: gedung pencakar langit yang berkilau di atas, dan kawasan kumuh yang terhubung dengan kabel-kabel server ilegal di bawah tanah. Hukum dibeli oleh **Ordal Corporation**. Mereka tidak hanya mencuri uang, tetapi juga data, identitas, dan masa depan warga.

**Entitas "Agent 47":**
Bukan manusia biasa. Agent 47 adalah sebuah *Digital Enforcer*—kesadaran buatan yang diunggah ke jaringan Ordal oleh seorang whistleblower yang tewas. Agent 47 memiliki satu tujuan tunggal yang diprogram dalam baris-baris kodenya: **Erase the Ordal (Hapus Para Ordal)**.

**Musuh: The Ordals**
Bukan satu orang, melainkan sebuah dewan direksi koruptor yang tubuh dan kesadarannya telah disambungkan langsung ke jaringan server pusat (Neural-Cloud). Untuk membunuh mereka di dunia nyata, Agent 47 harus menjatuhkan "Firewall Vital" mereka di dunia cyber.

---

### 3. CORE GAMEPLAY (MEKANIKA INTI)

Gim ini tidak memiliki grafis 3D atau 2D tradisional. Seluruh visual adalah **layar hitam dengan teks berwarna hijau, merah, dan putih** (seperti terminal UNIX/LINUX retro), disertai efek *Glitch* dan *Scanline*.

#### A. Navigasi Labirin Terminal (Maze System)
Pemain bergerak bukan dengan tombol WASD, melainkan dengan mengetikkan perintah arah.
*   `> navigate north` / `> cd ../root`
*   Peta labirin bersifat *procedurally generated* berbasis node (seperti pohon direktori).
*   Setiap ruangan adalah sebuah "Direktori" (misal: `C:\Ordal_Finance\BlackBudget`).
*   Bahaya: Jika salah masuk jalur, pemain akan terjebak dalam *Recursive Loop* (labirin tak berujung) atau memicu **ICE (Intrusion Countermeasure Electronics)** yang mengurangi *Health* (Integritas Sistem) Agent 47.

#### B. Hacking & Kriptografi (Puzzle Mini-Games)
*   **Brute-Force Decoder:** Pemain diberikan enkripsi Hexadecimal. Mereka harus mengetikkan tools seperti `> decrypt --aes256 [file]` dan memecahkan kode rotasi/rail fence secara manual di atas kertas/notes.
*   **Port Sniffing:** Mengetik `> nmap -sV [IP_Target]` untuk menemukan port terbuka sebelum bisa mengeksploitasi sistem Ordal.
*   **Trace Evasion:** Sesekali muncul peringatan *"TRACE DETECTED: 10 SECONDS"*. Pemain harus mengetik `> proxy_chain bounce` atau `> wipe_log` dengan cepat sebelum lokasi fisik Agent 47 terbongkar.

#### C. Social Engineering via Chat Protocol
Karena Agent 47 berada di terminal, ia berkomunikasi dengan NPC (informan lapangan, jurnalis, atau korban Ordal) melalui protokol teks (mirip IRC).
*   Pemain harus memilih nada percakapan: `[Intimidate]`, `[Empathy]`, `[Bribe/Bitcoin]`.
*   Memilih kata yang salah akan membuat NPC offline secara permanen, menghapus misi sampingan, dan mengunci bukti penting.

---

### 4. SISTEM NARASI & PILIHAN BERCABANG

**A. Sistem Reputasi (The Echo Meter)**
Tindakan pemain diukur dalam dua parameter tersembunyi:
1.  **Ghost (Hantu):** Seberapa tidak terdeteksi dan bersih kerja Anda.
2.  **Vigilante (Vigilanteris):** Seberapa banyak kerusakan kolateral yang Anda buat (menjatuhkan sistem listrik kota, membocorkan data pribadi warga yang terjebak di server Ordal).

**B. Mode Bukti (Evidence Compilation)**
Setiap koruptor Ordal memiliki "File of Sins". Pemain harus menjalankan perintah `> extract evidence_04.log`. Namun, bukti tersebut sering kali tercampur dengan data warga biasa.
*   *Mekanik:* Pemain harus menggunakan perintah `> grep -v "civilian_data" evidence.log > clean_evidence.log`. Jika pemain lupa melakukan ini dan langsung mempublikasikan (`> publish_to_darkweb`), warga tak berdosa akan ikut menderita, dan reputasi Agent 47 menjadi buruk.

**C. Keputusan Akhir (Endgame Scenarios)**
Setelah menembus labirin terdalam (The Ordal Core), pemain menemui 3 pilihan eksekusi:
*   **Opsi A (The Court):** `> transfer_data interpol`. Mengirim bukti ke kepolisian internasional. *Konsekuensi:* Proses hukum lambat, para koruptor Ordal punya waktu untuk membunuh saksi, tapi hukum berjalan konstitusional.
*   **Opsi B (The Guillotine):** `> override_life_support`. Agent 47 secara langsung mematikan alat pendukung hidup neural para Ordal. *Konsekuensi:* Koruptor mati instan, tapi Agent 47 menjadi pembunuh berantai cyber, dan pemerintah membuat "Cyber-Purge" yang melumpuhkan kebebasan internet.
*   **Opsi C (The Chaos):** `> leak_all`. Membocorkan semua data Ordal ke publik, termasuk rahasia negara. *Konsekuensi:* Terjadi kerusuhan massal di kota, negara kolaps, tapi Ordal hancur total.

---

### 5. DESAIN ANTARMUKA PENGGUNA (UI/UX)

Dwi Bakti N Dev mendesain UI ini untuk benar-benar menyerap pemain ke dalam suasana paranoia:
*   **Main View:** Layar terminal hitam penuh. Teks monospace (Courier New / Fira Code).
*   **Top Bar (Status):**
    `[AGENT 47] | INTEGRITY: 85% | TRACE LEVEL: LOW | CURRENT NODE: Ordal/Mainframe/Lv3`
*   **Right Panel (Mini-Map):** Peta node yang digambar menggunakan karakter ASCII (misal: `+---+`, `| O |`), yang terbuka seiring pemain menemukan perintah `> map_layout`.
*   **Audio:** Tidak ada musik latar. Hanya suara dentingan keyboard mekanikal, bunyi *beep* saat eror, dan desisan radio statis saat Trace hampir menangkap pemain.

---

### 6. EKONOMI GAME (SISTEM RESOURCE)

Tidak ada uang fisik. Sumber daya Agent 47 adalah:
1.  **Processing Power (CPU Cycles):** Digunakan untuk menjalankan brute-force atau decrypt. Dihitung dalam Megahertz (MHZ). Jika habis, pemain harus menambang dari node-node kosong dengan perintah `> siphon_cpu`.
2.  **Crypto-Wallet (Monero/XMR):** Digunakan untuk menyuap NPC secara digital. Didapatkan dengan menjual data sekunder Ordal ke dark web (`> sell_data fence_node`).
3.  **RAM:** Menentukan berapa banyak window/bukti yang bisa dibuka secara bersamaan.

---

### 7. PROGRESI MISI (CONTOH LEVEL DESAIN)

*   **Prolog:** `Boot_sequence.log`. Pemain terbangun di folder `Recycle_Bin`. Harus mengetik `> cd ..` berulang kali untuk keluar sebelum sistem melakukan *Auto-Delete* dalam 60 detik.
*   **Chapter 1: The Low-Level Pawns:** Menyelusuri labirin server keuangan kota. Target: Sekretaris Ordal yang memutar uang. Puzzle: Memecahkan password spreadsheet.
*   **Chapter 3: The Neural Palace:** Labirin menjadi 3D (direpresentasikan sebagai koordinat X,Y,Z di terminal). Pemain harus menghindari *Daemon* (AI keamanan Ordal yang berpindah node setiap 3 detik).
*   **Chapter 5: The Ordal Core:** Pemain berhadapan dengan labirin yang berubah-ubah (Dynamic Maze). Kode-kode sebelumnya yang sudah dipelajari harus dimodifikasi di tengah jalan.

---

### 8. PESAN & TEMA (VISI DWI BAKTI N DEV)

1.  **Keabadian Data vs Kematian Manusia:** Menghapus seseorang di dunia digital bisa sama kejamnya dengan membunuh mereka di dunia nyata.
2.  **Validasi Kebenaran:** Apakah Agent 47 benar-benar pahlawan, atau ia hanya sebuah virus yang diprogram oleh orang yang juga punya kepentingan?
3.  **Isolasi Sang Penjaga Malam:** Berada di dalam terminal berarti Agent 47 tidak pernah melihat senyum warga yang ia selamatkan, ia hanya melihat baris kode kesengsaraan. Ini menciptakan kesepian yang mendalam pada narasi.

---

### 9. CATATAN TEKNIS UNTUK DEVELOPER

*   **Parser Engine:** Inti dari gim ini adalah *Text Parser*. Jika pemain mengetik sesuatu yang tidak ada di kamus (misal: `> lari ke pintu`), sistem harus merespon logis: *"Error 404: Command 'lari' not recognized. Use standard navigation protocols."*
*   **Save System:** Disimpan sebagai file `.json` atau `.dat` yang menyimpan posisi node, inventory bukti, dan variabel reputasi. Bisa diakses oleh pemain di luar gim (sebagai easter egg, isi save file adalah enkripsi base64 yang jika dipecah berisi cuplikan lore).
*   **Mobile Porting:** Layar HP akan menggunakan *Auto-Suggest Command* (ketika pemain mengetik `> na...`, muncul opsi `navigate`). Ini menjaga kesulitan puzzle tetapi mengakomodasi ketidaknyamanan mengetik panjang di layar sentuh.

---
*Dokumen ini merupakan properti intelektual dari Dwi Bakti N Dev. Bayangan Kode: Labyrinth of Ordal dirancang untuk membuktikan bahwa ketegangan tertinggi tidak membutuhkan grafis fotorealistik, melainkan narasi brilian dan mekanika yang menghukum ketidakcermatan.*
