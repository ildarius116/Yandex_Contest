def encode_word(word):
    mapping = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'
    }
    return ''.join(mapping[char] for char in word)


def decode_message(s, words):
    word_set = set(words)
    encoded_words = {encode_word(word): word for word in word_set}
    dp = [None] * (len(s) + 1)
    dp[0] = []
    for i in range(1, len(s) + 1):
        for j in range(i):
            word_code = s[j:i]
            if word_code in encoded_words and dp[j] is not None:
                dp[i] = dp[j] + [encoded_words[word_code]]
                break
    return ' '.join(dp[len(s)]) if dp[len(s)] else ""


s = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

result = decode_message(s, words)
print(result)
