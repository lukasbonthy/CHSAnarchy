from colorama import Fore, Back, Style
import os
print(Fore.GREEN + 'EaglerCux 2024')
print(Fore.CYAN + 'Use the branch "MAIN" for the latest commands or use "HELP" to view all commands')
print(Style.RESET_ALL)
cmd = input("Enter command here: ")
if cmd == "help":
    print("str - start server only")
    print("motd - edit the motd")
    print("setupsvr - setup/update server")
elif cmd == "motd":
    motd = input("Paste motd here: ")
    # Define the file path and the line to edit
    file_path = '/workspaces/EaglerCux/velocity/plugins/eaglerxvelocity/listeners.yml'
    line_to_edit = 9  # Line 10 in Python is index 9 (0-based indexing)

    # Read the file contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace line 10 with the desired content
    lines[line_to_edit] = f"- '&1{motd}'\n"

    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
elif cmd == "setupsvr":
    os.system('sudo apt update -y & sudo apt full-upgrade -y & sudo apt autoremove -y & sudo apt auto-clean -y & sdk install java 17.0.9-amzn')
elif cmd == "str":
    os.system('cd server & chmod +x server.sh & ./server.sh')
