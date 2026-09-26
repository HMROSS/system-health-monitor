# System Health Monitor

A Python command-line tool that monitors basic system health and generates a readable health report.

## Features

- Displays computer name and operating system
- Shows system uptime
- Monitors CPU, memory, and disk usage
- Classifies usage as OK, WARNING, or CRITICAL
- Handles unavailable disk information
- Saves the latest health report to a text file
- Supports Windows and Linux disk paths

## Requirements

- Python 3
- psutil 7.2.2

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py

## Example Output

===== SYSTEM HEALTH REPORT ======

Generated: 2026-09-26 20:30:00

Computer: Legion-KIANO
Operating System: Windows
Uptime: 5 days, 4 hours, 39 minutes, 46 seconds

CPU: 16.7% - OK
Memory: 47.2% - OK
Disk: 75.6% - WARNING
```
