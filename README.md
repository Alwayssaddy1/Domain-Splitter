# 🔪 SPLITTER  
### High-Performance Domain List Splitter for Huge Files

SPLITTER is a **fast, memory-efficient, and Termux-optimized** command-line tool for splitting **very large domain lists** into clean, sequential batch files.  
It is designed to handle **hundreds of millions of lines** safely without loading the full file into memory.

---

## 🚀 Why SPLITTER?

Most tools crash or get killed when handling massive files (100M+ lines).  
**SPLITTER uses streaming I/O**, progress tracking, and graceful shutdowns to ensure reliability even on low-RAM systems like **Android (Termux)**.

---

## ✨ Features

- ⚡ **Ultra-fast streaming split**
- 🧠 **Low RAM usage** (no full file load)
- 📊 **Progress bar + ETA**
- 📁 **Smart output location**
  - Output saved in the same directory as input file
- 📄 **Sequential output files**
  - `batch1.txt`, `batch2.txt`, `batch3.txt`, …
- 🧯 **Ctrl+C safe shutdown**
- 📱 **Termux & Linux compatible**
- 🧪 Tested with **100M+ domain lists**

---

## 📌 Use Cases

- OSINT & reconnaissance
- Bug bounty automation
- Mass scanning tools
- DNS / email analysis
- Any workflow involving **huge text lists**

---

## ⚠️ Important Notes

Input must be a plain text (.txt) file

Empty lines are ignored automatically

Domains are not modified

Safe to interrupt anytime using Ctrl+C

---

## 👨‍💻 Author

Coded by: SAD MAN
Contact: https://t.me/Alwayssaddy

---

## ⭐ Support

If this tool helps you:

⭐ Star the repository

🐛 Report issues

🔧 Submit pull requests

Your support keeps the project alive ❤️

---

## 🛠️ Installation

### Clone the repository
```bash
git clone https://github.com/yourusername/SPLITTER.git
cd SPLITTER
python splitter.py
