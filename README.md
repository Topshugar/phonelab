# 📱 PhoneLab

On-device Android Automation Framework.
Zero PC Dependency. Zero Root Requirement.

## 📖 Overview

PhoneLab is an Android automation framework that executes ADB commands locally on the device via LADB loopback, orchestrated by Termux.

Architecture:
Termux (Python Runtime) -> LADB (Local ADB Shell) -> Android Framework

## ❌ Problem Statement

Traditional ADB automation requires:
1. External host machine
2. USB debugging cable
3. Platform drivers

## ✅ Solution

PhoneLab implements self-hosted automation:
- 🔌 LADB provides local ADB server
- 🐍 Termux provides Python execution environment
- ⚙️ Framework provides flow-based test orchestration

## 🚀 Features

- 🔌 Local ADB execution via LADB
- 📹 Screen recording capture
- 📊 HTML report generation
- 📝 JSON-based flow definition
- 📴 Offline execution capability
- 🧩 Modular controller architecture

## 📋 Prerequisites

- 🤖 Android 11+
- 📦 Termux (F-Droid distribution)
- 🔧 LADB application

## 💾 Installation

### 1. 🐍 Termux Environment

```bash
pkg update -y
pkg install python git unzip -y
termux-setup-storage
### 2. 📦 LADB Binary

Source:
https://github.com/Topshugar/phonelab/releases/tag/Tools
Artifact: my-ladb-apk.zip
Payload: app-debug.apk
### 3. 🔗 LADB Pairing

Procedure:
Settings > About Phone > Build Number (7x)
Developer Options > Wireless Debugging > Enable
Wireless Debugging > Pair with pairing code
LADB > Input pairing code > Establish connection
## ▶️ Execution
git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r requirements.txt
python python_controller/farm.py --test flows/login_flow.json
Artifacts:
recordings/ - MP4 capture
reports/    - HTML execution logs
## 📝 Flow Definition

Example:
{
  "flow": "login",
  "steps": [
    {
      "action": "tap",
      "x": 540,
      "y": 1200
    },
    {
      "action": "wait",
      "seconds": 2
    },
    {
      "action": "screenshot",
      "name": "result"
    }
  ]
}
Supported Actions:
- 👆 `tap`: `x`, `y` coordinates
- 👉 `swipe`: `x1`, `y1`, `x2`, `y2`, `duration`
- ⏱️ `wait`: `seconds`
- 📸 `screenshot`: `name`

## 📁 Directory Structure
phonelab/
├── flows/                      # Flow definitions
├── python_controller/
│   └── farm.py                 # Execution engine
├── record.py                   # Media capture module
├── report.py                   # Report generator
├── requirements.txt            # Dependencies
└── README.md
## 🗺️ Roadmap

- v0.1: Core ADB interface, flow parser
- v0.2: Recording module, report generator
- v0.3: Input capture, JSON transpiler
- v0.4: Multi-device orchestration
- v1.0: Web dashboard interface

## 🔗 Dependencies

- LADB Core: tytydraco
- Runtime: Termux
- Language: Python 3.11+

## 👤 Author

Topshugar

## 📄 License

MIT License - See LICENSE
