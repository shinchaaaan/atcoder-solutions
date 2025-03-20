N = int(input())
cards = list(map(int, input().split()))
sorted_cards = sorted(cards)
is_first = True
alice_score = 0
bob_score = 0

while sorted_cards:
    if is_first:
        alice_score += sorted_cards.pop(-1)
        is_first = False
    else:
        bob_score += sorted_cards.pop(-1)
        is_first = True

print(alice_score - bob_score)
