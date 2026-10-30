# PhoneLab - On-Device Android Lab

> A lightweight framework for running ADB operations directly on Android without a PC.

PhoneLab uses LADB to create a local ADB shell via Wireless Debugging loopback, allowing you to run `farm.py` and other automation directly on-device.

### Download

**LADB APK (inside ZIP):** https://github.com/Topshugar/phonelab/releases/download/Tools/my-ladb-apk.zip

Release tag: `Tools` - File: `my-ladb-apk.zip` containing `app-debug.apk`

---

### Complete Walkthrough

#### Prerequisites

- Android 11 or higher
- Device with Wireless Debugging option
- File Manager that can extract ZIP (or ZArchiver)
- Termux

#### Step 1: Termux Setup

1. Install Termux from F-Droid (not Play Store - Play Store version is outdated)
2. Open Termux and run:

```bash
pkg update && pkg upgrade -y
pkg install python git unzip -y
termux-setup-storage
Allow storage permission when prompted.

#### Step 2: Download the ZIP Artifact

1. Tap the download link above
2. Wait for `my-ladb-apk.zip` to finish in Downloads
3. File is ∼3.8MB compressed

#### Step 3: Extract APK from ZIP

The file is distributed as ZIP because GitHub mobile blocks direct APK upload.

*File Manager:*
Downloads > Tap `my-ladb-apk.zip` > Extract > you get `app-debug.apk`

*Termux:*
cd ~/storage/downloads
unzip my-ladb-apk.zip
> If extraction fails, install ZArchiver from Play Store.

#### Step 4: Install APK

1. Tap `app-debug.apk` > Install
2. If blocked: Settings > Apps > Special Access > Install unknown apps > Allow File Manager
3. Verify LADB appears in app drawer

#### Step 5: Wireless ADB Pairing (One-Time)

1. Settings > About Phone > Tap Build Number 7 times
2. Settings > System > Developer Options > Enable Wireless Debugging
3. Inside Wireless Debugging > Pair device with pairing code
4. Note IP:PORT and 6-digit code
5. Open LADB > Enter port and code > Pair
6. LADB shows Connected

> You only need Wi-Fi for 60 seconds to get the code. After pairing, it works offline.

#### Step 6: Run PhoneLab
git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r requirements.txt
python farm.py
---

### Roadmap

- *v0.1 - Core*
- [ ] v0.2 - Screen Recorder + HTML Report
- [ ] v0.3 - Record Mode
- [ ] v0.4 - Multi-phone Parallel
- [ ] v0.5 - iOS Support
- [ ] v1.0 - Web Dashboard[x]

### Troubleshooting

- *Can't install APK:* Enable Install unknown apps for File Manager
- *LADB offline:* Re-enable Wireless Debugging
- *Can't extract ZIP:* Use ZArchiver
- *farm.py permission denied:* Run `termux-setup-storage`

### Requirements

- Android 11+
- Wireless Debugging support
- ∼50MB free

### Credits

- LADB by tytydraco - free build compiled from source
- PhoneLab © Topshugar
