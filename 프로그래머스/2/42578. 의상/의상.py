def solution(clothes):
    category_count = {}
    for _, category in clothes:
        category_count[category] = category_count.get(category, 0) + 1
    combinations = 1
    for count in category_count.values():
        combinations *= (count + 1)

    return combinations - 1



