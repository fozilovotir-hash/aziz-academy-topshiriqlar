th1, lang1, dbg1 = input().split()

th2, lang2, dbg2 = input().split()
theme: th1
theme = th1
if th2 != '-':
    theme = th2
lang = lang1
if lang2 != '-':
    lang = lang2
debug = dbg1
if dbg2 != '-':
    debug = dbg2
print(theme, lang, debug)

