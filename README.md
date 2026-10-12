## Log Files and Supported Formats

### What is a Log File?
A log file records events and activities from a system, application, or web server. It can contain IP addresses, timestamps, HTTP requests, status codes, and error messages.

### Common Log Types
- **Access Logs:** Record requests made to a web server.
- **Error Logs:** Record errors and problems.
- **Application Logs:** Record activities inside applications.
- **Security Logs:** Record login attempts and security events.
- **System Logs:** Record operating system activities.

### Log Formats
Log files can use different formats, such as Apache Common, Apache Combined, Nginx Access Logs, JSON, CSV, and Syslog.

### Our Project
Our project is a Python CLI tool that reads and analyzes Apache and compatible Nginx access logs.

It performs three main tasks:

1. **IP Masking:** Hides IPv4 addresses (`[MASKED_IP]`) to protect user privacy.
2. **HTTP Classification:** Groups HTTP status codes into INFO (2xx/3xx), WARNING (4xx), and ERROR (5xx).
3. **File Export:** Saves cleaned and classified logs with sequential numbering into separate text files.

### Supported Formats
- Apache Common Log Format
- Apache Combined Log Format
- Nginx access logs using compatible formats

Other formats, such as JSON, CSV, Windows Event Logs, and Apache Error Logs, are not currently supported.

### Project Directory and File Structure
The project is built with a modular approach and consists of the following files and directories:

```text
log_project_real/
├── main.py                  # Main CLI application and core functions
├── README.md                # Project documentation and usage guide
├── Samples/                 # Sample log files used for testing
│   ├── apache_logs.log      # Full-scale Apache access log
│   ├── broken_test.log      # Malformed / broken test log
│   └── second_test.log      # Secondary validation log
├── Output/                  # Output directory generated upon execution
│   ├── 01_Info.txt
│   ├── 02_Warning.txt
│   ├── 03_ERROR.txt
│   ├── 04_Critical.txt
│   └── 05_ALL_LOGS_WITH_MASKED_IP.txt
└── contributions/           # Individual team member contribution reports
```

#### Purpose of Folders and Scripts:
- **`main.py`**: The primary executable Python script. Built with pure standard libraries and divided into 5 modules:
  - **Module 1 (`read_log_file`):** Reads the input log file in UTF-8 and gracefully handles file errors (`FileNotFoundError`, `PermissionError`, `UnicodeError`).
  - **Module 2 (`mask_log_line`):** Validates and masks IPv4 addresses (4 octets, 0-255 range, no leading zeros) with `[MASKED_IP]`.
  - **Module 3 (`classify_and_filter_logs`):** Extracts HTTP request lines and status codes, classifying records into INFO (2xx/3xx), WARNING (4xx), and ERROR (5xx).
  - **Module 4 (`save_logs_to_file`):** Formats lines with index numbers and saves each log group into its designated output file.
  - **Module 5 (`main`):** Parses CLI flags (`--source`, `--output`, `--verbose`) using `argparse` and orchestrates the execution flow.
- **`Samples/`**: Houses test logs for validating the pipeline against valid, large, and corrupted access logs.
- **`Output/`**: Default destination directory for processed, masked, and classified log files.
- **`contributions/`**: Contains individual member contribution markdown files named according to the template `<STUDENT_NAME>_<STUDENT_ID>_<GITHUB_USERNAME>.md`.

### Usage (CLI Arguments)
The program can be executed via the command line with the following arguments:

```bash
# Basic run
python3 main.py --source Samples/sample.log

# Run with custom output directory and verbose summary
python3 main.py --source Samples/apache_logs.log --output Output --verbose
```

- `--source` (Required): Path to the Apache/Nginx access log file.
- `--output` (Optional): Directory where output files will be saved (Default: `Output`).
- `--verbose` (Optional): Displays a statistical summary in the terminal after processing.

### Output Files
When execution finishes, the following files are saved in the output directory with numbered lines:
- `01_Info.txt`: Logs with HTTP 2xx and 3xx status codes (Success / Redirection).
- `02_Warning.txt`: Logs with HTTP 4xx status codes (Client errors).
- `03_ERROR.txt`: Logs with HTTP 5xx status codes (Server errors).
- `04_Critical.txt`: Critical logs (empty, as critical level is not directly inferred from HTTP status codes).
- `05_ALL_LOGS_WITH_MASKED_IP.txt`: All cleaned log entries with masked IPv4 addresses (`[MASKED_IP]`).

The project uses Python functions, loops, conditions, string operations, file handling, and argparse, based on the topics covered in class.