# query-log-control

## Objective
Build a problem solution that uses APIs with logs at different stages. These logs should be stored in some log files such as `log1.log`, `log2.log` etc files. You need to build a Query Interface also that traverses through these logs files and fetches logs based on timestamp, log string, source of the log, etc.

Both the systems (the log stores and the query interface) can be built using any programming language of your choice.

## Query Interface:
The logs might have the below format.
- Offer a user interface (Web UI or CLI) for full-text search across logs.
- Include filters based on:
    - level
    - log_string
    - timestamp
    - metadata.source
- Aim for efficient and quick search results.

## Advanced Features (Bonus):

These features aren’t compulsory to implement, however, adding them might increase the chances of your submission being accepted.

- Implement search within specific date ranges.
- Utilize regular expressions for search.
- Allow combining multiple filters.
- Provide real-time log ingestion and searching capabilities.
- Implement role-based access to the query interface.

## Approach
### Step 1: Set up a Python project

- Create a new directory for your project.
- Open a text editor or an integrated development environment (IDE) of your choice.

### Step 2: Create a file for the log ingestor

- Create a new Python file, e.g., log_ingestor.py.
- We'll start by creating a simple function to generate sample log data.

```
import datetime
import random

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

    return log_data
```

This function generates a dictionary representing a log entry with a random log level, a timestamp, and a random source file name.

### Step 3: Write logs to files

- In the log_ingestor.py file, import the json module to convert the log data dictionary to a JSON string.

```
import json
```
- Create a function to write the log data to a file.

```
def write_log_to_file(log_data, file_name):
    log_json = json.dumps(log_data) + "\n"
    with open(file_name, "a") as log_file:
        log_file.write(log_json)
```
This function takes two arguments: log_data (a dictionary) and file_name (the name of the log file). It converts the log data dictionary to a JSON string and appends it to the specified file.

- Modify the generate_log_data function to call the write_log_to_file function with the generated log data and a file name.

```
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

```
- Add a simple loop to generate and write multiple log entries.
```
for _ in range(10):
    log_data = generate_log_data()
    print(log_data)
```
After executing this You should see 10 log data dictionaries printed to the console, and the corresponding log files (e.g., log1.log, log2.log, etc.) should be created in the same directory with the log entries written to them.
At this point, you should have a basic log ingestor that generates and writes log data to files.

### Step 4: Integrate APIs
In this step, we'll integrate some APIs to generate logs at different stages of the application. Since you don't have any prior knowledge of APIs, we'll simulate them using Python functions.

- Create a new Python file called api_simulator.py.
- Define a simple function representing an API that generates a log.

```
import random
from log_ingestor import generate_log_data, write_log_to_file

def search_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Search API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Success", "Failed"])
```

This function generates log data using the generate_log_data function from the log_ingestor module, updates the log_string key, writes the log data to a file, and then simulates some processing by returning a random string.

- Define another function representing a different API.

```
def authentication_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Authentication API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Authenticated", "Failed"])
```
This function follows a similar pattern, but with a different log_string value.

- Repeat this process to create a few more API functions

```
def messaging_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Messaging API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Messaging", "Failed"])

def calander_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Calander API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Calander", "Failed"])

def weather_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Weather API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Weather", "Failed"])

def fileStorage_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the File Storage API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["File Storage", "Failed"])

def translation_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Translation API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Translation", "Failed"])

def analytics_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Analytics API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Analytics", "Failed"])

def socialMedia_api():
    log_data = generate_log_data()
    log_data["log_string"] = "Inside the Social Media API"
    write_log_to_file(log_data, log_data["metadata"]["source"])
    # Simulate some processing
    return random.choice(["Social Media", "Failed"])
```
- In the api_simulator.py file, add a main function that calls these API functions.

