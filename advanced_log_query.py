import os
import json
import re
import datetime
from itertools import product

def read_log_data(file_path):
    logs = []
    with open(file_path, "r") as log_file:
        for line in log_file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Skip empty lines
                try:
                    log_entry = json.loads(line)
                    logs.append(log_entry)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
    return logs

def search_logs(filter_key, filter_value, start_date=None, end_date=None, use_regex=False):
    logs = []
    for file_name in os.listdir("."):
        if file_name.endswith(".log"):
            file_path = os.path.join(".", file_name)
            log_data = read_log_data(file_path)
            for entry in log_data:
                if "." in filter_key:
                    # Handle nested keys
                    keys = filter_key.split(".")
                    value = entry
                    for key in keys:
                        value = value.get(key, {})
                    if use_regex:
                        if re.search(filter_value, str(value)):
                            if start_date and end_date:
                                log_timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                                if start_date <= log_timestamp.replace(tzinfo=None) <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
                    else:
                        if str(value) == str(filter_value):
                            if start_date and end_date:
                                log_timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                                if start_date <= log_timestamp.replace(tzinfo=None) <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
                else:
                    if use_regex:
                        if re.search(filter_value, str(entry.get(filter_key, ""))):
                            if start_date and end_date:
                                log_timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                                if start_date <= log_timestamp.replace(tzinfo=None) <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
                    else:
                        if str(entry.get(filter_key)) == str(filter_value):
                            if start_date and end_date:
                                log_timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                                if start_date <= log_timestamp.replace(tzinfo=None) <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
    return logs

def search_logs_by_date_range(start_date, end_date):
    logs = []
    for file_name in os.listdir("."):
        if file_name.endswith(".log"):
            file_path = os.path.join(".", file_name)
            log_data = read_log_data(file_path)
            for entry in log_data:
                timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                if start_date <= timestamp.replace(tzinfo=None) <= end_date:
                    logs.append(entry)
    return logs

def search_logs_by_regex(regex_pattern):
    logs = []
    regex = re.compile(regex_pattern)
    for file_name in os.listdir("."):
        if file_name.endswith(".log"):
            file_path = os.path.join(".", file_name)
            log_data = read_log_data(file_path)
            for entry in log_data:
                if regex.search(json.dumps(entry)):
                    logs.append(entry)
    return logs

def search_logs_by_multiple_filters(filters):
    logs = []
    for file_name in os.listdir("."):
        if file_name.endswith(".log"):
            file_path = os.path.join(".", file_name)
            log_data = read_log_data(file_path)
            for entry in log_data:
                match = True
                for filter_key, filter_value in filters.items():
                    if "." in filter_key:
                        keys = filter_key.split(".")
                        value = entry
                        for key in keys:
                            value = value.get(key, {})
                        if value != filter_value:
                            match = False
                            break
                    else:
                        if entry.get(filter_key) != filter_value:
                            match = False
                            break
                if match:
                    logs.append(entry)
    return logs

def main():
    filter_keys = []
    filter_values = []
    use_regex = False

    while True:
        filter_key = input("Enter the key to filter logs (level, log_string, timestamp, metadata.source), or 'q' to quit: ")
        if filter_key.lower() == 'q':
            break

        filter_value = input(f"Enter the value for {filter_key}: ")
        filter_keys.append(filter_key)
        filter_values.append(filter_value)

        regex_choice = input("Do you want to use regular expressions for this filter? (y/n) ").lower()
        if regex_choice == 'y':
            use_regex = True

    date_range = input("Do you want to filter by date range? (y/n) ")
    start_date = None
    end_date = None
    if date_range.lower() == "y":
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")
        start_date = datetime.datetime.fromisoformat(start_date_str)
        end_date = datetime.datetime.fromisoformat(end_date_str)

    filter_combinations = product(filter_keys, filter_values)
    combined_logs = []
    for key, value in filter_combinations:
        logs = search_logs(key, value, start_date, end_date, use_regex)
        combined_logs.extend(logs)

    # Add the code to remove duplicates and convert back to dictionaries here

    for log in combined_logs:
        print(log)

if __name__ == "__main__":
    main()