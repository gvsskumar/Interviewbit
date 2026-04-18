# Create a closure-based logger that stores logs internally.
def create_logger():
    logs = []  # enclosed state

    def log(message):
        logs.append(message)

    def get_logs():
        return logs

    return log, get_logs


# Usage
log, get_logs = create_logger()

log("Start process")
log("Processing data")
log("End process")

print(get_logs())