# PhoneLab

> On-device Android automation lab.
> No PC. No Root. Just your phone.

[[License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[[Android](https://img.shields.io/badge/Android-11%2B-brightgreen.svg)](#)
[[PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue.svg)](CONTRIBUTING.md)

### Why PhoneLab?

Normal ADB needs a PC, cable, drivers.

PhoneLab runs ADB directly on your
phone using LADB. Your phone tests itself.

### Features

- **On-Device ADB** - LADB loopback
- **Screen Record** - Auto record tests
- **HTML Reports** - With video embed
- **JSON Flows** - Simple tap/swipe
- **Offline** - Works after pairing

### How It Works

Termux (Python)
   -> LADB (local ADB)
   -> Android System

### Quick Start

#### 1. Termux
Install from F-Droid only.

```bash
pkg update -y
pkg install python git unzip -y
termux-setup-storage
#### 2. Download LADB
Go to Releases > Tools tag.

Download `my-ladb-apk.zip`
Extract and install `app-debug.apk`

https://github.com/Topshugar/phonelab/releases/tag/Tools

#### 3. Pair LADB (once)

1. Settings > About Phone
2. Tap Build Number 7x
3. Developer Options >
   Wireless Debugging ON
4. Pair device with code
5. Open LADB, enter port + code

Needs Wi-Fi for 60s only.

#### 4. Run
git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r requirements.txt
python python_controller/farm.py \
  --test flows/login_flow.json
Output:
- `recordings/` - videos
- `reports/` - logs + html

### Write a Flow

Create `flows/my_test.json`:
{
  "flow": "my_test",
  "steps": [
    {"action": "tap", "x": 540, "y": 1200},
    {"action": "wait", "seconds": 2},
    {"action": "screenshot", "name": "home"}
  ]
}
Actions: `tap`, `swipe`, `wait`, `screenshot`

### Project Structure
phonelab/
├── flows/ - your tests
├── python_controller/
│   └── farm.py - runner
├── record.py
├── report.py
└── README.md
### Roadmap

- v0.1 - Core ADB + Flows
- [ ] v0.2 - Recorder + Report
- [ ] v0.3 - Record Mode (tap to JSON)
- [ ] v0.4 - Multi-phone
- [ ] v1.0 - Dashboard[x]

Check `CONTRIBUTING.md` to claim a task.

### Contributing

1. Pick issue from board
2. Fork + branch
3. PR

### Credits

- LADB by tytydraco
- PhoneLab by Topshugar

### License

MIT
