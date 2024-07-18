def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # essentially checking if s and t hav same form by mapping the elts of each together
    # if s = "egg", t = "add"
    # map_s: e -> a, g -> d
    # map_t: a -> e, d -> g
    # then check if as you loop thru everything that it's mapped and mapped correctly

    map_s = {}
    map_t = {}

    for i in range(len(s)):
        # check negative condition
        if (s[i] in map_s and map_s[s[i]] != t[i]) or (t[i] in map_t and map_t[t[i]] != s[i]):
            return False

        # map the characters to eachother in both maps
        map_s[s[i]] = t[i]
        map_t[t[i]] = s[i]

    return True 