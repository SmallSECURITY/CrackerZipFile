import pyzipper
import os
import time
from datetime import datetime
import random
from colorama import init, Fore, Style

# Initialize colorama
init()

def print_banner():
    banners = [
        """
    ███████╗██╗██████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ╚══███╔╝██║██╔══██╗   ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
      ███╔╝ ██║██████╔╝   ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
     ███╔╝  ██║██╔═══╝    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ███████╗██║██║        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚══════╝╚═╝╚═╝         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """,
        """
    ███████╗██╗██████╗     ██████╗ ██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ╚══███╔╝██║██╔══██╗   ██╔════╝██╔═══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
      ███╔╝ ██║██████╔╝   ██║     ██║   ██║███████║██║     █████╔╝ █████╗  ██████╔╝
     ███╔╝  ██║██╔═══╝    ██║     ██║   ██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ███████╗██║██║        ╚██████╗╚██████╔╝██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚══════╝╚═╝╚═╝         ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """,
        """
    ███████╗██╗██████╗     ██████╗ ██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ╚══███╔╝██║██╔══██╗   ██╔════╝██╔═══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
      ███╔╝ ██║██████╔╝   ██║     ██║   ██║███████║██║     █████╔╝ █████╗  ██████╔╝
     ███╔╝  ██║██╔═══╝    ██║     ██║   ██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ███████╗██║██║        ╚██████╗╚██████╔╝██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚══════╝╚═╝╚═╝         ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """
    ]
    
    print(Fore.RED + random.choice(banners) + Style.RESET_ALL)
    print(f"{Fore.RED}[*] {Fore.WHITE}Developer: {Fore.GREEN}Elias and ChatGpt{Style.RESET_ALL}")
    print(f"{Fore.RED}[*] {Fore.WHITE}GitHub: {Fore.GREEN}https://github.com/minyhacktelegram{Style.RESET_ALL}")
    print(f"{Fore.RED}[*] {Fore.WHITE}Version: {Fore.GREEN}1.2{Style.RESET_ALL}\n")

def print_status(message):
    print(f"{Fore.RED}[*] {Fore.WHITE}{message}{Style.RESET_ALL}")

def print_success(message):
    print(f"{Fore.GREEN}[+] {Fore.WHITE}{message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}[-] {Fore.WHITE}{message}{Style.RESET_ALL}")

def print_info(message):
    print(f"{Fore.BLUE}[i] {Fore.WHITE}{message}{Style.RESET_ALL}")

def crack_zip_password():
    try:
        # Get zip file path
        zip_path = input(f"{Fore.RED}[*] {Fore.WHITE}Enter ZIP file path: {Style.RESET_ALL}")
        if not os.path.exists(zip_path):
            print_error("File not found!")
            return

        # Get password list file path
        password_list_path = input(f"{Fore.RED}[*] {Fore.WHITE}Enter password list path: {Style.RESET_ALL}")
        if not os.path.exists(password_list_path):
            print_error("Password list file not found!")
            return

        # Create output directory if it doesn't exist
        output_dir = "Cracked Files"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Read password list
        with open(password_list_path, 'r', encoding='utf-8', errors='ignore') as file:
            passwords = [line.strip() for line in file]

        print_status(f"Starting password cracking...")
        print_info(f"Target file: {zip_path}")
        print_info(f"Password list: {password_list_path}")
        print_info(f"Total passwords to try: {len(passwords)}")
        print_info("Press Ctrl+C to stop the process\n")

        start_time = time.time()
        tried_passwords = 0

        # Try each password
        for password in passwords:
            tried_passwords += 1
            try:
                with pyzipper.AESZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.setpassword(password.encode())
                    zip_ref.extractall(output_dir)
                    
                    end_time = time.time()
                    duration = end_time - start_time
                    
                    print_success("Password found!")
                    print_info(f"Password: {password}")
                    print_info(f"Time taken: {duration:.2f} seconds")
                    print_info(f"Passwords tried: {tried_passwords}")
                    print_info(f"Files extracted to: {os.path.abspath(output_dir)}")
                    return
            except RuntimeError:
                # Show progress every 100 passwords
                if tried_passwords % 100 == 0:
                    elapsed_time = time.time() - start_time
                    print_status(f"Tried {tried_passwords} passwords in {elapsed_time:.2f} seconds")
            except Exception as e:
                print_error(f"Error: {str(e)}")
                return

        end_time = time.time()
        duration = end_time - start_time
        
        print_error("Password not found!")
        print_info(f"Total time: {duration:.2f} seconds")
        print_info(f"Total passwords tried: {tried_passwords}")

    except KeyboardInterrupt:
        end_time = time.time()
        duration = end_time - start_time
        print_error("Process stopped by user!")
        print_info(f"Time elapsed: {duration:.2f} seconds")
        print_info(f"Passwords tried: {tried_passwords}")
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")

def main():
    print_banner()
    print_status("ZIP Password Cracker Tool")
    print_status("1. Crack password using wordlist")
    print_status("2. Exit")
    
    choice = input(f"\n{Fore.RED}[*] {Fore.WHITE}Enter your choice (1-2): {Style.RESET_ALL}")
    
    if choice == "1":
        crack_zip_password()
    elif choice == "2":
        print_success("Goodbye!")
    else:
        print_error("Invalid choice!")

if __name__ == "__main__":
    main()