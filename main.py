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