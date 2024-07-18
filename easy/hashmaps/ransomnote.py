# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and 
# false otherwise.

def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    # put elts of magazine into hashMap
    hashMag = {}
    for character in magazine:
        if character in hashMag:
            hashMag[character] += 1
        else:
            hashMag[character] = 1
    
    # loop thru ransom note
    # return False if conditions don't apply
    for c in ransomNote:
        if c not in hashMag: 
            return False
        else: 
            if hashMag[c] < 1: return False
            else: hashMag[c] -= 1
    
    return True
