import os
import time
import shutil
import subprocess
from datetime import datetime

RECORD_DIR = "/sdcard/Movies/phonelab"
LOCAL_DIR = "./recordings"

def has_adb():
    return shutil.which("adb") is not None

def run(cmd):
    print(f"$ {cmd}")
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def record(duration=30, filename=None):
    os.makedirs(LOCAL_DIR, exist_ok=True)
    
    if not filename:
        filename = f"phonelab_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    
    remote = f"{RECORD_DIR}/{filename}"
    local = f"{LOCAL_DIR}/{filename}"
    
    if has_adb():
        print("[Mode] Termux ADB (main)")
        run(f"adb shell mkdir -p {RECORD_DIR}")
        run(f"adb shell screenrecord --time-limit {duration} {remote}")
        time.sleep(1)
        run(f"adb pull {remote} {local}")
    else:
        print("[Mode] LADB direct (alternative)")
        run(f"mkdir -p {RECORD_DIR}")
        run(f"screenrecord --time-limit {duration} {remote}")
        time.sleep(1)
        if os.path.exists(remote):
            run(f"cp {remote} {local}")

    if os.path.exists(local):
        print(f"✅ Saved: {local}")
        return local
    print("❌ Failed")
    return None

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--time", type=int, default=30)
    p.add_argument("--output", type=str)
    a = p.parse_args()
    record(min(a.time, 180), a.output)