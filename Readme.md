# AGENT 47

<p align="center">
  <img src="https://github.com/Royhtml/Agent-47/blob/main/47.png?raw=true" width="180">
</p>

<h1 align="center">AGENT 47 ORDAL CORRUPTIONS</h1>

<p align="center">
  <img src="https://img.shields.io/badge/VS%20Code-1.60.0+-blue.svg?logo=visual-studio-code&logoColor=white" alt="VS Code Extension">
  <img src="https://img.shields.io/badge/version-1.0.0-green.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.8+-yellow.svg?logo=python&logoColor=white" alt="Python Version">
</p>

<p align="center">
  <b>An easy-to-understand and user-friendly programming language compiler based on Indonesian.</b>
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

**Platform:** PC (Windows/Linux/macOS), Mobile (Android/iOS - *Text & Virtual Keyboard Optimization*)

**Engine:** Unity (with Custom Terminal UI Framework) / Godot

---

### 1. EXECUTIVE SUMMARY
Developed by Dwi Bakti N Dev, **Shadow Code: Labyrinth of Ordal** is a narrative game played entirely through a **Command Line Interface (CLI/Terminal)**. Players control "Agent 47", a digital entity/phantom hacker trapped inside the secret server network of the *Ordal Cartel*—a syndicate of corruptors controlling the government and corporations. To eradicate them, players must navigate a deadly code maze, collect data fragments, and make ethical decisions that will change the cyber world.

---

### 2. LORE & WORLD
**Background:**
The year is 2045. Nusantara City is a harsh contrast: gleaming skyscrapers above, and slums connected by illegal server cables below ground. Laws are bought by **Ordal Corporation**. They don't just steal money; they steal data, identities, and the future of the citizens.

**The "Agent 47" Entity:**
Not an ordinary human. Agent 47 is a *Digital Enforcer*—an artificial consciousness uploaded into the Ordal network by a deceased whistleblower. Agent 47 has a single ultimate goal programmed into its code lines: **Erase the Ordal**.

**The Enemy: The Ordals**
Not a single person, but a board of corrupt directors whose bodies and consciousness have been directly connected to the central server network (Neural-Cloud). To kill them in the real world, Agent 47 must take down their "Vital Firewalls" in the cyber world.

---

### 3. CORE GAMEPLAY (CORE MECHANICS)

The game does not have traditional 3D or 2D graphics. All visuals are a **black screen with green, red, and white text** (like a retro UNIX/LINUX terminal), complete with *Glitch* and *Scanline* effects.

#### A. Terminal Maze Navigation (Maze System)
Players do not move using WASD keys, but by typing directional commands.
*   `> navigate north` / `> cd ../root`
*   The maze map is *procedurally generated* based on nodes (like a directory tree).
*   Each room is a "Directory" (e.g., `C:\Ordal_Finance\BlackBudget`).
*   Hazards: If you enter the wrong path, the player gets trapped in a *Recursive Loop* (endless maze) or triggers **ICE (Intrusion Countermeasure Electronics)** which reduces Agent 47's *Health* (System Integrity).

#### B. Hacking & Cryptography (Puzzle Mini-Games)
*   **Brute-Force Decoder:** Players are given Hexadecimal encryption. They must type tools like `> decrypt --aes256 [file]` and manually solve rotation/rail fence codes on paper/notes.
*   **Port Sniffing:** Typing `> nmap -sV [IP_Target]` to find open ports before exploiting the Ordal system.
*   **Trace Evasion:** Occasionally, a warning appears: *"TRACE DETECTED: 10 SECONDS"*. Players must quickly type `> proxy_chain bounce` or `> wipe_log` before Agent 47's physical location is exposed.

#### C. Social Engineering via Chat Protocol
Because Agent 47 is in a terminal, it communicates with NPCs (field informants, journalists, or Ordal victims) via text protocol (similar to IRC).
*   Players must choose the tone of conversation: `[Intimidate]`, `[Empathy]`, `[Bribe/Bitcoin]`.
*   Choosing the wrong words will make the NPC go offline permanently, deleting side missions and locking crucial evidence.

---

### 4. NARRATIVE SYSTEM & BRANCHING CHOICES

