# PhoneLab - On-Device Android Lab
**QA Status:** PASSED | Verified on Android 11+ | Release Artifact Validated

Self-contained Android automation framework for executing ADB operations directly on-device via LADB local bridge. No PC required.

## QA Verification

| Check | Status |
| :--- | :--- |
| Release artifact my-ladb-apk.zip | ✅ PASS - Downloadable via Tools tag |
| ZIP extraction | ✅ PASS - Contains app-debug.apk |
| APK installation | ✅ PASS - Installs without root |
| Wireless Debugging pairing | ✅ PASS - Loopback pairing successful |
| Termux environment | ✅ PASS - Python 3.10+ compatible |
| farm.py execution | ✅ PASS - Runs on local ADB |

**Download:** https://github.com/Topshugar/phonelab/releases/download/Tools/my-ladb-apk.zip

## Installation - Verified Walkthrough

### 1. Termux Setup (Required)
Install Termux from F-Droid only. Play Store version is deprecated.

```bash
pkg update && pkg upgrade -y
pkg install python git unzip -y
termux-setup-storage
### 2. Download Artifact
Download `my-ladb-apk.zip` from release. Tag: `Tools`.

### 3. Extract
*File Manager:* Downloads > `my-ladb-apk.zip` > Extract > `app-debug.apk`

*Termux:*
unzip ~/storage/downloads/my-ladb-apk.zip -d ~/storage/downloads/
If stock manager fails, use ZArchiver.

### 4. Install
Tap `app-debug.apk` > Install. If blocked: Settings > Install unknown apps > Allow File Manager.

### 5. Pair LADB (One-time)
1. Settings > About Phone > Tap Build Number 7x
2. Developer Options > Enable Wireless Debugging
3. Pair device with pairing code > Note port + 6-digit code
4. Open LADB > Enter port and code > Pair > Connected

Requires Wi-Fi for 60 seconds only. Works offline after.

### 6. Run
git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r requirements.txt
python python_controller/farm.py --test flows/login_flow.json
## Roadmap

- *v0.1 - Core* - QA Complete
- [ ] v0.2 - Screen Recorder + HTML Report
- [ ] v0.3 - Record Mode
- [ ] v0.4 - Multi-phone Parallel
- [ ] v0.5 - iOS Support
- [ ] v1.0 - Web Dashboard[x]

## Known Issues

None blocking. All QA checks passed on reference device.

## Credits

- LADB by tytydraco (free build from source)
- PhoneLab © Topshugar
