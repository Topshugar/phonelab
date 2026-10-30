# 📱 PhoneLab

> Turn any Android phone into a self-hosted automation lab. No PC. No Root. Just LADB + Termux.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Android](https://img.shields.io/badge/Android-11%2B-brightgreen)](https://developer.android.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

### Why PhoneLab?
PC-based ADB is annoying. You need cables, drivers, and your PC always on. PhoneLab runs **100% on-device** using LADB's local ADB bridge. Your phone tests itself.

**Features:**
- 🔌 **On-Device ADB** - Uses LADB loopback, no PC needed
- 📹 **Auto Screen Record** - Every test run is recorded
- 📊 **HTML Reports** - Shareable reports with video
- 🔄 **JSON Flows** - Write tests like `{"action": "tap", "x": 500, "y": 800}`
- 📦 **Works Offline** - After 60s setup, no Wi-Fi needed

### How it Works
`Termux (Python) -> LADB (local ADB) -> Android System -> ScreenRecord`

### 🚀 Quick Start

**1. Install Termux** (from F-Droid ONLY, Play Store version is dead)
```bash
pkg update -y && pkg install python git unzip -y
termux-setup-storage
*2. Get LADB APK*
Download `my-ladb-apk.zip` from https://github.com/Topshugar/phonelab/releases/tag/Tools -> Extract -> Install `app-debug.apk`

*3. Pair LADB (60 seconds, one-time)*
Settings > About Phone > Tap Build Number 7x > Developer Options > Wireless Debugging > Pair with code -> Open LADB and enter code

*4. Run Your First Test*
git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r requirements.txt
python python_controller/farm.py --test flows/login_flow.json
Videos + reports appear in `./recordings/` and `./reports/`

### 📂 Project Structure
phonelab/
├── flows/                  # Your test flows (JSON)
├── python_controller/
│   └── farm.py             # Main runner
├── record.py               # Screen recorder module
├── report.py               # HTML report generator
└── README.md
### ✍️ Writing a Flow
{
  "flow": "my_app_test",
  "steps": [
    {"action": "tap", "x": 540, "y": 1200},
    {"action": "wait", "seconds": 2},
    {"action": "screenshot", "name": "result"}
  ]
}
### 🗺️ Roadmap
- *v0.1* Core on-device ADB + Flows
- [ ] *v0.2* Screen Recorder + HTML Report (Claim this!)
- [ ] *v0.3* Record Mode - Tap to generate JSON
- [ ] *v0.4* Multi-phone parallel
- [ ] *v1.0* Web Dashboard[x]

Want to build one? Check [CONTRIBUTING.md](CONTRIBUTING.md) -> https://github.com/Topshugar/phonelab/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22

### 🤝 Contributing
We track everything on the Project Board. PRs welcome!

### Credits
- LADB by https://github.com/tytydraco/ladb
- Built by Topshugar