**A. Reputation System (The Echo Meter)**
Player actions are measured in two hidden parameters:
1.  **Ghost:** How undetected and clean your work is.
2.  **Vigilante:** How much collateral damage you cause (shutting down the city's power grid, leaking data of civilians caught in the Ordal servers).

**B. Evidence Mode (Evidence Compilation)**
Each corrupt Ordal has a "File of Sins". Players must execute the command `> extract evidence_04.log`. However, this evidence is often mixed with ordinary citizen data.
*   *Mechanic:* Players must use the command `> grep -v "civilian_data" evidence.log > clean_evidence.log`. If players forget to do this and immediately publish (`> publish_to_darkweb`), innocent civilians will suffer, and Agent 47's reputation will be ruined.

**C. Final Decision (Endgame Scenarios)**
After breaching the deepest labyrinth (The Ordal Core), players are presented with 3 execution options:
*   **Option A (The Court):** `> transfer_data interpol`. Sends evidence to international police. *Consequence:* Legal process is slow, the Ordal corruptors have time to kill witnesses, but the law runs constitutionally.
*   **Option B (The Guillotine):** `> override_life_support`. Agent 47 directly shuts down the neural life support of the Ordals. *Consequence:* Corruptors die instantly, but Agent 47 becomes a cyber serial killer, and the government creates a "Cyber-Purge" that cripples internet freedom.
*   **Option C (The Chaos):** `> leak_all`. Leaks all Ordal data to the public, including state secrets. *Consequence:* Massive riots occur in the city, the state collapses, but the Ordal is completely destroyed.

---

### 5. USER INTERFACE DESIGN (UI/UX)

Dwi Bakti N Dev designed this UI to truly immerse the player in an atmosphere of paranoia:
*   **Main View:** Full black terminal screen. Monospace text (Courier New / Fira Code).
*   **Top Bar (Status):**
    `[AGENT 47] | INTEGRITY: 85% | TRACE LEVEL: LOW | CURRENT NODE: Ordal/Mainframe/Lv3`
*   **Right Panel (Mini-Map):** A node map drawn using ASCII characters (e.g., `+---+`, `| O |`), which opens as players find the `> map_layout` command.
*   **Audio:** No background music. Only the sound of mechanical keyboard typing, a *beep* sound on error, and radio static hissing when a Trace is about to catch the player.

---

### 6. GAME ECONOMY (RESOURCE SYSTEM)

There is no physical money. Agent 47's resources are:
1.  **Processing Power (CPU Cycles):** Used to run brute-force or decryption. Calculated in Megahertz (MHZ). If depleted, players must mine from empty nodes using the command `> siphon_cpu`.
2.  **Crypto-Wallet (Monero/XMR):** Used to digitally bribe NPCs. Obtained by selling secondary Ordal data to the dark web (`> sell_data fence_node`).
3.  **RAM:** Determines how many windows/evidence files can be opened simultaneously.

---

### 7. MISSION PROGRESSION (LEVEL DESIGN EXAMPLE)

*   **Prologue:** `Boot_sequence.log`. The player wakes up in the `Recycle_Bin` folder. Must type `> cd ..` repeatedly to escape before the system performs an *Auto-Delete* in 60 seconds.
*   **Chapter 1: The Low-Level Pawns:** Navigating the city's financial server maze. Target: The Ordal secretary laundering money. Puzzle: Cracking a spreadsheet password.
*   **Chapter 3: The Neural Palace:** The maze becomes 3D (represented as X,Y,Z coordinates in the terminal). Players must avoid *Daemons* (Ordal security AIs that change nodes every 3 seconds).
*   **Chapter 5: The Ordal Core:** Players face a constantly changing maze (Dynamic Maze). Previously learned codes must be modified on the fly.

---

### 8. MESSAGES & THEMES (VISION OF DWI BAKTI N DEV)

1.  **Immortality of Data vs. Human Death:** Erasing someone in the digital world can be just as cruel as killing them in the real world.
2.  **Validation of Truth:** Is Agent 47 truly a hero, or just a virus programmed by someone who also has vested interests?
3.  **Isolation of the Night Watchman:** Being inside a terminal means Agent 47 never sees the smile of the citizens he saves; he only sees lines of code depicting misery. This creates a profound loneliness in the narrative.

---

### 9. TECHNICAL NOTES FOR DEVELOPERS

*   **Parser Engine:** The core of this game is the *Text Parser*. If a player types something not in the dictionary (e.g., `> lari ke pintu`), the system must respond logically: *"Error 404: Command 'lari' not recognized. Use standard navigation protocols."*
*   **Save System:** Saved as a `.json` or `.dat` file that stores node position, evidence inventory, and reputation variables. It can be accessed by the player outside the game (as an easter egg, the contents of the save file are base64 encrypted, which if cracked, contains lore snippets).
*   **Mobile Porting:** Mobile screens will use an *Auto-Suggest Command* feature (when a player types `> na...`, options like `navigate` appear). This maintains the puzzle difficulty but accommodates the inconvenience of typing long texts on touch screens.

---
*This document is the intellectual property of Dwi Bakti N Dev. Shadow Code: Labyrinth of Ordal is designed to prove that the highest tension does not require photorealistic graphics, but rather a brilliant narrative and mechanics that punish inattentiveness.*
