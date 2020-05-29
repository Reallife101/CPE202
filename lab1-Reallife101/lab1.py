def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:  # Checks to see if the List is empty
        raise ValueError()  # If so, raise a ValueError

    if not int_list:  # Checks to see if the List is []
        return None  # If so, return none

    x = int_list[0]  # Sets x(the max value) to the first item of the list
    for val in int_list:  # Iterates through entire list
        if x < val:
            x = val
    return x


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None:  # Checks to see if the List is empty
        raise ValueError()  # If so, raise a ValueError

    if not int_list:  # Checks to see if the List is []
        return []  # If so, return none

    new_list = []

    if len(int_list) == 1:  # Base Case: if list is 1 item long, just return that one item
        return int_list

    new_list.append(int_list[len(int_list) - 1])  # Adds last item of int_list to the end of new_list
    int_list.remove(int_list[len(int_list) - 1])  # Removes the just added item of int_list
    new_list = new_list + reverse_rec(int_list)  # recursively adds the next last item by calling the function again
    # and adding it to the end of the list
    return new_list  # Returns the newly reversed list


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    # (high-low)/2+low
    if int_list is None:  # Checks to see if the List is empty
        raise ValueError()  # If so, raise a ValueError

    if not int_list:  # Checks to see if the List is []
        return None  # If so, return none

    mid = (high + low) // 2  # Setting Midpoint index

    if int_list[high] == target:
        return high

    if int_list[mid] == target:  # if you find the target, return index
        return mid

    if low == high:  # In the case target doesn't exist
        return None

    if int_list[mid] > target:
        return bin_search(target, low, mid - 1, int_list)
    if int_list[mid] < target:
        return bin_search(target, mid + 1, high, int_list)
