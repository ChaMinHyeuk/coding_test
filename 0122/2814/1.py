def restructure_word(word, arr):

    for i in range(len(word)):
        if word[i].isdecimal():
            for _ in range(int(word[i])):
                arr.pop(-1)
        elif word[i] in arr:
            arr.remove(word[i])
    
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(original_word)
result = restructure_word(word, arr)
print("".join(result))

