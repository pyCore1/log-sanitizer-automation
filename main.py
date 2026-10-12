import os
import argparse

# Module 1 - Berivan
# Reading log files and handling file errors

def read_log_file(file_name):
    try:
        with open(file_name, "r", encoding="latin-1") as f:
            lines = f.readlines()

        print("Log file read successfully.")
        return lines

    except (FileNotFoundError, PermissionError, UnicodeError) as err:
        print(f"Cannot read log file or files : {err}")
        return None
    
# Module 2 - Melda
# IPv4 Address Masking

def mask_log_line(line):
    words = line.split()
    if not words:
        return ""

    ip = words[0]
    parts = ip.split(".")

    # check if valid ipv4
    if len(parts) == 4:
        valid = True
        for p in parts:
            if not p.isdigit():
                valid = False
            elif len(p) > 3 or int(p) > 255:
                valid = False
            elif len(p) > 1 and p[0] == "0":
                valid = False

        if valid:
            words[0] = "[MASKED_IP]"

    return " ".join(words) + "\n"

# Module 3 - Mustafa
# Extracting HTTP status codes and classifying logs

def classify_and_filter_logs(lines):
    info_list = []
    warn_list = []
    error_list = []
    crit_list = []
    unknown_count = 0

    for line in lines:
        parts = line.split('"')
        if len(parts) < 3:
            unknown_count += 1
            continue

        details = parts[2].split()
        if not details:
            unknown_count += 1
            continue

        status = details[0]
        # check status code
        if not status.isdigit() or len(status) != 3:
            unknown_count += 1
        # group by http code
        elif status.startswith("2") or status.startswith("3"):
            info_list.append(line.strip())
        elif status.startswith("4"):
            warn_list.append(line.strip())
        elif status.startswith("5"):
            error_list.append(line.strip())
        else:
            unknown_count += 1

    return info_list, warn_list, error_list, crit_list, unknown_count
# Module 4 - Beyza
# Saving cleaned and classified logs to files

def save_logs_to_file(output_dir, file_name, logs):
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        count = 1
        for line in logs:
            f.write(f"{count}. {line.strip()}\n")
            count += 1

    print(f"Saved: {file_name} ({len(logs)} logs)")
    
# Module 5 - Emre
# Main CLI function

def main():
    parser = argparse.ArgumentParser(description="Clean and classify Apache access logs")
    parser.add_argument("--source", required=True, help="Path to Apache access log")
    parser.add_argument("--output", default="Output", help="Output folder")
    parser.add_argument("--verbose", action="store_true", help="Show summary")
    args = parser.parse_args()

    raw_lines = read_log_file(args.source)
    if raw_lines is None:
        return

    # clean lines
    cleaned = []
    for line in raw_lines:
        if line.strip():
            cleaned.append(mask_log_line(line))

    info_logs, warn_logs, error_logs, crit_logs, unknown = classify_and_filter_logs(cleaned)

    try:
        os.makedirs(args.output, exist_ok=True)
        # save files
        save_logs_to_file(args.output, "01_Info.txt", info_logs)
        save_logs_to_file(args.output, "02_Warning.txt", warn_logs)
        save_logs_to_file(args.output, "03_ERROR.txt", error_logs)
        save_logs_to_file(args.output, "04_Critical.txt", crit_logs)
        save_logs_to_file(args.output, "05_ALL_LOGS_WITH_MASKED_IP.txt", cleaned)
    except OSError as err:
        print(f"Cannot save output: {err}")
        return

    # print details if verbose
    if args.verbose:
        print(f"Processed: {len(cleaned)} lines")
        print(f"INFO (HTTP 2xx/3xx): {len(info_logs)}")
        print(f"WARNING (HTTP 4xx): {len(warn_logs)}")
        print(f"ERROR (HTTP 5xx): {len(error_logs)}")
        print(f"Other/unrecognized: {unknown}")
        print("CRITICAL is not inferred from Apache HTTP status codes.")

if __name__ == "__main__":
    main()