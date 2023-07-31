import os
import sys
import subprocess
import alias.constant as c
import alias.utility as u

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

    alias_str = f'\n\nalias {alias}="{sh_command}"'
    u.write_string_to_file(bash_alias_file_path, alias_str, "a")
    subprocess.Popen(f"source ~/{c.BASH_ALIAS_FILE_NAME}", shell = True)

def validate_input_args(input_args: list) -> bool:
    """
    This function validates input arguments.

    Parameters
    ----------
    :param input_args: The input arguments to validate
    """

    validated = True
    if len(input_args) != 3:
        print("Invalid number of input arguments provided.")
        validated = False
    return validated

def main():
    """
    This main entry point function.
    """

    cmd_args = sys.argv
    if validate_input_args(cmd_args):
        register_alias(cmd_args[1], cmd_args[2])