```
def main():
    search_result = search_api()
    print(f"Search API result: {search_result}")

    auth_result = authentication_api()
    print(f"Authentication API result: {auth_result}")

    messaging_result = messaging_api()
    print(f"Authentication API result: {messaging_result}")

    calander_result = calander_api()
    print(f"Authentication API result: {calander_result}")

    weather_result = weather_api()
    print(f"Authentication API result: {weather_result}")

    file_result = fileStorage_api()
    print(f"Authentication API result: {file_result}")

    translation_result = translation_api()
    print(f"Authentication API result: {translation_result}")

    analytics_result = analytics_api()
    print(f"Authentication API result: {analytics_result}")

    social_result = socialMedia_api()
    print(f"Authentication API result: {social_result}")

    # Call other API functions here

if __name__ == "__main__":
    main()
```

After Executing this you will see the log files being updated with new log entries from the simulated APIs, and the API results printed to the console.
By integrating these simulated APIs, you've completed the first part of the log ingestor requirements.

### Step 5: Create a query interface

- Create a new Python file called log_query.py.
- Import the necessary modules.
```
import os
import json
```
- Define a function to read log data from files.
```
def read_log_data(file_path):
    with open(file_path, "r") as log_file:
        log_data = log_file.readlines()
    return [json.loads(line) for line in log_data]
```
This function takes a file path as input, reads the contents of the file, and returns a list of dictionaries representing the log data.

- Define a function to search for logs based on a filter.

```
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
```
This function takes two arguments: filter_key (the key to search for) and filter_value (the value to match). It iterates through all the log files in the current directory, reads the log data, and appends the log entries that match the filter condition to a list. Finally, it returns the list of matching log entries.

- Add a simple command-line interface to accept user input for the filter.

```
def main():
    filter_key = input("Enter the key to filter logs (level, log_string, timestamp, metadata.source): ")
    filter_value = input(f"Enter the value for {filter_key}: ")
    logs = search_logs(filter_key, filter_value)
    for log in logs:
        print(log)

if __name__ == "__main__":
    main()
```

By this point we have completed query interface the next step is to develop advanced features

### Step 6: Create Advanced Query Interface

- Create a new Python file called advanced_log_query.py.
- Copy the contents of the log_query.py file into advanced_log_query.py. This will include the existing code for reading log data and searching logs based on a filter.
- In advanced_log_query.py, add the following imports at the top of the file:
```
import re
import datetime
from itertools import product
```

These imports are required for the bonus features: regular expressions (re), datetime operations (datetime), and combining multiple filters (itertools.product).

- Modify the search_logs function to accept an optional use_regex parameter and handle regular expressions
```
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
                                if start_date <= log_timestamp <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
                    else:
                        if value == filter_value:
                            if start_date and end_date:
                                log_timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                                if start_date <= log_timestamp <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
                else:
                    if use_regex:
                        if re.search(filter_value, str(entry.get(filter_key, ""))):
                            if start_date and end_date:
                                log_timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                                if start_date <= log_timestamp <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
                    else:
                        if entry.get(filter_key) == filter_value:
                            if start_date and end_date:
                                log_timestamp = datetime.datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                                if start_date <= log_timestamp <= end_date:
                                    logs.append(entry)
                            else:
                                logs.append(entry)
    return logs
```

This modified search_logs function now accepts an additional use_regex parameter. If use_regex is True, it uses the re.search function from the re module to perform regular expression matching instead of strict string equality.

- Update the main function to prompt the user for regular expression usage and combine multiple filters

```
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

    combined_logs = list(set(combined_logs))  # Remove duplicates
    for log in combined_logs:
        print(log)

if __name__ == "__main__":
    main()
```

This updated main function allows the user to enter multiple filter keys and values, and it prompts the user to choose whether to use regular expressions for each filter. The user is also prompted for a date range, just like before.
After collecting all the filters, the function uses itertools.product to generate all possible combinations of filter keys and values. It then calls the search_logs function for each combination, passing the use_regex flag based on the user's choice. The resulting log entries from all combinations are combined into a single list, with duplicates removed.
### 
At this point we are able to perform multiple filters, choose to use regular expressions for each filter, and filter by date range. The combined results from all filters will be printed to the console.

