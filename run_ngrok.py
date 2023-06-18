import subprocess
from config import port_number


def run_ngrok():
    try:
        subprocess.check_output(['./ngrok', 'http', str(port_number)])
        print("ngrok run")

    except Exception:
        subprocess.check_output(['killall', 'ngrok'])


if __name__ == "__main__":
    run_ngrok()