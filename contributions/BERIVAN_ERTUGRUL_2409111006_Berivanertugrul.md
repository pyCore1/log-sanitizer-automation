# Contribution Report: Berivan Ertuğrul

- **Full Name:** Berivan Ertuğrul
- **Student ID:** 2409111006
- **GitHub Username:** Berivanertugrul

---

## 1. Role and Responsibility in the Project
- **Module 1 (File Reading and Error Handling - `read_log_file`):**
  - Responsible for loading the input access log file from disk into memory with proper encoding and handling system-level file exceptions safely.

## 2. Technical Contributions and Code Details
- **Robust File Reading:**
  - Implemented file opening to read log entries line by line into memory using `readlines()`.
  - Provided descriptive feedback on standard output (`"Log file read successfully."`) upon successful file retrieval.
- **Robust Exception Handling:**
  - `FileNotFoundError`: Gracefully intercepted cases where the specified log file does not exist, printing an informative diagnostic message rather than crashing the program.
  - `PermissionError`: Handled operating system permission issues when file access rights are restricted.
  - `UnicodeError`: Handled encoding incompatibilities to prevent unexpected termination during reading.
- **Controlled Return Value:**
  - Returned `None` upon encountering any file reading failure and returned the list of raw string lines upon success, enabling safe downstream error management in the main pipeline.

## 3. Testing and Verification
- Tested with standard access logs (`Samples/apache_logs.log`), non-existent file paths, and unreadable files to ensure exception messages trigger appropriately.
