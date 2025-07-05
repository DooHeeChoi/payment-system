from datetime import datetime

def log(message, save_to_file=False):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{now}] {message}"
    print(formatted)

    if save_to_file:
        with open("app.log", "a") as f:
            f.write(formatted + "\n")
