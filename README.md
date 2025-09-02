<div align="center">

```
██╗    ██╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██║ █╗ ██║█████╗  ██████╔╝███████╗██║     ███████║██╔██╗ ██║
██║███╗██║██╔══╝  ██╔══██╗╚════██║██║     ██╔══██║██║╚██╗██║
╚███╔███╔╝███████╗██║█ ██║███████║╚██████╗██║  ██║██║ ╚████║
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
```
### WebDiscover by Faizan Ahmad Khichi (FAK) v2.0
**A user-friendly Python tool for discovering web pages and directories.**

</div>

WebDiscover is a powerful yet easy-to-use tool for web content discovery. It helps security researchers, developers, and enthusiasts find hidden pages, directories, and endpoints on a web server using a provided wordlist. It features both a simple interactive mode for beginners and a robust command-line mode for advanced users.

---

## ✨ Features

-   **Dual Mode Operation**:
    -   **Interactive Mode**: A guided, step-by-step process perfect for new users.
    -   **Command-Line Mode**: Full control with flags and arguments for automation and advanced scanning.
-   **Recursive Scanning**: Discovered directories can be recursively scanned to find deeper content.
-   **Colored Output**: Status codes are color-coded for quick and easy analysis (200 OK, 403 Forbidden, 3xx Redirects).
-   **Customizable Delay**: Adjust the delay between requests to be gentle on servers or to speed up scans.
-   **Session Management**: Uses `requests.Session()` for efficient connection pooling.
-   **Comprehensive Wordlist**: Comes with a large, well-organized wordlist covering common files, directories, and CMS-specific paths.

## ⚙️ Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Faizan-khichi/webscan.git
    cd webscan
    ```

2.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## 🚀 Usage Manual

You can use this tool in two ways: Simple Mode or Advanced Mode.

### Method 1: Simple Mode (Interactive)
This is the easiest way to get started. Just run the script without any arguments.

```sh
python web_scanner.py
```
The tool will guide you through the setup. **You can stop the scan at any time by pressing `Ctrl + C`.**

### Method 2: Advanced Mode (Command-Line)
For more control, use command-line arguments.

**A basic scan:**
```sh
python web_scanner.py https://example.com
```

**A deep, recursive scan with a low delay:**
```sh
python web_scanner.py https://example.com -d 0.1 -r 1 -o scan_results.txt
```

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security assessments only. The author is not responsible for any misuse or damage caused by this program. Always obtain permission from the website owner before scanning.
