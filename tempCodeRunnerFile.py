True:
    try:
        s = input().strip()
        if s[len(s)-1] not in dau:
            s += '.'
        text += s
    except EOFError:
        br