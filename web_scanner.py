import requests
import time
import argparse
import os
import sys
from urllib.parse import urljoin
from colorama import init, Fore, Style

# Initialize colorama for colored console output
init(autoreset=True)

def print_banner():
    """Prints the visually enhanced banner for the tool."""
    banner = """
    ██╗    ██╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
    ██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
    ██║ █╗ ██║█████╗  ██████╔╝█████╗  ██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
    ██║███╗██║██╔══╝  ██╔══██╗██╔══╝  ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
    ╚███╔███╔╝███████╗██║  ██║███████╗╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    """
    by_line = "                           WebDiscover by Faizan Ahmad Khichi (FAK) v2.0"
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + by_line + "\n")

def print_user_manual():
    """Prints a quick user manual for interactive mode."""
    print(Style.BRIGHT + Fore.WHITE + "--- Welcome to WebDiscover ---")
    print("This tool helps you find hidden pages and directories on a website.")
    print("\n" + Fore.GREEN + "How to use this guide:")
    print("1. Enter the full URL of the website you want to scan (e.g., https://example.com).")
    print("2. Choose a scan mode:")
    print(f"   - {Style.BRIGHT}Quick Scan:{Style.NORMAL} Fast, uses a common wordlist, no deep searching.")
    print(f"   - {Style.BRIGHT}Deep Scan:{Style.NORMAL}  Slower, more thorough, and checks one level deeper for directories.")
    print(f"   - {Style.BRIGHT}Custom:{Style.NORMAL}     You control all the settings.")
    print(f"\n{Fore.YELLOW}[i] During the scan, press {Style.BRIGHT}Ctrl + C{Style.NORMAL}{Fore.YELLOW} at any time to stop.")
    print(Style.BRIGHT + Fore.WHITE + "-" * 30 + "\n")

def get_interactive_config():
    """Gets scan configuration from the user via prompts."""
    print_user_manual()
    config = {}

    # Get URL
    while True:
        url = input(Style.BRIGHT + Fore.WHITE + "Enter the target URL (e.g., https://example.com): " + Style.RESET_ALL)
        if url.startswith("http://") or url.startswith("https://"):
            config['url'] = url
            break
        else:
            print(Fore.RED + "[!] Invalid URL. Please include 'http://' or 'https://'.")

    # Get Scan Mode
    print("\n" + Style.BRIGHT + Fore.WHITE + "Choose a scan mode:")
    print("1. Quick Scan (Recommended for beginners)")
    print("2. Deep Scan (More thorough, takes longer)")
    print("3. Custom Scan (Advanced users)")
    
    while True:
        choice = input(Style.BRIGHT + Fore.WHITE + "Enter your choice (1/2/3): " + Style.RESET_ALL)
        if choice == '1': # Quick Scan
            config['wordlist'] = 'wordlist.txt'
            config['delay'] = 0.2
            config['recursive'] = 0
            config['output'] = 'found_pages_quick.txt'
            break
        elif choice == '2': # Deep Scan
            config['wordlist'] = 'wordlist.txt'
            config['delay'] = 0.1
            config['recursive'] = 1
            config['output'] = 'found_pages_deep.txt'
            break
        elif choice == '3': # Custom Scan
            config['wordlist'] = input("  Enter path to wordlist (default: wordlist.txt): ") or 'wordlist.txt'
            while True:
                try:
                    config['delay'] = float(input("  Enter delay between requests in seconds (default: 0.2): ") or 0.2)
                    break
                except ValueError:
                    print(Fore.RED + "[!] Invalid number. Please enter a value like 0.1, 0.5, etc.")
            while True:
                try:
                    config['recursive'] = int(input("  Enter recursive depth (0=disabled, 1=one level deep, etc.): ") or 0)
                    break
                except ValueError:
                    print(Fore.RED + "[!] Invalid number. Please enter a whole number like 0, 1, 2.")
            config['output'] = input("  Enter output file name (default: found_pages_custom.txt): ") or 'found_pages_custom.txt'
            break
        else:
            print(Fore.RED + "[!] Invalid choice. Please enter 1, 2, or 3.")
            
    return argparse.Namespace(**config)

def scan_path(base_url, path, session, delay, output_file, scanned_paths):
    """Scans a single path, checks the response, and logs if found."""
    full_url = urljoin(base_url, path)
    
    if full_url in scanned_paths:
        return None, None
    scanned_paths.add(full_url)

    try:
        response = session.get(full_url, timeout=10, allow_redirects=True, verify=False) # Added verify=False for convenience
        status_code = response.status_code
        content_length = len(response.content)

        if status_code == 200:
            print(f"{Fore.GREEN}[+] FOUND:     {full_url:<50} [Status: 200 OK] [Size: {content_length} B]")
            with open(output_file, 'a') as f:
                f.write(full_url + '\n')
        elif status_code == 403:
            print(f"{Fore.YELLOW}[!] FORBIDDEN: {full_url:<50} [Status: 403 Forbidden]")
            with open(output_file, 'a') as f:
                f.write(f"{full_url} (Forbidden)\n")
        elif 300 <= status_code < 400:
            print(f"{Fore.BLUE}[i] REDIRECT:  {full_url:<50} [Status: {status_code}] -> {response.url}")
            with open(output_file, 'a') as f:
                f.write(f"{full_url} (Redirects to {response.url})\n")
        
        time.sleep(delay)
        return status_code, path

    except requests.exceptions.RequestException as e:
        # Silently handle common errors for a cleaner output, or print for debug
        # print(f"{Fore.RED}[!] ERROR: Could not connect to {full_url}. ({e})")
        time.sleep(delay)
        return None, None

