def make_kmp_table(pattern):
    m = len(pattern)

    border = [-1] * (m + 1)
    i = 0
    j = -1

    while i < m:
        # try a shorter prefix
        while j >= 0 and pattern[i] != pattern[j]:
            j = border[j]

        # extend the current border
        i += 1
        j += 1

        border[i] = j

    return border


def kmp_search(pattern, border, text):
    if not pattern:
        return 0

    m = 0  # starting position of the current match
    i = 0  # index of the character compared in the pattern
    t_len = len(text)
    p_len = len(pattern)

    # continue while the current text index is within bounds
    while m + i < t_len:
        if pattern[i] == text[m + i]:  # return the starting index when the entire pattern matches
            if i == p_len - 1:
                return m

            i += 1
        else:
            if border[i] > -1:  # shift the pattern using the border table
                m = m + i - border[i]
                i = border[i]
            else:  # move to the next text position when no border exists
                i = 0
                m += 1

    return -1  # if the pattern is not found

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

border = make_kmp_table(pattern)

result = kmp_search(pattern, border, text)

print("텍스트:", text)
print("패턴:", pattern)
print("부분 일치 테이블:", border)

if result != -1:
    print("패턴을 찾은 인덱스:", result)
else:
    print("패턴을 찾지 못했습니다.")