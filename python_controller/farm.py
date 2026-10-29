import subprocess
import json
import time
import os
from datetime import datetime

def run_adb(cmd):
    """Run adb command"""
    result = subprocess.run(f"adb {cmd}", shell=True, capture_output=True, text=True)
    return result.stdout

def get_devices():
    out = run_adb("devices")
    devices = [line.split()[0] for line in out.splitlines()[1:] if "device" in line]
    return devices

def install_apk(apk_path, device_id):
    print(f"[INSTALL] Installing {apk_path} on {device_id}")
    run_adb(f"-s {device_id} install -r {apk_path}")
    print("[OK] Installed")

def tap(x, y, device_id):
    print(f"[TAP] {x},{y}")
    run_adb(f"-s {device_id} shell input tap {x} {y}")

def swipe(x1, y1, x2, y2, duration=300, device_id=None):
    print(f"[SWIPE] {x1},{y1} -> {x2},{y2}")
    run_adb(f"-s {device_id} shell input swipe {x1} {y1} {x2} {y2} {duration}")

def screenshot(device_id, save_path):
    run_adb(f"-s {device_id} exec-out screencap -p > {save_path}")
    print(f"[SCREENSHOT] Saved to {save_path}")

def run_flow(flow_path, device_id):
    with open(flow_path) as f:
        data = json.load(f)
    
    print(f"--- Running flow: {data['flow']} ---")
    os.makedirs("reports", exist_ok=True)
    
    # Start logcat
    log_file = f"reports/{data['flow']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    logcat = subprocess.Popen(f"adb -s {device_id} logcat > {log_file}", shell=True)
    
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
        logcat.terminate()
        print(f"[LOGS] Saved to {log_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", help="Path to APK")
    parser.add_argument("--test", help="Path to flow JSON")
    parser.add_argument("--device", help="Device ID", default=None)
    args = parser.parse_args()

    devices = get_devices()
    if not devices:
        print("No devices found. Connect phone and enable USB Debugging")
        exit(1)
    
    device = args.device or devices[0]
    print(f"Using device: {device}")

    if args.install:
        install_apk(args.install, device)
    if args.test:
        run_flow(args.test, device)