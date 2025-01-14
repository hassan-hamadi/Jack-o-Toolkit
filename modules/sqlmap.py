import subprocess

def run_sqlmap(target, options=""):

    try:
        command = f"sqlmap -u {target} {options} --batch"
        print(f"[+] Running: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[-] Error running SQLMap: {e}"