i = len(string) - 1
    while i > 0 and ord(string[i - 1]) >= ord(string[i]):
        i -= 1
    if i <= 0:
        return "no answer"
    j = len(string) - 1
    while ord(string[j]) <= ord(string[i - 1]):
        j -= 1
    string = list(string)
    string[i - 1], string[j] = string[j], string[i - 1]
    string[i:] = reversed(string[i:])
    return "".join(string)