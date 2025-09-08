<div align="center">
  ██╗    ██╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
  ██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
  ██║ █╗ ██║█████╗  ██████╔╝███████╗██║     ███████║██╔██╗ ██║
  ██║███╗██║██╔══╝  ██╔══██╗╚════██║██║     ██╔══██║██║╚██╗██║
  ╚███╔███╔╝███████╗██████║███████║╚██████╗██║  ██║██║ ╚████║
   ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

  **WebDiscover by Faizan Ahmad Khichi (FAK) v2.0**

  A user-friendly tool for discovering web pages and directories.

</div>

WebDiscover is a powerful yet easy-to-use tool for web content discovery. It helps security researchers, developers, and enthusiasts find hidden pages, directories, and endpoints on a web server using a provided wordlist. It features both a simple interactive mode for beginners and a robust command-line mode for advanced users.

---

### ✨ Features

- **Dual Mode Operation**:
  - **Interactive Mode**: A guided, step-by-step process perfect for new users.
  - **Command-Line Mode**: Full control with flags and arguments for automation and advanced scanning.
- **Recursive Scanning**: Discovered directories can be recursively scanned to find deeper content.
- **Colored Output**: Status codes are color-coded for quick and easy analysis (200 OK, 3xx Redirects, 403 Forbidden).
- **Customizable Delay**: Adjust the delay between requests to be gentle on servers or to speed up scans.
- **Session Management**: Uses `requests.Session()` for efficient connection pooling and performance.
- **Graceful Exit**: Handles `Ctrl+C` cleanly to stop scans without messy errors.
- **Comprehensive Wordlist Support**: Easily use any wordlist for your scans.

---

### ⚙️ Installation

#### Method 1: Quick & Permanent Setup (Linux/macOS)

This single command clones the repository, installs dependencies, and creates a permanent `webscan` command so you can run the tool from anywhere.

```bash
git clone https://github.com/Faizan-khichi/webscan.git ~/webscan && pip install -r ~/webscan/requirements.txt && echo "alias webscan='python ~/webscan/web_scanner.py'" >> ~/.bashrc && source ~/.bashrc
```
After running this, you can start the tool simply by typing `webscan` in your terminal.

#### Method 2: Manual Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Faizan-khichi/webscan.git
    cd webscan
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

### 🚀 Usage Manual

You can use this tool in two ways: Simple Mode or Advanced Mode.

#### Method 1: Simple Mode (Interactive)

This is the easiest way to get started. Just run the script without any arguments. If you used the permanent setup, type:

```bash
webscan
```
Otherwise, run:
```bash
python web_scanner.py
```
The tool will guide you through the setup, asking for the URL, wordlist, and other options. You can stop the scan at any time by pressing `Ctrl + C`.

#### Method 2: Advanced Mode (Command-Line)

For more control, use command-line arguments.

**Command Syntax:**
`webscan <URL> [options]`

**Options:**
- `-w`, `--wordlist`: Path to the wordlist file (default: `wordlist.txt`).
- `-d`, `--delay`: Delay between requests in seconds (default: `0`).
- `-r`, `--recursive`: Maximum recursion depth (default: `0` - no recursion).
- `-o`, `--output`: Save results to an output file.

**Examples:**

- **A basic scan on a target:**
  ```bash
  webscan https://example.com
  ```

- **A scan using a specific wordlist:**
  ```bash
  webscan https://example.com -w /usr/share/wordlists/dirb/common.txt
  ```

- **A deep, recursive scan with a low delay, saving results:**
  ```bash
  webscan https://example.com -d 0.1 -r 2 -o scan_results.txt
  ```

---

### ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security assessments only. The author is not responsible for any misuse or damage caused by this program. Always obtain permission from the website owner before scanning.
