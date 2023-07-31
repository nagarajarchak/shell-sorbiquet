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