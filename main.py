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