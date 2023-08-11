import os
import sys
import subprocess
import alias.constant as c
import alias.utility as u
import alias.validate as v

home_dir = os.path.expanduser("~")
bash_rc_file_path = f"{home_dir}/{c.BASH_RC_FILE_NAME}"
bash_alias_file_path = f"{home_dir}/{c.BASH_ALIAS_FILE_NAME}"
contents = f"\n\nif [ -f ~/{c.BASH_ALIAS_FILE_NAME} ]; then\n" \
           f"\t. ~/{c.BASH_ALIAS_FILE_NAME}\n" \
           "fi\n"

def create_empty_alias_script() -> None:
    """
    This function creates an empty shell file for aliases.
    """

    if not os.path.exists(bash_rc_file_path):
        open(f"{home_dir}/{c.BASH_ALIAS_FILE_NAME}", "a").close()

def register_alias(alias: str, sh_command: str) -> None:
    """
    This is a wrapper function to write aliases to shell file.

    Parameters
    ----------
    :param alias: The alias to be written to file
    :param sh_command: The shell command to be written to file
    """

    alias_str = f'alias {alias}="{sh_command}"\n'
    u.write_string_to_file(bash_alias_file_path, alias_str, "a")
    subprocess.Popen(f"source ~/{c.BASH_ALIAS_FILE_NAME}", shell = True)

def list_alias() -> None:
    """
    This is a function to list aliases all.
    """

    if os.path.exists(bash_alias_file_path):
        with open(f"{home_dir}/{c.BASH_ALIAS_FILE_NAME}", "r") as f:
            content = f.readlines()
            if len(content) != 0:
                print("List of aliases:")
                for line in content:
                    line_split = line.split("=")
                    print(f"Alias: {line_split[0].split()[-1]}, Command: {line_split[1][1:-2]}")
            else:
                print("No aliases registered.")

def clear_alias() -> None:
    """
    This is a function to clear all aliases from shell file.
    """

    open(f"{home_dir}/{c.BASH_ALIAS_FILE_NAME}", "w").close()
    print(f"Successfully cleared alias file: {home_dir}/{c.BASH_ALIAS_FILE_NAME}")

def clear_single_alias(alias_name: str) -> None:
    """
    This is a function to clear a single alias.
    
    Parameters
    ----------
    :param alias_name: The alias to be removed from shell file.
    """

    if os.path.exists(bash_alias_file_path):
        updated_alias_list = list()
        with open(f"{home_dir}/{c.BASH_ALIAS_FILE_NAME}", "r") as f:
            content = f.readlines()
            if len(content) != 0:
                for line in content:
                    line_split = line.split("=")
                    if line_split[0].split()[-1] != alias_name:
                        updated_alias_list.append(line)
                if len(updated_alias_list) == len(content):
                    print(f"No alias found for: {alias_name}")
            else:
                print("No aliases registered.")

def main():
    """
    This main entry point function.
    """

    cmd_args = sys.argv
    
    if not v.validate_input_args(cmd_args):
        exit()
    
    if cmd_args[1] == c.LIST:
        list_alias()
    elif cmd_args[1] == c.CLEAR:
        clear_alias()
    elif cmd_args[1] == c.CLEAR and cmd_args[2]:
        clear_single_alias(cmd_args[2])
    else:
        register_alias(cmd_args[1], cmd_args[2])
