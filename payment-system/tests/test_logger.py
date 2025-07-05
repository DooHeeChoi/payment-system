from app.logger import log

def test_log():
    log("test message", save_to_file=True)
