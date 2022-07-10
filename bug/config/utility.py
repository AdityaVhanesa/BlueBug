def resolveId(currentId, A=0, B=0, C=0):
    tempBugId = ""
    if A:
        tempBugId += str(A) + str(currentId + 1)
        return int(tempBugId)

    if B:
        tempBugId += str(A) + str(B) + str(currentId + 1)
        return int(tempBugId)

    if C:
        tempBugId += str(A) + str(B) + str(C) + str(currentId + 1)
        return int(tempBugId)


