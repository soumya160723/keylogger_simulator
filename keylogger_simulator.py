import time

def simulate_keylogger():
    print("Starting simulated keylogger...")
    for i in range(3):
        fake_input = f"User typed fake input {i+1}"
        with open("simulated_logs.txt", "a") as f:
            f.write(f"{time.ctime()}: {fake_input}\n")
        print(f"[+] Logged: {fake_input}")
        time.sleep(1)
    print("Simulation complete. Logs saved in 'simulated_logs.txt'.")

if __name__ == "__main__":
    simulate_keylogger()
