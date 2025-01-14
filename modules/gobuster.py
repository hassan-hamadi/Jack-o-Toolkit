import subprocess

def run_gobuster(target, wordlist, options=""):

    command = f"gobuster dir -u {target} -w {wordlist} {options}"
    print(f"[+] Running command: {command}\n")

    # Use subprocess.Popen to stream output
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    try:
        for line in process.stdout:
            print(line.strip())  # Print each line as it’s produced
    except KeyboardInterrupt:
        process.kill()
        print("\n[!] Gobuster process terminated by user.")
    finally:
        process.stdout.close()
        process.stderr.close()