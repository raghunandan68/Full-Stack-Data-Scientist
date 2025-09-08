def preLetterCase(s,l):
    s=s.lower()
    k=list(s)
    try:
        index=k.index(l)
        for i in range(0,index):
            k[i]=k[i].lower()
        for j in range(index,len(k)):
            k[j]=k[j].upper()
    except:
        return s.lower()
    return ''.join(k)
print(preLetterCase ("CAtCHa","a"))
print(preLetterCase ("Preteen","e"))
print(preLetterCase ("You've got this", "m"))
print(preLetterCase ("Keep trying", "k"))
