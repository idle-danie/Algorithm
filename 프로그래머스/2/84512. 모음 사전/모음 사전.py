def dict_count(idx, letter):
    vowels = 'AEIOU'
    vowel_idx = vowels.find(letter) 
    return vowel_idx * ((5 ** (5 - idx) - 1) // (5-1))


def solution(word):
    count = 0
    for idx, letter in enumerate(word):
        count += dict_count(idx, letter)    
    return count + len(word)



# 1. 모음만 사용 가능
# 2. 길이 5 이하
# 3. 첫번째 단어는 A  -> AA -> 마지막 UUUUU
# 4. 1 <= word <= 5
# 5. 대문자로만 이루어짐

# word 가 주어지면 몇번째 단어인지

# A E I O U

    # # if idx == 0:
    # #     return vowel_idx * 781       
    # # if idx == 1:
    # #     return vowel_idx * 156       
    # # if idx == 2:
    # #     return vowel_idx * 31
    # # if idx == 3:
    # #     return vowel_idx * 6      
    # return vowel_idx 





