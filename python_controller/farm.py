import subprocess
import json
import time
import os
import sys
import shutil
from datetime import datetime

# Add root to import record.py and report.py
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)
LOCAL_DIR = os.path.join(ROOT_DIR, "recordings")

def has_adb():
    return shutil.which("adb") is not None

def run_adb(cmd):
    """Run adb command - supports both Termux ADB and LADB"""
    if has_adb():
        full = f"adb {cmd}"
    else:
        # LADB mode - strip adb prefix, run direct shell command
        if cmd.startswith("shell "):
            full = cmd.replace("shell ", "", 1)
        elif "shell" in cmd:
            full = cmd.split("shell ")[-1]
        else:
            full = cmd
    result = subprocess.run(full, shell=True, capture_output=True, text=True)
    return result.stdout

def get_devices():
    if not has_adb():
        return ["local_device"]  # LADB has no device list, single device
    out = run_adb("devices")
    devices = [line.split()[0] for line in out.splitlines()[1:] if "device" in line]
    return devices

def install_apk(apk_path, device_id):
    print(f"[INSTALL] Installing {apk_path} on {device_id}")
    if has_adb():
        run_adb(f"-s {device_id} install -r {apk_path}")
    else:
        subprocess.run(f"pm install -r {apk_path}", shell=True)
    print("[OK] Installed")

def tap(x, y, device_id):
    print(f"[TAP] {x},{y}")
    run_adb(f"-s {device_id} shell input tap {x} {y}" if has_adb() else f"input tap {x} {y}")

def swipe(x1, y1, x2, y2, duration=300, device_id=None):
    print(f"[SWIPE] {x1},{y1} -> {x2},{y2}")
    run_adb(f"-s {device_id} shell input swipe {x1} {y1} {x2} {y2} {duration}" if has_adb() else f"input swipe {x1} {y1} {x2} {y2} {duration}")

def screenshot(device_id, save_path):
    if has_adb():
        run_adb(f"-s {device_id} exec-out screencap -p > {save_path}")
    else:
        subprocess.run(f"screencap -p {save_path}", shell=True)
    print(f"[SCREENSHOT] Saved to {save_path}")

def start_recording(duration=30):
    """Hook into your root record.py"""
    try:
        import record
        return record.record(duration=duration)
    except Exception as e:
        print(f"[RECORD] Failed, trying direct: {e}")
        filename = f"phonelab_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        os.makedirs(LOCAL_DIR, exist_ok=True)
        remote = f"/sdcard/Movies/phonelab/{filename}"
        local = os.path.join(LOCAL_DIR, filename)
        subprocess.run(f"mkdir -p /sdcard/Movies/phonelab", shell=True)
        subprocess.run(f"screenrecord --time-limit {duration} {remote}", shell=True)
        if os.path.exists(remote):
            shutil.copy(remote, local)
            return local
        return None

def run_flow(flow_path, device_id):
    with open(flow_path) as f:
        data = json.load(f)

    print(f"--- Running flow: {data['flow']} ---")
    print(f"[Mode] {'Termux ADB (main)' if has_adb() else 'LADB direct (alternative)'}")
    os.makedirs("reports", exist_ok=True)
    os.makedirs(LOCAL_DIR, exist_ok=True)

    # Start recording
    video = start_recording(duration=180)

    # Start logcat only if ADB exists
    log_file = f"reports/{data['flow']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    logcat = None
    if has_adb():
        logcat = subprocess.Popen(f"adb -s {device_id} logcat > {log_file}", shell=True)
    else:
        logcat = subprocess.Popen(f"logcat > {log_file}", shell=True)

    try:
        for step in data["steps"]:
            action = step["action"]
            if action == "tap":
                tap(step["x"], step["y"], device_id)
            elif action == "swipe":
                swipe(step["from"][0], step["from"][1], step["to"][0], step["to"][1], device_id=device_id)
            elif action == "wait":
                time.sleep(step["seconds"])
            elif action == "screenshot":
                screenshot(device_id, f"reports/{step['name']}.png")
            time.sleep(1)
    finally:
        if logcat:
            logcat.terminate()
        print(f"[LOGS] Saved to {log_file}")
        
        # Generate report using root report.py
        if video:
            try:
                import report
                report.generate(video)
            except Exception as e:
                print(f"[REPORT] Failed: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", help="Path to APK")
    parser.add_argument("--test", help="Path to flow JSON")
    parser.add_argument("--device", help="Device ID", default=None)
    parser.add_argument("--record", type=int, default=30, help="Record duration")
    args = parser.parse_args()

    devices = get_devices()
    if not devices:
        print("No devices found. Connect phone and enable USB Debugging")
        exit(1)

    device = args.device or devices[0]
    print(f"Using device: {device} | Mode: {'ADB' if has_adb() else 'LADB'}")

    if args.install:
        install_apk(args.install, device)
    if args.test:
        run_flow(args.test, device)