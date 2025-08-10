def restoreIpAddresses(s):
    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        for end in range(start + 1, min(len(s) + 1, start + 4)):
            part = s[start:end]
            if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                continue
            path.append(part)
            backtrack(end, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

print(restoreIpAddresses("25525511135"))
