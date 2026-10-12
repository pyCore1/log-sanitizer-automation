# Contribution Report: Ali Emre Erginler

- **Full Name:** Ali Emre Erginler
- **Student ID:** 2409111007
- **GitHub Username:** AiEmreer

---

## 1. Role and Responsibility in the Project
- **Module 5 (CLI Integration and Pipeline Orchestration - `main`):**
  - Responsible for designing the command-line interface arguments using `argparse`, orchestrating the execution pipeline across all modules, and printing summary statistics.

## 2. Technical Contributions and Code Details
- **CLI Design with argparse:**
  - Configured `argparse.ArgumentParser` with descriptive flags:
    - `--source`: Required flag specifying the input log file path.
    - `--output`: Optional flag setting the destination directory (defaulting to `"Output"`).
    - `--verbose`: Optional flag (`action="store_true"`) to print diagnostic summaries upon completion.
- **Workflow Orchestration and Error Resilience:**
  - Evaluated the output from Module 1 (`if raw_lines is None: return`) to prevent execution on missing or corrupted input files.
  - Handled automated output directory creation using `os.makedirs(args.output, exist_ok=True)` and caught potential `OSError` exceptions.
  - Linked the end-to-end pipeline: reading -> masking -> classification -> file writing.
  - Exported all required output files (`01_Info.txt`, `02_Warning.txt`, `03_ERROR.txt`, `04_Critical.txt`, and `05_ALL_LOGS_WITH_MASKED_IP.txt`).
- **Verbose Output Reporting:**
  - Printed high-level summary metrics when `--verbose` is supplied, displaying counts for processed lines, INFO (2xx/3xx), WARNING (4xx), ERROR (5xx), unrecognized lines, and clarifying the critical severity scope.

## 3. Testing and Verification
- Executed the CLI with varying flags (default options, custom output directory, and `--verbose` mode) to verify proper parsing and argument validation.
