# PhoneLab

Turn your phone into a 
self-hosted test lab.
No PC. No Root.

> Python + LADB + Termux
> Works 100% on-device.

## Why?

PC ADB needs cable + drivers.
PhoneLab runs on your phone.

## Features

- On-device ADB via LADB
- Auto screen record
- HTML reports
- JSON flows
- Works offline

## How It Works

Termux -> LADB -> Android

## Quick Start

### 1. Install Termux
Get it from F-Droid.
Play Store is broken.

pkg update -y
pkg install python git unzip -y
termux-setup-storage

### 2. Get LADB
Download from Releases:
Tools tag -> zip -> apk

Link:
http://github.com/Topshugar/
phonelab/releases/tag/Tools

### 3. Pair LADB
One time only. 60 sec.

- Settings > About Phone
- Tap Build 7x
- Dev Options >
  Wireless Debugging
- Pair with code
- Open LADB, enter code

### 4. Run Test
git clone https://
 http://github.com/Topshugar/
 http://phonelab.git
cd phonelab
pip install -r
 http://requirements.txt
python python_controller/
 http://farm.py --test flows/
 login_flow.json

Videos go to:
`./recordings/`
Logs go to:
`./reports/`

## Project

flows/ - test JSON
python_controller/
 http://farm.py - main runner
http://record.py - recorder
http://report.py - reports

## Write a Flow

```json
{
  "flow": "my_test",
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
## Roadmap

- v0.1 Core - DONE
- v0.2 Recorder + Report
- v0.3 Record taps to JSON
- v0.4 Multi-phone
- v1.0 Web Dashboard

Want to build?
See http://CONTRIBUTING.md

## Contributing

PRs welcome!
Check Issues tab.

## Credits

- LADB by tytydraco
- Built by Topshugar
