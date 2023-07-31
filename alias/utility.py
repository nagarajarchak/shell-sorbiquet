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
