"""
Auxiliary function module
"""


def numerate_line(num: int, line: str, num_width: int=3) -> str:
    """
    Returns numbered line

    input:
        num - number of the line
        line -  line content
        num_width - the count of characters that the line number occupies

    output:
        result - numbered line 
    """
    result = str(num).ljust(num_width) + line
    return result