def start_scan(base_url, wordlist_paths, delay, output_file, recursive_depth):
    """Main function to orchestrate the scanning process."""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'WebDiscover/2.0 (Security Scanner by FAK)'
    })
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


    scanned_paths = set()
    paths_to_scan = [(path, 0) for path in wordlist_paths]
    
    total_paths = len(paths_to_scan)
    print(f"\n{Style.BRIGHT}[*] Starting scan of {total_paths} initial paths...")
    print(f"{Fore.YELLOW}[i] Press Ctrl+C to stop the scan.\n")

    while paths_to_scan:
        path, current_depth = paths_to_scan.pop(0)
        
        status_code, found_path = scan_path(base_url, path, session, delay, output_file, scanned_paths)

        if recursive_depth > 0 and status_code in [200, 301, 302, 307, 403] and current_depth < recursive_depth:
            # Heuristic: if a path is found and doesn't look like a file, treat it as a directory
            if '.' not in os.path.basename(found_path) or found_path.endswith('/'):
                print(f"{Fore.CYAN}[*] Found directory '{found_path}'. Queuing recursive scan (depth {current_depth + 1})...")
                for next_word in wordlist_paths:
                    new_path = f"{found_path.strip('/')}/{next_word.strip('/')}"
                    if (new_path, current_depth + 1) not in paths_to_scan:
                        paths_to_scan.append((new_path, current_depth + 1))

if __name__ == "__main__":
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="WebDiscover: A simple Python tool to discover pages on a website.",
        epilog="Example (Advanced): python web_scanner.py https://example.com -w wordlist.txt -d 0.1 -r 1 -o results.txt"
    )
    parser.add_argument("url", nargs='?', default=None, help="The base URL of the website to scan (e.g., https://example.com).")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="Path to the wordlist file (default: wordlist.txt).")
    parser.add_argument("-d", "--delay", type=float, default=0.2, help="Delay in seconds between requests (default: 0.2).")
    parser.add_argument("-o", "--output", default="found_pages.txt", help="File to log found pages (default: found_pages.txt).")
    parser.add_argument("-r", "--recursive", type=int, default=0, metavar="DEPTH", help="Enable recursive scanning up to a certain depth (e.g., 1). Default is 0 (disabled).")
    
    # If no command-line arguments are given (besides the script name), run interactive mode
    if len(sys.argv) == 1:
        args = get_interactive_config()
    else:
        args = parser.parse_args()
        if not args.url:
            print(Fore.RED + "[!] ERROR: The 'url' argument is required for command-line use.")
            parser.print_help()
            sys.exit(1)
            
    # --- Input Validation ---
    if not os.path.exists(args.wordlist):
        print(f"{Fore.RED}[!] ERROR: Wordlist file not found at '{args.wordlist}'")
        sys.exit(1)

    # --- Read Wordlist ---
    print(f"\n{Style.BRIGHT}[*] Loading wordlist from: {args.wordlist}")
    with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        wordlist = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    
    # --- Print Scan Summary ---
    print(Fore.WHITE + Style.BRIGHT + "\n" + "="*50)
    print("           SCAN CONFIGURATION SUMMARY")
    print("="*50)
    print(f"{Fore.CYAN}Target URL:      {Fore.WHITE}{args.url}")
    print(f"{Fore.CYAN}Wordlist:        {Fore.WHITE}{args.wordlist} ({len(wordlist)} entries)")
    print(f"{Fore.CYAN}Delay:           {Fore.WHITE}{args.delay} seconds")
    print(f"{Fore.CYAN}Recursive Depth: {Fore.WHITE}{args.recursive}")
    print(f"{Fore.CYAN}Output File:     {Fore.WHITE}{args.output}")
    print(Style.BRIGHT + "="*50)
    
    try:
        # Clear output file before starting
        open(args.output, 'w').close()
        start_scan(args.url, wordlist, args.delay, args.output, args.recursive)
        print(f"\n{Fore.GREEN}{Style.BRIGHT}[+] Scan complete! Found pages have been saved to {args.output}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[!] Scan interrupted by user. Partial results saved to {args.output}. Exiting.")
    except Exception as e:
        print(f"\n{Fore.RED}{Style.BRIGHT}[!] An unexpected error occurred: {e}")