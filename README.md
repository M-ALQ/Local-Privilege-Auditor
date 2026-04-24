# Local Privilege Auditor
A script designed to audit local user accounts and administrative group memberships for security compliance.

### Features
- **Administrative Group Audit**: Extracts the list of users with local administrator privileges for "Least Privilege" review.
- **Guest Account Verification**: Specifically checks if the default Guest account is active, identifying a common security misconfiguration.
- **Account Inventory**: Lists all local user accounts present on the system.

### How It Works
The script interfaces with Windows management commands via the `subprocess` module to query the Local Security Authority (LSA). It parses the returned data to identify high-risk configurations, such as an active Guest account or unauthorized administrative users.

### Usage
This script requires Administrative privileges to query group memberships:
1. Open Command Prompt as Administrator.
2. Run: `python privilege_auditor.py`
