def first_unique(text):
    count = {}

    for each_text in text:
        if each_text in count:
            count[each_text] += 1
        else:
            count[each_text] = 1

    for each_text in text:
        if count[each_text] == 1:
            return each_text

    return None
print(first_unique("leetcode"))
print(first_unique("aabbcddee"))
print(first_unique("aabbcc"))