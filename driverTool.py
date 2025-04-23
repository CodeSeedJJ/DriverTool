import os
import csv
from datetime import datetime
import wmi

# Output directory and file
output_dir = r"D:\DriverEasier"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = os.path.join(output_dir, f"scan_results_{timestamp}.txt")

def ensure_output_dir():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def scan_drivers():
    c = wmi.WMI()
    print("[+] Scanning installed devices and drivers...\n")
    results = []

    for device in c.Win32_PnPSignedDriver():
        name = device.DeviceName or "Unknown Device"
        version = device.DriverVersion or "Unknown"
        date = device.DriverDate or "Unknown"
        vendor = device.Manufacturer or "Unknown Vendor"

        line = f"{name} | Driver: {version} | Date: {date} | Vendor: {vendor}"
        print(line)
        results.append(line)

    return results

def save_results(results):
    with open(output_file, "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")
    print(f"\n[+] Results saved to: {output_file}")

def main():
    ensure_output_dir()
    results = scan_drivers()
    save_results(results)

if __name__ == "__main__":
    main()
