"""
Write a program which takes as input two strings s and t of bits encoding binary numbers
B_s and B_t respectively and returns a new string of bits representing B_s + B_t.
"""

def add(s, t):
    if len(s) > len(t):
        s, t = t, s
    s = s.rjust(len(t), "0")
    res = []
    carry = 0
    for i in range(len(t)-1, -1, -1):
        temp = ord(s[i]) - ord('0')
        temp += ord(t[i]) - ord('0')
        temp += carry
        res.append(str(temp % 2))
        carry = temp >> 1
    if carry:
        res.append(carry)
    res.reverse()
    return "".join(res)

if __name__ == '__main__':
    s = "011011"
    t = "111"
    print(add(s, t))

