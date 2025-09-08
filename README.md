code
Markdown
download
content_copy
expand_less

<div align="center">  ██╗    ██╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗  
██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║  
██║ █╗ ██║█████╗  ██████╔╝███████╗██║     ███████║██╔██╗ ██║  
██║███╗██║██╔══╝  ██╔══██╗╚════██║██║     ██╔══██║██║╚██╗██║  
╚███╔███╔╝███████╗██████║███████║╚██████╗██║  ██║██║ ╚████║  
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

WebDiscover by Faizan Ahmad Khichi (FAK) v2.0

A user-friendly tool for discovering web pages and directories.

</div>  WebDiscover is a powerful yet easy-to-use tool for web content discovery. It helps security researchers, developers, and enthusiasts find hidden pages, directories, and endpoints on a web server using a provided wordlist. It features both a simple interactive mode for beginners and a robust command-line mode for advanced users.


✨ Features

Dual Mode Operation:

Interactive Mode: A guided, step-by-step process perfect for new users.

Command-Line Mode: Full control with flags and arguments for automation and advanced scanning.


Recursive Scanning: Discovered directories can be recursively scanned to find deeper content.

Colored Output: Status codes are color-coded for quick and easy analysis (200 OK, 403 Forbidden, 3xx Redirects).

Customizable Delay: Adjust the delay between requests to be gentle on servers or to speed up scans.

Session Management: Uses requests.Session() for efficient connection pooling.

Comprehensive Wordlist: Comes with a large, well-organized wordlist covering common files, directories, and CMS-specific paths.


⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Faizan-khichi/webscan.git  
cd webscan

Install the required dependencies:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip install -r requirements.txt
Permanent Setup (Recommended)

To make webscan available as a command from anywhere in your terminal, run this one-liner. This will clone the tool, install dependencies, and create a permanent alias.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
git clone https://github.com/Faizan-khichi/webscan.git ~/webscan && pip install -r ~/webscan/requirements.txt && echo "alias webscan='python ~/webscan/web_scanner.py'" >> ~/.bashrc && source ~/.bashrc

🚀 Usage Manual

You can use this tool in two ways: Simple Mode or Advanced Mode.

Note: If you completed the "Permanent Setup", you can use the webscan command instead of python web_scanner.py.

Method 1: Simple Mode (Interactive)

This is the easiest way to get started. Just run the script without any arguments.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
webscan

Or if you haven't set up the alias:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python web_scanner.py

The tool will guide you through the setup. You can stop the scan at any time by pressing Ctrl + C.

Method 2: Advanced Mode (Command-Line)

For more control, use command-line arguments.

A basic scan:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
webscan https://example.com

A deep, recursive scan with a low delay:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
webscan https://example.com -d 0.1 -r 1 -o scan_results.txt

⚠️ Disclaimer

This tool is intended for educational purposes and authorized security assessments only. The author is not responsible for any misuse or damage caused by this program. Always obtain permission from the website owner before scanning.

code
Code
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
