import os
import json

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

def search_logs(filter_key, filter_value):
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
                    if value == filter_value:
                        logs.append(entry)
                else:
                    if entry.get(filter_key) == filter_value:
                        logs.append(entry)
    return logs

def main():
    filter_key = input("Enter the key to filter logs (level, log_string, timestamp, metadata.source): ")
    filter_value = input(f"Enter the value for {filter_key}: ")
    logs = search_logs(filter_key, filter_value)
    for log in logs:
        print(log)

if __name__ == "__main__":
    main()