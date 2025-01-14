from modules.gobuster import run_gobuster
from modules.sqlmap import run_sqlmap

def gobuster_call():
    print("Gobuster Initiated")
    target = input("Enter the target URL: ")
    wordlist = input("Enter location of wordlist: ")
    options = input("Enter additional options (blank=default): ")
    run_gobuster(target, wordlist, options)

def sqlmap_call():
    print("Sqlmap Initiated")
    target = input("Enter the target URL: ")
    options = input("Enter additional options (blank=default): ")

    output = run_sqlmap(target, options)
    print("\n[+] SQLMap Output:")
    print(output)

def print_header():
    header = r"""
      🎃  Jack O' Toolkit 🎃
       _____________________
      /                     \
     |   ~~~~  ~~~~  ~~~~   |
     |   ( O )  ( O )        |
     |        >              |
     |   \  ---   /          |
      \_____________________/
    """
    print("\033[1;33m" + header + "\033[0m") 
print_header()
print("-------------------------------------------------------------------")

def print_options():
    options = """
    a) Gobuster
    b) Sqlmap
    """
    print(options)
print_options()

while True:
    option = input("What tool would you like to use?\n")
    if (option == 'a'):
        gobuster_call()
    if (option == 'b'):
        sqlmap_call()
    else:
        print("ERROR: Invalid input.")

