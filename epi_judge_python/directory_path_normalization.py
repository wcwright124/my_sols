from test_framework import generic_test


def shortest_equivalent_path(path):
    # TODO - you fill in here.
    if not path:
        return ''
    stack = []
    if path[0] == '/':
        stack.append('/')
    path_split = path.split('/')
    for part in path_split:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if not stack or stack[-1] == '..':
                stack.append(part)
            else:
                if stack[-1] == '/':
                    return 
                stack.pop()
        else:
            stack.append(part)
    res = '/'.join(stack)
    if len(res) < 2:
        return res
    if res[0:2] == '//':
        return res[1:]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
