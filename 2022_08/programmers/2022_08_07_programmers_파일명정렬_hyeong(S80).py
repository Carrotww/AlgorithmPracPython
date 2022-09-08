def solution(files):
    sort_files = []
    result = []
    cnt = 0
    for file in files:
        head, num, tail = [], [], []
        for ch in file:
            if not ch.isdigit() and not num:
                head.append(ch)
            elif ch.isdigit() and not tail:
                num.append(ch)
            else:
                tail.append(ch)
        if not tail:
            sort_files.append([''.join(head), ''.join(num), '', cnt])
        else:
            sort_files.append([''.join(head), ''.join(num), ''.join(tail), cnt])
        cnt += 1

    sort_files = sorted(sort_files, key=lambda x: [x[0].lower(), int(x[1]), x[3]])

    for i in sort_files:
        del i[3]
        result.append(''.join(i))

    return result