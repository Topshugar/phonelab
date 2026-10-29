# PhoneLab — Open Device Farm for Mobile QA

> Test your app on real phones. Python + ESP32 gantry that taps and swipes.

## Why?
Emulators lie. Real phones crash differently. PhoneLab is for real-hardware QA.

- 1 phone now, 10+ with gantry
- No root, just ADB + Python
- OpenCV checks for crashes

## Structure
phonelab/
├── python_controller/farm.py
├── firmware/
├── flows/ # JSON tests
└── reports/ # logs + screenshots

## Quick Start
```bash
pip install -r requirements.txt
adb devices
python python_controller/farm.py --install app.apk
python python_controller/farm.py --test flows/login_flow.json
## Example Test
`flows/login_flow.json`
{
  "flow": "login",
  "steps": [
    {"action": "tap", "x": 540, "y": 1200},
    {"action": "swipe", "from": [500, 1500], "to": [500, 500]}
  ]
}
## Roadmap
- v0.1 Software core
- v0.2 Gantry firmware
- v0.3 Vision
- v1.0 Full farm

## Safety
For QA/testing only. Not for fake engagement.

## License
MIT
