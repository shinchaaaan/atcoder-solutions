# ABC146 B
def shift_letters(text, shift):
    result = ''
    for char in text:
        shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        result += shifted
    return result

N = int(input())
S = input()

print(shift_letters(S, N))

