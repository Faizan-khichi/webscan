#!/usr/bin/env python3

import requests
import argparse
import sys
import time
import os
from urllib.parse import urljoin

# --- Color Codes for Terminal Output ---
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def display_banner():
    """Prints the ASCII art banner for the tool."""
    banner = f"""
{Colors.BLUE}<div align="center">
  ██╗    ██╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
  ██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
  ██║ █╗ ██║█████╗  ██████╔╝███████╗██║     ███████║██╔██╗ ██║
  ██║███╗██║██╔══╝  ██╔══██╗╚════██║██║     ██╔══██║██║╚██╗██║
  ╚███╔███╔╝███████╗██████║███████║╚██████╗██║  ██║██║ ╚████║
   ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

  WebDiscover by Faizan Ahmad Khichi (FAK) v2.0
  A user-friendly tool for discovering web pages and directories.
</div>{Colors.RESET}
"""
    print(banner)

def get_status_colored(status_code):
    """Returns a color-coded string for a given HTTP status code."""
    if 200 <= status_code < 300:
        return f"{Colors.GREEN}{status_code}{Colors.RESET}"
    elif 300 <= status_code < 400:
        return f"{Colors.YELLOW}{status_code}{Colors.RESET}"
    elif 400 <= status_code < 500:
        if status_code == 403:
            return f"{Colors.RED}{status_code}{Colors.RESET}"
        return f"{Colors.BLUE}{status_code}{Colors.RESET}"
    else:
        return f"{Colors.RED}{status_code}{Colors.RESET}"

def scan(base_url, wordlist_path, delay, output_file, max_depth, current_depth=0):
    """
    Performs the web content discovery scan.
    This function is recursive.
    """
    if current_depth > max_depth:
        return

    try:
        with open(wordlist_path, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Colors.RED}[-] Error: Wordlist not found at '{wordlist_path}'{Colors.RESET}")
        return

    session = requests.Session()
    session.headers.update({'User-Agent': 'WebDiscover/2.0'})

    print(f"\n{Colors.YELLOW}[*] Starting scan on: {base_url} (Depth: {current_depth}){Colors.RESET}")
    print(f"{'Status':<10} {'URL':<60}")
    print(f"{'-'*10} {'-'*60}")

    for word in words:
        try:
            target_url = urljoin(base_url + '/', word)
            response = session.get(target_url, timeout=10, allow_redirects=True)
            
            status_code = response.status_code
            status_colored = get_status_colored(status_code)
            
            # Print significant status codes
            if status_code < 400 or status_code == 403:
                result_line = f"[{status_colored}]    {target_url}"
                print(result_line)

                if output_file:
                    with open(output_file, 'a') as f:
                        f.write(f"[{status_code}] {target_url}\n")
                
                # If recursion is enabled and a directory is found, scan it
                if max_depth > current_depth and (200 <= status_code < 300) and target_url.endswith('/'):
                    scan(target_url, wordlist_path, delay, output_file, max_depth, current_depth + 1)
            
            time.sleep(delay)

        except requests.exceptions.RequestException as e:
            # print(f"{Colors.RED}[-] Connection error for {target_url}: {e}{Colors.RESET}")
            pass # Suppress connection errors for cleaner output
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[!] Scan interrupted by user. Exiting...{Colors.RESET}")
            sys.exit(0)

def interactive_mode():
    """Guides the user through setting up a scan interactively."""
    print(f"\n{Colors.YELLOW}--- Interactive Mode ---{Colors.RESET}")
    
    # Get Target URL
    while True:
        target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
        if target_url.startswith("http://") or target_url.startswith("https://"):
            break
        print(f"{Colors.RED}Invalid URL. Please include http:// or https://{Colors.RESET}")
    
    # Get Wordlist
    default_wordlist = "wordlist.txt"
    wordlist_path = input(f"Enter the path to your wordlist (default: {default_wordlist}): ").strip() or default_wordlist
    if not os.path.isfile(wordlist_path):
        print(f"{Colors.RED}Wordlist not found at '{wordlist_path}'. Please check the path.{Colors.RESET}")
        return

    # Get Delay
    while True:
        try:
            delay_str = input("Enter delay between requests in seconds (default: 0): ").strip() or "0"
            delay = float(delay_str)
            break
        except ValueError:
            print(f"{Colors.RED}Invalid input. Please enter a number.{Colors.RESET}")

    # Get Recursion Depth
    while True:
        try:
            depth_str = input("Enter recursion depth (e.g., 1 for one level deep, 0 for none): ").strip() or "0"
            recursion_depth = int(depth_str)
            break
        except ValueError:
            print(f"{Colors.RED}Invalid input. Please enter a whole number.{Colors.RESET}")

    # Get Output File
    output_file = input("Enter output file name to save results (optional, press Enter to skip): ").strip() or None

    scan(target_url, wordlist_path, delay, output_file, recursion_depth)


def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="WebDiscover v2.0 - A tool for discovering web pages and directories.",
        epilog="Example: python web_scanner.py http://example.com -r 1 -d 0.1 -o results.txt"
    )
    
    parser.add_argument("url", nargs='?', default=None, help="The target URL to scan.")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="Path to the wordlist file.")
    parser.add_argument("-d", "--delay", type=float, default=0, help="Delay between requests in seconds.")
    parser.add_argument("-r", "--recursive", type=int, default=0, help="Maximum recursion depth (0 for no recursion).")
    parser.add_argument("-o", "--output", help="Save results to an output file.")

    args = parser.parse_args()

    if args.url is None:
        # No URL provided, enter interactive mode
        interactive_mode()
    else:
        # URL provided, run in command-line mode
        if not (args.url.startswith("http://") or args.url.startswith("https://")):
            print(f"{Colors.RED}Error: URL must start with http:// or https://{Colors.RESET}")
            sys.exit(1)
        scan(args.url, args.wordlist, args.delay, args.output, args.recursive)

    print(f"\n{Colors.GREEN}[+] Scan complete.{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Program terminated by user. Exiting.{Colors.RESET}")
        sys.exit(0)
