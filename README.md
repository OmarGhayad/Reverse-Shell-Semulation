# 🐚 Reverse Shell Semulation

![Warning](https://img.shields.io/badge/Security-Awareness-red?style=for-the-badge\&logo=hackaday)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Linux-Compatible-yellow?style=for-the-badge\&logo=linux)
![Educational](https://img.shields.io/badge/Use-Educational-green?style=for-the-badge\&logo=bookstack)

---

## ⚠️ Disclaimer

This project is for **educational and awareness purposes only**. It demonstrates how a reverse shell works in a **controlled virtual environment**. Do **NOT** use it on real systems without explicit permission. The author is not responsible for misuse.

---

## 📝 Overview

This repository simulates a basic reverse shell attack:

* **Listener.py** → Runs on the attacker machine and listens for incoming reverse shell connections.
* **Shell.py** → Runs on the victim machine and connects back to the attacker, providing shell access.

The goal is to teach how attackers exploit reverse shells and how defenders can detect unusual outbound connections.

---

## ⚙️ How It Works

1. The **attacker machine** runs `Listener.py` to listen for incoming connections.
2. The **victim machine** runs `Shell.py` which connects back to the attacker’s IP and port.
3. Once connected, the attacker can execute commands on the victim’s system.

---

## 🚀 Setup & Execution

### 1. Clone Repository

```bash
git clone https://github.com/OmarGhayad/reverse-shell-semulation.git
cd reverse-shell-semulation
```

### 2. Run Listener (Attacker Machine)

On the **attacker machine** (Linux recommended), run:

```bash
python3 Listener.py
```

This will start listening on port **4444** by default.

### 3. Configure Victim Script

Edit **Shell.py** and replace the connection placeholders with your lab listener values (only inside the isolated lab):

```python
LISTENER_IP = "YOUR_LAB_IP"   # Attacker/Listener VM IP inside the lab
LISTENER_PORT = 4444
```

Example:

```python
LISTENER_IP = "192.168.1.100"
LISTENER_PORT = 4444
```

### 4. Run Victim Script (Victim Machine)

On the **victim simulation machine**, run:

```bash
python3 Shell.py
```

This will connect back to the attacker, creating a reverse shell.

---

## 📌 Notes

* Use only in a **virtual lab environment**.
* Demonstrates risks of reverse shells and why **outbound traffic monitoring** is critical.
* Helps raise awareness of **network security defenses**.

---

![Awareness](https://img.shields.io/badge/Cybersecurity-Awareness-orange?style=for-the-badge\&logo=shield)
