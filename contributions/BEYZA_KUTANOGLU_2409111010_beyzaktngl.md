# Contribution Report: Beyza Kutanoğlu

- **Full Name:** Beyza Kutanoğlu
- **Student ID:** 2409111010
- **GitHub Username:** beyzaktngl

---

## 1. Role and Responsibility in the Project
- **Module 4 (Exporting Cleaned and Classified Logs - `save_logs_to_file`):**
  - Responsible for formatting and saving classified, masked log lines into designated output text files with sequential line numbers.

## 2. Technical Contributions and Code Details
- **Cross-Platform Path Construction:**
  - Used `os.path.join(output_dir, file_name)` to generate valid path strings across both macOS and Windows operating systems.
- **Sequential Line Indexing:**
  - Implemented 1-based indexing for saved log lines formatted as `{count}. {line.strip()}\n` to provide readable and structured output files.
- **Encoding and Resource Management:**
  - Ensured all outputs are written in UTF-8 (`encoding="utf-8"`) to maintain Unicode safety across all target environments.
  - Used safe context managers (`with open(...)`) to ensure files are closed reliably even if an error occurs.
- **Console Feedback:**
  - Printed clear status lines showing the created file name and total record count (`print(f"Saved: {file_name} ({len(logs)} logs)")`).

## 3. Testing and Verification
- Tested writing both empty log lists and large files containing thousands of entries, verifying sequential indexing and file integrity.
