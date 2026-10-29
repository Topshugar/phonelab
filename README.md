# 📱 PhoneLab — Real Phone Testing, Not Emulators

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/Topshugar/phonelab?style=social)](https://github.com/Topshugar/phonelab)
[![PhoneLab CI](https://github.com/Topshugar/phonelab/actions/workflows/main.yml/badge.svg)](https://github.com/Topshugar/phonelab/actions/workflows/main.yml)

> **Emulators lie. Real phones crash differently.** PhoneLab runs your app on REAL Android phones and finds crashes emulators miss.

### 🎥 Demo
![Demo](https://raw.githubusercontent.com/Topshugar/phonelab/main/reports/demo.gif)
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
adb devices
python python_controller/farm.py --test flows/login_flow.json
### 🗺️ Roadmap
- *v0.1 - Core http://farm.py* - https://github.com/Topshugar/phonelab/blob/main/python_controller/farm.py
- [ ] *v0.2 - Screen Recorder + HTML Report* - https://github.com/Topshugar/phonelab/blob/main/CONTRIBUTING.md
- [ ] *v0.3 - Record Mode* - https://github.com/Topshugar/phonelab/blob/main/CONTRIBUTING.md
- [ ] *v0.4 - Multi-phone Parallel* - https://github.com/Topshugar/phonelab/issues
- [ ] *v0.5 - iOS Support* - https://github.com/Topshugar/phonelab/issues
- [ ] *v1.0 - Web Dashboard* - https://github.com/Topshugar/phonelab/projects

### 📸 How It Works
!https://raw.githubusercontent.com/Topshugar/phonelab/main/docs/architecture.png
_Real Phone -> ADB -> Python Controller -> Reports_

### 🤝 Contributing
We welcome contributions! Please see our https://github.com/Topshugar/phonelab/blob/main/CONTRIBUTING.md and our https://github.com/Topshugar/phonelab/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22.

### 📄 License
[MIT License](LICENSE) - Free for commercial use.
