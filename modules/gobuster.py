import subprocess

def run_gobuster(target, wordlist, options=""):

    command = f"gobuster dir -u {target} -w {wordlist} {options}"
    print(f"[+] Running command: {command}\n")

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    try:
        for line in process.stdout:
            print(line.strip()) 
    except KeyboardInterrupt:
        process.kill()
        print("\n[!] Gobuster process terminated by user.")
    finally:
        process.stdout.close()
        process.stderr.close()