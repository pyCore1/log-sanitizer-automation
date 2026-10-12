# Contribution Report: Muhammed Mustafa Adsan

- **Full Name:** Muhammed Mustafa Adsan
- **Student ID:** 2409011010
- **GitHub Username:** SyraxLL

---

## 1. Role and Responsibility in the Project
- **Module 3 (HTTP Status Code Parsing and Classification - `classify_and_filter_logs`):**
  - Responsible for parsing HTTP request lines and status codes from masked log records, validating code formatting, and categorizing log entries by severity level.

## 2. Technical Contributions and Code Details
- **Log Format Tokenization:**
  - Split each log line by double quotes (`"`) using `line.split('"')` to isolate the quoted HTTP request string.
  - Extracted the HTTP status code immediately following the quoted request string (`parts[2].split()[0]`).
  - Implemented safe checks for lines with fewer than 3 quote-separated parts or missing detail fields, incrementing `unknown_count` and skipping malformed lines without throwing runtime index errors.
- **HTTP Status Code Validation and Grouping:**
  - Validated that the status code is exactly 3 characters long and strictly numeric (`status.isdigit() and len(status) == 3`).
  - **INFO (2xx / 3xx):** Grouped successful responses and redirection codes into `info_list`.
  - **WARNING (4xx):** Grouped client error codes (e.g., 400 Bad Request, 404 Not Found) into `warn_list`.
  - **ERROR (5xx):** Grouped server error codes (e.g., 500 Internal Server Error, 502 Bad Gateway) into `error_list`.
  - Accounted for any non-standard or out-of-range status codes by routing them to `unknown_count`.
  - Initialized an empty `crit_list` to satisfy the interface contract (since standard HTTP status codes do not designate a separate critical level).

## 3. Testing and Verification
- Tested with diverse log lines containing various HTTP codes (`200 OK`, `301 Moved Permanently`, `404 Not Found`, `500 Server Error`).
- Verified edge cases and malformed lines from `Samples/broken_test.log` to ensure no uncaught exceptions occurred and invalid records were correctly accounted for in `unknown_count`.
