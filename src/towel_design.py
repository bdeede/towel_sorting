from read_input import get_available_towel_patterns, get_desired_designs

def design_towels(file_path):
    """
    Generates towel designs based on available patterns and desired designs.
    Args:
        file_path (str): The path to the file containing available patterns and desired designs.
    Returns:
        tuple: A tuple containing:
            - output (list of str): A list of strings describing whether each desired design can be made and with which patterns.
            - possible_design_cnt (int): The count of possible designs that can be made from the available patterns.
    """
    try:
        available_patterns = get_available_towel_patterns(file_path)
        desired_designs = list(set(get_desired_designs(file_path)))
    except FileNotFoundError:
        return ["Error: File not found."], 0
    except Exception as e:
        return [f"Error: {str(e)}"], 0

    available_patterns.sort(key=len, reverse=True)
    
    output = []
    possible_design_cnt = 0
    for desired_design in desired_designs:
        design_possible = _can_form_design(desired_design, available_patterns)
        if design_possible:
            towel_design_pattern = _get_towel_design_pattern(desired_design, available_patterns, [])

            if len(towel_design_pattern) > 0: 
                possible_design_cnt += 1
                if len(towel_design_pattern) > 1:
                    design_pattern_sequence_str = ', '.join(towel_design_pattern[:-1]) + ' and ' + towel_design_pattern[-1]
                else:
                    design_pattern_sequence_str = towel_design_pattern[0]

                output.append(f'{desired_design} can be made with {design_pattern_sequence_str}')
            else:
                output.append(f'{desired_design} impossible')
        else:
            output.append(f'{desired_design} impossible')

    return output, possible_design_cnt

def _can_form_design(desired_design: str, available_patterns: list) -> bool:
    return any(desired_design.startswith(pattern) for pattern in available_patterns)

def _get_towel_design_pattern(desired_design: str, available_patterns: list, design_pattern_sequence: list = []) -> list:
    if desired_design == "":
        return design_pattern_sequence
    
    for pattern in available_patterns:
        if desired_design.startswith(pattern):
            new_sequence = design_pattern_sequence + [pattern]
            remaining_design = desired_design[len(pattern):]
            result_sequence = _get_towel_design_pattern(remaining_design, available_patterns, new_sequence)
            if result_sequence:
                return result_sequence
    
    return []  # return empty list if the desired design cannot be formed by the available patterns