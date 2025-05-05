#problem 3

f=open('problem2.txt')
text=f.read()
text_lower=text.lower()
lol_true = False
textlower_split = text_lower.split("\n")
text_split = text.split("\n")
for e in range(len(text_split)):
    for i in range(len(text_split[e])-2):
        if textlower_split[e][i:i+3] == "lol":
            print(text_split[e])
            break

#guerzhoy's:
for lines in text_split:
    if lines.lower().find("lol")!=-1: #if it doesn'tfind string, it returns -1. so if we want it to return what it finds, we set thecondition !=-1
        print(lines)