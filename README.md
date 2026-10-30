# PhoneLab

My on-device Android lab.
No PC. No Root.

I built this so my phone can test itself.

### Why

PC ADB needs cable + drivers.
Mine runs on my phone via LADB.

### How I Run It

My Phone -> Termux -> LADB -> Android

#### 1. Termux
From F-Droid only.

pkg update -y
pkg install python git unzip -y
termux-setup-storage

#### 2. LADB
From my Releases > Tools:

https://github.com/Topshugar/phonelab/releases/tag/Tools

File: `my-ladb-apk.zip` -> `app-debug.apk`

#### 3. Pair (once, 60s)

- Settings > About Phone
- Tap Build 7x
- Dev Options > Wireless Debugging
- Pair with code
- Open LADB, enter code

#### 4. Test

git clone https://github.com/Topshugar/phonelab.git
cd phonelab
pip install -r http://requirements.txt
python python_controller/farm.py \
  --test flows/login_flow.json

I check:
- `recordings/` - videos
- `reports/` - logs

### My Flows

`flows/my_test.json`:

```json
{
  "flow": "my_test",
  "steps": [
    {"action": "tap", "x": 540, "y": 1200},
    {"action": "wait", "seconds": 2},
    {"action": "screenshot", "name": "home"}
  ]
}
### Structure
flows/ - my tests
python_controller/farm.py - runner
record.py - recorder
report.py - report
### My Roadmap

- v0.1 Core - done
- v0.2 Recorder
- v0.3 Tap to JSON
- v0.4 Multi-phone
- v1.0 Dashboard

### By Me

Built by Topshugar.
LADB base by tytydraco.

MIT
