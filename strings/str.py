sentence=[["i love that gril very much"],["but she doesnt understand me"],["i also failed to understand her"]]

for sentens in sentence:
    maxword=0
    comp_senc=" "
    if len(sentens[0].split())>maxword:
        maxword=len(sentens[0].split())
        comp_senc=" ".join(sentens)
print(maxword)
print(comp_senc)


