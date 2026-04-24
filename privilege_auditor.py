import subprocess
import os

def run_audit():
    print("--- Local Privilege & Account Audit ---")
    
    commands = {
        "User Accounts": "net user",
        "Administrator Group Members": "net localgroup Administrators",
        "Guest Account Status": "net user Guest"
    }

    results = {}

    for label, cmd in commands.items():
        print(f"[*] Auditing: {label}...")
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
            results[label] = output
        except subprocess.CalledProcessError as e:
            results[label] = f"Error: {e.output.decode()}"

    print("\n" + "="*50)
    print("AUDIT SUMMARY")
    print("="*50)

    # Check for Guest Account Vulnerability
    if "Account active               Yes" in results.get("Guest Account Status", ""):
        print("[!] SECURITY ALERT: Guest Account is ENABLED. (Non-Compliant)")
    else:
        print("[+] Guest Account is disabled. (Compliant)")

    # Display Admin group members for manual review
    print("\n[!] Review Administrator Group Members:")
    # Clean up the 'net localgroup' output to show only the members
    admin_output = results.get("Administrator Group Members", "")
    print(admin_output)

    print("="*50)
    print("[*] Audit complete. Review the output above for unauthorized accounts.")

if __name__ == "__main__":
    run_audit()