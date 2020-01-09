from test_framework import generic_test



def get_valid_ip_address(s, k=3):
    # TODO - you fill in here.
    def is_valid(s):
        if len(s) == 0:
            return False
        return len(s) == 1 or (s[0] != '0' and 0<= int(s) <= 255)
    
    def helper(string, p, parts):
        if p == 0:
            if is_valid(string):
                parts.append(string)
                valid_ip = '.'.join(parts)
                res.append(valid_ip)
                parts.pop()
            return
        for i in range(1, 4):
            part = string[:i]
            if is_valid(part):
                parts.append(part)
                helper(string[i:], p-1, parts)
                parts.pop()
    
    res = []
    helper(s, k, [])
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    #tests = ['19216811']
    #for t in tests:
    #    print(len(get_valid_ip_address(t)))
    #"""
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
    #"""
