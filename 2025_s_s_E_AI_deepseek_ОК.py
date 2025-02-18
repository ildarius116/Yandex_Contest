def decode_message(s, dictionary):
    digit_to_letters = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }

    word_to_code = {}
    for word in dictionary:
        code = ''
        for char in word:
            for key, letters in digit_to_letters.items():
                if char in letters:
                    code += key * (letters.index(char) + 1)
                    break
        word_to_code[word] = code

    dp = [None] * (len(s) + 1)
    dp[0] = 0

    for i in range(len(s) + 1):
        if dp[i] is not None:
            for word in dictionary:
                code = word_to_code[word]
                if s[i:i + len(code)] == code:
                    if dp[i + len(code)] is None:
                        dp[i + len(code)] = word

    result = []
    i = len(s)
    while i > 0:
        word = dp[i]
        result.append(word)
        i -= len(word_to_code[word])

    result.reverse()
    return ' '.join(result)


s = input().strip()
n = int(input().strip())
dictionary = [input().strip() for _ in range(n)]

print(decode_message(s, dictionary))
