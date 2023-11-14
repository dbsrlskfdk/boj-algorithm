def solution(s):
    words_to_nums = {"zero": "0", "one": "1", "two" : "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for word in words_to_nums.keys():
        s = s.replace(word, words_to_nums[word]) if word in s else s
    
    answer = int(s)
    return answer