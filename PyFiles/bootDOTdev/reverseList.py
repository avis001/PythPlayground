def reverse_array(items):
    reveresedList = []

    for index in range(1, len(items) + 1):
        reveresedList.append(items[-index])

    return reveresedList
