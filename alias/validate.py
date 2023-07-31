import alias.constant as c

def validate_input_args(input_args: list) -> bool:
    """
    This function validates input arguments.

    Parameters
    ----------
    :param input_args: The input arguments to validate
    """

    if len(input_args) == 2 and input_args[1] in [c.LIST]:
        return True
    elif len(input_args) == 3:
        return True
    else:
        print("Invalid input arguments provided.")
        return False
    