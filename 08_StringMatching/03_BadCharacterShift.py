def make_bad_char_table(pattern):
    bad_char = {}

    # save the last index of character in the pattern
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i

    return bad_char


def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    bad_char = make_bad_char_table(pattern)

    # start matching from the beginning of text
    shift = 0

    while shift <= n - m:  # start comparing from the end of pattern
        j = m - 1

        # move left while characters are same
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        # if j is under 0 ->  pattern is found
        if j < 0:
            return shift
        else:  # find where the bad character appear
            bad_index = bad_char.get(text[shift + j], -1)

            # move the pattern to the right
            shift += max(1, j - bad_index)

    return -1

text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"

result = boyer_moore_search(text, pattern)

print("text:", text)
print("pattern:", pattern)

if result != -1:
    print("pattern found at index:", result)
else:
    print("pattern not found")