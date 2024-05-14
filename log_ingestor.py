import datetime
import random
import json

def write_log_to_file(log_data, file_name):
    log_json = json.dumps(log_data) + "\n"
    with open(file_name, "a") as log_file:
        log_file.write(log_json)

def generate_log_data():
    levels = ["info", "error", "success"]
    log_string = "Inside the Search API"
    timestamp = datetime.datetime.now().isoformat() + "Z"
    source = f"log{random.randint(1, 9)}.log"
    level = random.choice(levels)

    log_data = {
        "level": level,
        "log_string": log_string,
        "timestamp": timestamp,
        "metadata": {
            "source": source
        }
    }

    write_log_to_file(log_data, source)
    return log_data

for _ in range(10):
    log_data = generate_log_data()
    print(log_data)