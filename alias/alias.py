import os
import sys
import subprocess
import constant as c

home_dir = os.path.expanduser("~")
bash_rc_file_path = f"{home_dir}/{c.BASH_RC_FILE_NAME}"
bash_alias_file_path = f"{home_dir}/{c.BASH_ALIAS_FILE_NAME}"
contents = f"\n\nif [ -f ~/{c.BASH_ALIAS_FILE_NAME} ]; then\n" \
           f"\t. ~/{c.BASH_ALIAS_FILE_NAME}\n" \
           "fi\n"

def check_file_contains_string(file_path: str, phrase: str) -> bool:
    """
    This function checks if a given string is present in the
    given file path.

    Parameters
    ----------
    :param file_path: The file path to check for string
    :param phrase: The string phrase to check for existance

    Returns
    -------
    A boolean indicating if the string is present or not
    """

    if phrase in open(file_path).read():
        return True
    return False

def write_string_to_file(file_path: str, contents: str, mode: str) -> None:
    """
    This function writes a given string to file.

    Parameters
    ----------
    :param file_path: The file path to write string to
    :param contents: The string to be written
    :param mode: The write mode
    """

    with open(file_path, mode) as file:
        file.write(contents)
        file.close()

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
    write_string_to_file(bash_alias_file_path, alias_str, "a")
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
