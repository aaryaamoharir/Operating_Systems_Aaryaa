import sys
import datetime


def log_message(log_file, message):
    # gets the time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # splits the message into header and the rest
    parts = message.split(' ', 1)
    action = parts[0]
    msg = parts[1] if len(parts) > 1 else ""

    # correct formatting
    log_entry = f"### {timestamp} - [{action}]\n\n{msg}\n\n---\n"

    # allows me to add information to the file multiple times
    with open(log_file, 'a') as file:
        file.write(log_entry)


def main():
    # takes in the name of the file as an argument
    if len(sys.argv) != 2:
        print("Usage: python logger.py <log_file_name>")
        sys.exit(1)

    log_file = sys.argv[1]

    # creates the file if it doesn't exist
    try:
        with open(log_file, 'x') as file:
            file.write("# Devlog\n\nThis is a developer log.\n\n---\n")
    except FileExistsError:
        pass

    print("Logger started. Type 'QUIT' to stop.")

    while True:
        message = input("Enter log message: ")

        #stops the program when someone tells it to QUIT
        if message == "QUIT":
            print("Logger stopped.")
            break

        log_message(log_file, message)


if __name__ == "__main__":
    main()
