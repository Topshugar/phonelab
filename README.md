# 📱 PhoneLab — Real Phone Testing, Not Emulators

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4%EF%B8%8F-red)](https://github.com)

> **Emulators lie. Real phones crash differently.** PhoneLab runs your app on REAL Android phones and finds crashes emulators miss.

### 🎥 Demo
![Demo](reports/demo.gif)
*Tap, Swipe, Screenshot, Logs - Fully Automated*

---

### Why PhoneLab?
- ❌ Emulators: No real sensors, fake performance
- ✅ PhoneLab: Real device, real crash logs, real screenshots

### ✨ Features
- 🔌 Plug & Play - Just `adb devices`
- 🤖 JSON test flows - No code needed
- 📸 Auto screenshots + logcat on failure
- 🐍 100% Python - Hackable in 5 mins
- 📊 HTML reports

### 🚀 Quick Start - 30 Seconds
```bash
git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r requirements.txt

# 1. Connect phone with USB Debugging ON
adb devices

# 2. Run your first test
python python_controller/farm.py --test flows/login_flow.json
That's it. Check `reports/` folder for screenshots + logs.

### 🧪 Write a Test - No Coding
`flows/login_flow.json`
{
  "flow": "login_test",
  "steps": [
    {"action": "tap", "x": 540, "y": 1200},
    {"action": "wait", "seconds": 2},
    {"action": "screenshot", "name": "login_screen"}
  ]
}
### 🗺️ Roadmap
- v0.1 - Core http://farm.py
- [ ] v0.2 - Screen Recorder + HTML Report
- [ ] v0.3 - Record Mode: Click to generate JSON
- [ ] v0.4 - Multi-phone parallel
- [ ] v0.5 - iOS support
- [ ] v1.0 - Web Dashboard

### 🤝 Want to Contribute?
We are looking for contributors! Check [CONTRIBUTING.md](CONTRIBUTING.md)

### 📄 License
MIT - Use it for any project.

---
*Star ⭐ this repo if emulators have ever wasted your time.*
