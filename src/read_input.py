def read_file(file_path):
    """
    Reads the contents of a file and returns them as a list of lines.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        list: A list of strings, each representing a line in the file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def get_available_towel_patterns(file_path):
    """
    Reads a file containing towel patterns and returns a list of patterns and the number of patterns.

    Args:
        file_path (str): The path to the file containing the towel patterns.

    Returns:
        tuple: A tuple containing a list of patterns (list of str) and the number of patterns (int).
    """
    lines = read_file(file_path)
    patterns_string = lines[0].strip()
    patterns = [pattern.strip() for pattern in patterns_string.split(',')] 
    return patterns

def get_desired_designs(file_path):
    """
    Reads a file and returns a list of desired designs.

    The function skips the first two lines of the file and processes the remaining lines.
    Each line is stripped of leading and trailing whitespace.

    Args:
        file_path (str): The path to the file containing the designs.

    Returns:
        list: A list of desired designs as strings.
    """
    lines = read_file(file_path)
    return [line.strip() for line in lines[2:]]