import os
import sys

BASH_RC_FILE_NAME = ".bashrc"
BASH_ALIAS_FILE_NAME = ".shell-sobriquet-aliases.sh"

home_dir = os.path.expanduser("~")
bash_rc_file_path = f"{home_dir}/{BASH_RC_FILE_NAME}"
bash_alias_file_path = f"{home_dir}/{BASH_ALIAS_FILE_NAME}"
contents = f"\n\nif [ -f ~/{BASH_ALIAS_FILE_NAME} ]; then\n" \
           f"\t. ~/{BASH_ALIAS_FILE_NAME}\n" \
           "fi\n"

def check_file_contains_string(file_path: str, phrase: str) -> bool:
    if phrase in open(file_path).read():
        return True
    return False

def write_string_to_file(file_path: str, contents: str, mode: str) -> None:
    with open(file_path, mode) as file:
        file.write(contents)
        file.close()

def register_alias_script() -> None:
    if os.path.exists(bash_rc_file_path):
        if check_file_contains_string(bash_rc_file_path, BASH_ALIAS_FILE_NAME):
            write_string_to_file(bash_rc_file_path, contents, "a")
    else:
        write_string_to_file(bash_rc_file_path, contents, "a")

def create_empty_alias_script() -> None:
    if not os.path.exists(bash_rc_file_path):
        open(f"{home_dir}/{BASH_ALIAS_FILE_NAME}", "a").close()

def main():
    cmd_args = sys.argv
    print(cmd_args)
    alias = cmd_args[1]
    sh_command = cmd_args[2]