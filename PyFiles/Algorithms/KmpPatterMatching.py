def prefixLength(pattern):
    prefixLength = [0] * len(pattern)

    i, j = 0, 1

    while j < len(pattern):
        if pattern[i] == pattern[j]:
            prefixLength[j] = i + 1
            j += 1
            i += 1
        elif i == 0:
            prefixLength[j] = 0
            j += 1
            i = 0
        else:
            lastLongestPrefixLen = prefixLength[i - 1]
            i = lastLongestPrefixLen

    return prefixLength
