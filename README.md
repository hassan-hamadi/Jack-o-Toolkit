# Jack O' Toolkit

## Overview
Jack O' Toolkit is a penetration testing toolkit designed to streamline various security assessment tasks. Currently, the toolkit integrates popular tools like Gobuster and SQLMap for directory brute-forcing and SQL injection testing, respectively.

However, this toolkit is a **work in progress**, and future iterations will include **custom-built tools** to replace external dependencies like Gobuster and SQLMap. The goal is to provide a fully customized penetration testing toolkit.

## Current Features
1. **Gobuster Integration**
   - Tool: [Gobuster](https://github.com/OJ/gobuster)
   - Purpose: Directory brute-forcing to discover hidden files and directories.
   - Usage: Users can specify a target URL and wordlist to run Gobuster from within the framework.

## How to Use
1. **Setting Up the Toolkit**
   - Clone the repository:
   ```bash
   git clone https://github.com/hassan-hamadi/Jack-o-Toolkit.git
   cd Jack-o-Toolkit
   ```
   - Set up a virtual environment (recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     OR
     source .venv/Scripts/activate
     ```
   - Install required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Toolkit**
   - Launch the toolkit by running the main script:
     ```bash
     python main.py
     ```
   - Follow the menu prompts to select and run tools like Gobuster or SQLMap.

## Author
Hassan Hamadi