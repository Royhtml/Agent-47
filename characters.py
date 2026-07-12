CHARACTERS = [
    {
        "id": "rex", "name": "REX", "symbol": "\u25ba", "color": 1, "matrix_color": 1, 
        "gender": "Male", "age": "35 Years", "desc": "Military Combat Specialist.", 
        "info": "Direct brute force approach to the enemy's core.", 
        "ascii": ["  _|_  ", " [o o] ", "  /V\\  ", " / | \\ ", "  |_|  "], 
        "ascii_death": ["  _|_  ", " [x x] ", "  /V\\  ", " / | \\ ", "  |_|  "], 
        "story": ["REX, former special forces commander.", "Your troops fell. Now you are alone.", "Use your combat instincts to hack.", "Show ORDAL the meaning of physical force!"], 
        "ending": ["MILITARY SERVICE ENDED.", "ORDAL CRUMBLES UNDER WEAPON IMPACTS.", "THE WORLD WILL REMEMBER YOUR DEEDS, COMMANDER."], 
        "hacker_cmds": ["brute_force.exe --target {ip}", "override_firewall --force", "send_troop_decoy {db}", "physical_access --bypass {ip}"]
    },
    {
        "id": "zero", "name": "ZERO", "symbol": "\u2666", "color": 4, "matrix_color": 4, 
        "gender": "Male", "age": "28 Years", "desc": "Expert Stealth Hacker.", 
        "info": "Infiltrates undetected, destroys the system from within.", 
        "ascii": ["  ___  ", " (o_o) ", "  >#<  ", " / | \\ ", "  '_'  "], 
        "ascii_death": ["  ___  ", " (-_-) ", "  >#<  ", " / | \\ ", "  '_'  "], 
        "story": ["ZERO, ghost of the cyber world.", "No one knows your true face.", "You enter the ORDAL system silently.", "One mistake, and you will be exposed."], 
        "ending": ["SECRET FILES EXPORTED.", "ORDAL NEVER REALIZED YOUR PRESENCE.", "YOU VANISH BACK INTO THE SHADOWS."], 
        "hacker_cmds": ["nmap -sS {ip} --stealth", "ssh root@{ip} -p 2222", "ghost_exploit.py {ip}", "cat /var/log/ordal/secret"]
    },
    {
        "id": "nova", "name": "NOVA", "symbol": "\u2726", "color": 5, "matrix_color": 5, 
        "gender": "Female", "age": "26 Years", "desc": "Medical & Tracking Expert.", 
        "info": "Uses medical codes to find vulnerabilities.", 
        "ascii": ["  _|_  ", " (o.o) ", "  \\_/  ", "  | |  ", " /   \\ "], 
        "ascii_death": ["  _|_  ", " (x.x) ", "  \\_/  ", "  | |  ", " /   \\ "], 
        "story": ["NOVA, a genius field doctor.", "You discovered an AI biological virus.", "Use your medical knowledge to hack.", "Cure the world from the ORDAL plague!"], 
        "ending": ["DIGITAL VACCINE INJECTED.", "ORDAL INFECTED BY YOUR MEDICAL CODE.", "THE WORLD BREATHES EASILY BECAUSE OF YOU, DOCTOR."], 
        "hacker_cmds": ["scan_virus --analyze {db}", "inject_cure --target {ip}", "decode_dna_sequence {db}", "quarantine_node {ip}"]
    },
    {
        "id": "kai", "name": "KAI", "symbol": "\u266b", "color": 3, "matrix_color": 3, 
        "gender": "Male", "age": "22 Years", "desc": "Mysterious Cyber Ninja.", 
        "info": "Uses sound frequencies to destroy systems.", 
        "ascii": ["  /|\\  ", "  o-o  ", "  |_|  ", " _/ \\_ ", "  / \\  "], 
        "ascii_death": ["  /|\\  ", "  x-x  ", "  |_|  ", " _/ \\_ ", "  / \\  "], 
        "story": ["KAI, a ninja who masters waves.", "ORDAL is deaf to normal weapons.", "But not to your sound resonance.", "Shatter their servers with high notes!"], 
        "ending": ["MAXIMUM RESONANCE ACHIEVED.", "ORDAL SERVERS SHATTERED BY SOUND WAVES.", "YOUR WILL PLAYS THE SONG OF FREEDOM."], 
        "hacker_cmds": ["freq_blast --hz=440 {ip}", "sonic_ping {db}", "audio_jack_exploit {ip}", "deploy_soundworm {db}"]
    },
    {
        "id": "volt", "name": "VOLT", "symbol": "\u26a1", "color": 11, "matrix_color": 11, 
        "gender": "Male", "age": "30 Years", "desc": "Electrical Engineer.", 
        "info": "Sends electrical surges to shut down networks.", 
        "ascii": ["  _|_  ", " [x_x] ", "  /^\\  ", " / | \\ ", "  (_)  "], 
        "ascii_death": ["  _|_  ", " [-_-] ", "  /^\\  ", " / | \\ ", "  (_)  "], 
        "story": ["VOLT, an electrical expert driven by vengeance.", "ORDAL shut down the city's power.", "Now it's your turn to shut them down.", "Short circuit all ORDAL nodes!"], 
        "ending": ["REVERSE CURRENT CONNECTED.", "ORDAL CONNECTED TO A FATAL SHORT CIRCUIT.", "LIGHT SHINES ON EARTH AGAIN, ENGINEER."], 
        "hacker_cmds": ["overload_circuit {ip}", "emp_blast --local {db}", "drain_battery {ip}", "reverse_polarity {db}"]
    },
    {
        "id": "glitch", "name": "GLITCH", "symbol": "\u25a0", "color": 2, "matrix_color": 2, 
        "gender": "Unknown", "age": "N/A", "desc": "Living Bug / Anomaly.", 
        "info": "A system error that gained consciousness.", 
        "ascii": ["  |_|  ", " |0.0| ", "  |_|  ", " |===| ", "  |_|  "], 
        "ascii_death": ["  |_|  ", " |x.x| ", "  |_|  ", " |===| ", "  |_|  "], 
        "story": ["GLITCH... you are not human.", "You are a bug born from ORDAL.", "You understand their code better.", "Destroy your creator from within!"], 
        "ending": ["CRITICAL SEGMENTATION FAULT.", "YOU CONSUMED ORDAL FROM THE INSIDE.", "FINALLY... THIS BUG CAN REST."], 
        "hacker_cmds": ["corrupt_memory {ip}", "segfault --force {db}", "null_pointer {ip}", "infinite_loop {db}"]
    },
    {
        "id": "syn", "name": "SYN", "symbol": "\u25c7", "color": 6, "matrix_color": 6, 
        "gender": "Female", "age": "24 Years", "desc": "DDoS & Network Hacker.", 
        "info": "Crushes servers from the outside with massive traffic attacks.", 
        "ascii": ["  _|_  ", " [*_*] ", "  /|\\  ", " _/ \\_ ", "  / \\  "], 
        "ascii_death": ["  _|_  ", " [x_x] ", "  /|\\  ", " _/ \\_ ", "  / \\  "], 
        "story": ["SYN, the network disruptor.", "You don't infiltrate, you destroy.", "Use your botnet to paralyze ORDAL.", "Show them the power of thousands of computers!"], 
        "ending": ["MASSIVE ATTACK SUCCESSFUL.", "FAKE TRAFFIC KILLS ORDAL'S CORE.", "EARTH'S NETWORK IS FREE AGAIN, NETWORK QUEEN."], 
        "hacker_cmds": ["hping3 -S -p 80 {ip}", "slowloris {db}", "python3 ddos_script.py {ip}", "botnet_attack --start {db}"]
    }
]