### Step 7: Improve the user interface (UI)
The current implementation uses a command-line interface (CLI) to interact with the query interface. While this works fine for simple use cases, we can enhance the user experience by creating a menu-based UI or a web-based UI. But for this project lets focus on CLI.

```
import os
import json
import re
import datetime
from itertools import product
from log_query import search_logs
from advanced_log_query import search_logs_by_date_range, search_logs_by_regex, search_logs_by_multiple_filters

def main():
    while True:
        print("\n===== Log Query Interface =====")
        print("1. Normal Search")
        print("2. Advanced Search")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Normal Search
            filter_key = input("Enter the key to filter logs (level, log_string, timestamp, metadata.source): ")
            filter_value = input(f"Enter the value for {filter_key}: ")
            logs = search_logs(filter_key, filter_value)
            print("\nSearch Results:")
            for log in logs:
                print(log)

        elif choice == "2":
            # Advanced Search
            print("\n===== Advanced Search =====")
            print("1. Search by Date Range")
            print("2. Search by Regular Expression")
            print("3. Search by Multiple Filters")
            print("4. Back to Main Menu")
            advanced_choice = input("Enter your choice (1-4): ")

            if advanced_choice == "1":
                # Search by Date Range
                start_date_str = input("Enter the start date (YYYY-MM-DD): ")
                end_date_str = input("Enter the end date (YYYY-MM-DD): ")
                start_date = datetime.datetime.fromisoformat(start_date_str)
                end_date = datetime.datetime.fromisoformat(end_date_str)
                logs = search_logs_by_date_range(start_date, end_date)
                print("\nSearch Results:")
                for log in logs:
                    print(log)

            elif advanced_choice == "2":
                # Search by Regular Expression
                regex_pattern = input("Enter the regular expression pattern: ")
                logs = search_logs_by_regex(regex_pattern)
                print("\nSearch Results:")
                for log in logs:
                    print(log)

            elif advanced_choice == "3":
                # Search by Multiple Filters
                filters = {}
                while True:
                    filter_key = input("Enter the key to filter logs (level, log_string, timestamp, metadata.source), or 'q' to quit: ")
                    if filter_key.lower() == 'q':
                        break
                    filter_value = input(f"Enter the value for {filter_key}: ")
                    filters[filter_key] = filter_value
                logs = search_logs_by_multiple_filters(filters)
                print("\nSearch Results:")
                for log in logs:
                    print(log)

            elif advanced_choice == "4":
                # Back to Main Menu
                continue

        elif choice == "3":
            # Exit
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

- The main function displays a main menu with options for "Normal Search," "Advanced Search," and "Exit."
- If the user chooses "Normal Search" (option 1), it prompts for a filter key and value, and calls the search_logs function from the log_query.py file to perform the search. The search results are then printed.
- If the user chooses "Advanced Search" (option 2), a submenu is displayed with options for "Search by Date Range," "Search by Regular Expression," "Search by Multiple Filters," and "Back to Main Menu."
  - If the user chooses "Search by Date Range" (option 1), it prompts for a start and end date, and calls the search_logs_by_date_range function from the advanced_log_query.py file to perform the search. The search results are then printed.
  - If the user chooses "Search by Regular Expression" (option 2), it prompts for a regular expression pattern, and calls the search_logs_by_regex function from the advanced_log_query.py file to perform the search. The search results are then printed.
  - If the user chooses "Search by Multiple Filters" (option 3), it prompts for filter keys and values until the user enters 'q' to quit. It then calls the search_logs_by_multiple_filters function from the advanced_log_query.py file to perform the search. The search results are then printed.
  - If the user chooses "Back to Main Menu" (option 4), it returns to the main menu.
- If the user chooses "Exit" (option 3) from the main menu, the program terminates.

With this implementation, the user can choose between normal search and advanced search options, and the appropriate functions from the respective modules (log_query.py and advanced_log_query.py) are called based on the user's choice.

