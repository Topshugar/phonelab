# PhoneLab - On-Device Android Lab & Task Farm

> A lightweight, on-device automation framework for ADB orchestration, task farming, and environment isolation - without a PC. Tested on Redmi A2+ and compatible with all Android 11+ devices.

PhoneLab enables you to run ADB commands, farm tasks, and manage local workspaces directly on your phone using a local ADB bridge.

### Compatibility

- **Minimum:** Android 11+ with Wireless Debugging
- **Tested & Optimized:** Redmi A2+ (Android Go), but works on any modern Android device
- **Storage:** ~50MB free

### Installation & LADB Deployment

We provide a pre-compiled free build of LADB so you can run PhoneLab without a PC or paid app.

#### 1. Download

**Latest:** [my-ladb-apk.zip](https://github.com/Topshugar/phonelab/releases/latest/download/my-ladb-apk.zip)

#### 2. Extract APK from ZIP

The file is distributed as ZIP. You must extract first:

**File Manager:** Downloads > tap `my-ladb-apk.zip` > Extract > you get `app-debug.apk`

**Termux:** `unzip ~/storage/downloads/my-ladb-apk.zip`

If your File Manager can't extract, install **ZArchiver** (free, 5MB).

#### 3. Install

Tap `app-debug.apk` > Install. If blocked, allow "Install unknown apps" for File Manager.

#### 4. One-Time Pairing

1. Settings > About Phone > Tap Build Number 7x
2. Settings > Developer Options > Enable **Wireless Debugging**
3. Inside Wireless Debugging > **Pair device with pairing code**
4. Note Port and 6-digit code
5. Open LADB > Enter Port + Code > Pair
6. Once Connected, LADB will work offline forever

> You only need WiFi for 60 seconds to get the pairing code. After that, it works without internet.

#### 5. Run PhoneLab

```bash
git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r requirements.txt
python farm.py
### Roadmap

- Free LADB artifact distribution
- Multi-device compatibility (Android 11+)
- [ ] Auto-recovery task queue
- [ ] Battery/thermal protection
- [ ] Multi-device fleet mode
- [ ] Local dashboard

### Credits

- LADB by tytydraco - free build compiled from source for testing
- PhoneLab © Topshugar
