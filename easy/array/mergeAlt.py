def mergeAlternately(self, word1: str, word2: str) -> str:
    p1, p2 = 0, 0
    result = ""

    # break when end of word1 or word2 (shortest word)
    while p1 < len(word1) and p2 < len(word2):
        result += word1[p1]
        result += word2[p2]
        p1+=1
        p2+=1

    # check which word is long + leftover chars
    while p1<len(word1):
        result+=word1[p1]
        p1+=1
    while p2<len(word2):
        result+=word2[p2]
        p2+=1
    
    # return merged str
    return result

    