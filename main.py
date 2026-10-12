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