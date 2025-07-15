# lib/utils.py
# Utility functions for data processing
def find_common_elements(list1: list, list2: list) -> list:
    # Finds common elements between two lists using an efficient, O(n+m) set-based approach.
    set1 = set(list1)
    common_elements = [item for item in list2 if item in set1]
    return common_elements
