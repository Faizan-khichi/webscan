<div align="center">

```
██╗    ██╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝█████╗  ██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══╝  ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██║  ██║███████╗╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
```
### WebDiscover by Faizan Ahmad Khichi (FAK) v2.0
**A user-friendly Python tool for discovering web pages and directories.**
</div>

---

WebDiscover is a powerful yet easy-to-use tool for web content discovery. It helps security researchers, developers, and enthusiasts find hidden pages, directories, and endpoints on a web server using a provided wordlist. It features both a simple interactive mode for beginners and a robust command-line mode for advanced users.

## ✨ Features

-   **Dual Mode Operation**:
    -   **Interactive Mode**: A guided, step-by-step process perfect for new users.
    -   **Command-Line Mode**: Full control with flags and arguments for automation and advanced scanning.
-   **Recursive Scanning**: Discovered directories can be recursively scanned to find deeper content.
-   **Colored Output**: Status codes are color-coded for quick and easy analysis (200 OK, 403 Forbidden, 3xx Redirects).
-   **Customizable Delay**: Adjust the delay between requests to be gentle on servers or to speed up scans.
-   **Comprehensive Wordlist**: Comes with a large, well-organized wordlist covering common files, directories, and CMS-specific paths.
-   **Session Management**: Uses `requests.Session()` for efficient connection pooling.

## ⚙️ Installation

WebDiscover is easy to set up. You just need Python 3.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/WebDiscover.git
    cd WebDiscover
    ```

2.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

That's it! You're ready to start scanning.

## 🚀 Usage Manual

You can use WebDiscover in two ways: Simple Mode or Advanced Mode.

### Method 1: Simple Mode (Interactive)

This is the easiest way to get started. Just run the script without any arguments.

```sh
python web_scanner.py
```

The tool will launch in interactive mode and guide you through the process:
1.  It will display a quick user manual.
2.  It will ask you for the target URL.
3.  You can choose a pre-configured scan type (`Quick`, `Deep`) or a `Custom` scan where you define all settings.
4.  The scan will start!

**You can stop the scan at any time by pressing `Ctrl + C`.**

### Method 2: Advanced Mode (Command-Line)

For more control and for use in scripts, you can use command-line arguments.

**Basic Syntax:**
```sh
python web_scanner.py <URL> [OPTIONS]
```

**Commands & Options:**

| Argument         | Short | Description                                                              | Example                               |
| ---------------- | ----- | ------------------------------------------------------------------------ | ------------------------------------- |
| `url`            |       | **(Required)** The target URL to scan.                                   | `https://example.com`                 |
| `--wordlist`     | `-w`  | Path to the wordlist file. (Default: `wordlist.txt`)                     | `-w /path/to/my_list.txt`             |
| `--delay`        | `-d`  | Delay in seconds between requests. (Default: `0.2`)                      | `-d 0.1`                              |
| `--output`       | `-o`  | File to save the found pages. (Default: `found_pages.txt`)               | `-o results.txt`                      |
| `--recursive`    | `-r`  | Enable recursive scanning up to a certain depth. (Default: `0`=disabled) | `-r 1`                                |
| `--help`         | `-h`  | Show the help message and exit.                                          |                                       |

**Examples:**

-   **A basic scan on a target:**
    ```sh
    python web_scanner.py https://example.com
    ```
-   **A deep, recursive scan with a low delay and custom output file:**
    ```sh
    python web_scanner.py https://example.com -d 0.1 -r 1 -o scan_results.txt
    ```
-   **Using a different wordlist:**
    ```sh
    python web_scanner.py https://example.com -w /usr/share/wordlists/dirb/common.txt
    ```

## ⚠️ Disclaimer

This tool is intended for educational purposes and for use in authorized security assessments only. Unauthorized scanning of websites is illegal. The author is not responsible for any misuse or damage caused by this program. Always obtain permission from the website owner before scanning.

## 📂 File Structure

```
WebDiscover/
├── web_scanner.py      # The main Python scanner script
├── wordlist.txt        # The default comprehensive wordlist
├── requirements.txt    # List of Python dependencies
└── README.md           # This file
```