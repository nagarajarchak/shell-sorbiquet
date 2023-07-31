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
    if os.path.exists(bash_alias_file_path):
        with open(f"{home_dir}/{c.BASH_ALIAS_FILE_NAME}", "a") as f:
            content = f.readlines()
            print(content)
            print(type(content))

def main():
    """
    This main entry point function.
    """

    cmd_args = sys.argv
    
    if not v.validate_input_args(cmd_args):
        exit()
    
    if cmd_args[1] == c.LIST:
        pass
    else:
        register_alias(cmd_args[1], cmd_args[2])
