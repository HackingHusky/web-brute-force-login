# Web Login Brute Force Script

A lightweight, command-line Python script designed to perform dictionary-based brute-force attacks against HTTP POST login endpoints. It automates credential auditing by submitting a fixed username alongside a list of target passwords.

## 🚀 Features

- **Automated POST Requests**: Submits credentials using standard application/x-www-form-urlencoded payloads.
- **Success Identification**: Scans target HTTP response bodies for a successful login signature (`"Login successful"`).
- **Real-time Console Output**: Prints the tracking status of every password attempt instantly.
- **Zero External Dependencies**: Operates entirely within standard Python environments (requires only the third-party `requests` library).

## 📋 Requirements

- **Python**: Version 3.6 or higher.
- **Library**: `requests` package.

You can install the required dependency via pip:
```bash
pip install requests
```

## 🛠️ Usage

Run the script from your terminal by passing the target URL, target username, and the path to your password dictionary file as positional arguments.

```bash
python web_brute_force.py <URL> <USERNAME> <PASSWORD_FILE>
```

### Example Command

```bash
python web_brute_force.py http://example.com admin passwords.txt
```

## ⚙️ Input File Format

The password dictionary file should contain one password per line with no additional delimiter characters:

```text
password123
admin2026
qwerty
letmein123
```

## 📜 Disclaimer

> [!WARNING]
> This tool is developed strictly for authorized security auditing, penetration testing, and educational purposes. Running this script against targets without explicit, prior written consent from the asset owner is illegal and violates computer fraud laws. The developers assume no liability for misuse or damage caused by this software.
