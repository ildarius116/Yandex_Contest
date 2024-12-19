def find_words(strng: str):
    words = strng.split('#')
    tmp_list = []
    for word in words:
        if len(word) >= 2:
            tmp_list.append(word)
    return tmp_list


result_list = []
words_list = []
all_words_dict = {}
all_words_list = []
R, C = map(int, input().split())
for _ in range(R):
    word = input()
    words_list.append(word)
    word_check = find_words(word)
    if word_check:
        for word in word_check:
            all_words_list.append(word)

for i in range(C):
    tmp_list = []
    tmp_word = ''
    for word in words_list:
        tmp_list.append(word[i])
    tmp_word = ''.join(tmp_list)
    word_check = find_words(tmp_word)
    if word_check:
        for word in word_check:
            all_words_list.append(word)
min_word = min(all_words_list)
print(min_word)

# print(words_list)
# print(all_words_list)
# min_in_row = min(words_list)
# min_in_col = min(words_list_col)
# print(min_in_row)
# print(min_in_col)

# print(' '.join(result_list))
