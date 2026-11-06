def brute_force(text, pattern, start=0):  # check possible position
    for i in range(start, len(text) - len(pattern) + 1):
        j = 0

        while j < len(pattern):
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == len(pattern):
            return i

    return -1  # the pattern is not found

text = "HELLO WORLD"
pattern = "WORLD"

result = brute_force(text, pattern)

print("텍스트:", text)
print("패턴:", pattern)

if result != -1:
    print("패턴을 찾은 인덱스:", result)
else:
    print("패턴을 찾지 못했습니다.")