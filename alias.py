import os

BASH_RC_FILE_NAME = ".bashrc"
BASH_ALIAS_FILE_NAME = ".shell-sobriquet-aliases.sh"

home_dir = os.path.expanduser("~")
bash_rc_file_path = f"{home_dir}/{BASH_RC_FILE_NAME}"
bash_alias_file_path = f"{home_dir}/{BASH_ALIAS_FILE_NAME}"

if os.path.exists(bash_rc_file_path):
    with open(bash_rc_file_path) as file:
        if BASH_ALIAS_FILE_NAME not in file.read():
            file.close()
            with open(bash_rc_file_path, "a") as file:
                lines = f"\n\nif [ -f ~/{BASH_ALIAS_FILE_NAME} ]; then\n" \
                        f"\t. ~/{BASH_ALIAS_FILE_NAME}\n" \
                        "fi\n"
                file.write(lines)
                file.close()
else:
    with open(bash_rc_file_path, "a") as file:
        lines = f"\n\nif [ -f ~/{BASH_ALIAS_FILE_NAME} ]; then\n" \
                f"\t. ~/{BASH_ALIAS_FILE_NAME}\n" \
                "fi\n"
        file.write(lines)
        file.close()

if not os.path.exists(bash_rc_file_path):
    open(f"{home_dir}/{BASH_ALIAS_FILE_NAME}", 'a').close()

