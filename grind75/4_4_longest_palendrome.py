def longestPalindrome(s: str) -> int:
    # palendrome requires at least 2 letters being the same on each side.
    # so if we can see how many "pairs" there are at least in the string
    # and add 1 if we have a single letter left over, we can get max length.
    char_map = {}
    for c in s:
        char_map[c] = 1 + char_map.get(c, 0)
    # print(char_map)
    num_pairs = 0
    while True:
        curr_max_char = max(char_map, key=char_map.get)
        # print(curr_max_char, char_map[curr_max_char])
        if char_map[curr_max_char] <= 1:
            if char_map[curr_max_char]:
                return (num_pairs * 2) + 1
            return num_pairs * 2
        pairs = char_map[curr_max_char] // 2
        num_pairs += pairs
        # print(num_pairs)
        char_map[curr_max_char] -= 2 * pairs
    # could we also solve this with a max heap?...


# print(longestPalindrome("abccccdd"))  # 7


def long_pal(s: str) -> int:
    char_map = {}
    for c in s:
        char_map[c] = 1 + char_map.get(c, 0)

    chars = 0
    odd = 0
    # for each value in the dict, we dont care about the
    # actual chars rn
    for v in char_map.values():
        # if its > than 1
        if v > 1:
            # if its an even number add all values to char
            if v % 2 == 0:
                chars += v
            # if its odd, add count - 1, add 1 to "odd" counter
            else:
                chars += v - 1
                odd += 1
        # if its == to 1 then add 1 to odd counter
        else:
            odd += 1
    # if odd counter has more than 1 char, we can add a middle char
    if odd >= 1:
        chars += 1
    
    return chars


print(long_pal("abccccdd"))  # 7
print(long_pal("ccc"))  # 7
