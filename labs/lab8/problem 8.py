'''def make_link(search):
    L = search.split()
    mod_search = ""
    for i in range (len(L)):
        if i == len((L))-1:
            mod_search = mod_search + str(L[i])
        else:
            mod_search = mod_search + str(L[i]) + "+"
    link = ("https://ca.search.yahoo.com/search?p=" + mod_search + "fr=yfp-t-s&fp=1&toggle=1&cop=mss&ei=UTF-8")
    return link'''

def search_results(search):
    L = search.split()
    mod_search = ""
    for i in range (len(L)):
        if i == len((L))-1:
            mod_search = mod_search + str(L[i])
        else:
            mod_search = mod_search + str(L[i]) + "+"
    link = ("https://ca.search.yahoo.com/search?p=" + mod_search + "fr=yfp-t-s&fp=1&toggle=1&cop=mss&ei=UTF-8")
    import urllib.request
    f = urllib.request.urlopen(link)
    page = f.read().decode("utf-8")
    L1 = page.split()
    possible = []
    for i in range (len(L1)):
        if L1[i] == "search":
            possible.append(L1[i-1])
    for e in possible:
        if e[0].isdigit() == True:
            return e
    f.close()

print(search_results("hi hi"))



