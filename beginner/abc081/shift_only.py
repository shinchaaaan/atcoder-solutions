def is_even_list(numbers_list):
    """リスト内のすべての数が偶数か判定"""
    for number in numbers_list:
        if number % 2 != 0:
            return False
    return True
        
def divided_list(numbers_list):
    """リスト内のすべての数を２で割る"""
    divided_numbers = [n // 2 for n in numbers_list]
    return divided_numbers

N = int(input())
numbers_list = list(map(int, input().split()))

count = 0
while is_even := is_even_list(numbers_list):
    numbers_list = divided_list(numbers_list)
    count += 1
print(count)