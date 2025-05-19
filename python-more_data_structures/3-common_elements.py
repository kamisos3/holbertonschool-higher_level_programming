#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Return z set containing the common elements in two sets.
    """
    return set_1 & set_2   # Using set intersection


if __name__ == "__main__":
    set_a = {"Python", "C", "Javascript"}
    set_b = {"Bash", "C", "Ruby", "Perl"}
    print(common_elements(set_a, set_b))   # Expected output: {'C'}
