#problem 4

def dict_to_str(d):
    d_str=""
    dict_str=str(d)
    for e in range(len(dict_str)):
        if dict_str[e] == ":":
            d_str+=dict_str[e-1]
            d_str+=", "
            d_str+=dict_str[e+2]
            d_str+="\\n"
    return d_str
d={3:2,5:6}
print(dict_to_str(d))

def dict_to_str1(d): #guerzhoy's '
    res = ""
    for k, v in d.items():
        res+=f"{k},{v}\n"
    return res[:-1] #excluding lastcharacter so that the last \n doesn't appear


#problem 5
L=[4,1,6]
L1=sorted(L)
def dict_to_str_sorted(d):
    d_str=dict_to_str(d)
    L=d_str.split(",")
    return sorted(L)
print(dict_to_str_sorted(d))

def dict_to_str_sorted1(d): #guerzhoy's'
    res=""
    sorted_keys = sorted(d.keys())
    for k in sorted_keys:
        res += f"{k}, {d[k]}/n"
    return res[:-1]
print(dict_to_str_sorted1(d))

#problem 6.a
def word_counts(dictionary):
    dict_split=open(dictionary, encoding="latin-1").read().split()
    dict_words = {}
    for e in range(len(dict_split)):
        if not dict_split[e] in dict_words:
            dict_words[dict_split[e]]=1
        else:
            dict_words[dict_split[e]]+=1
    return dict_words

def words_count1(dictionary):#guerzhoy (basically mine)
    words = open(dictionary, encoding="latin-1").read().lower().split() #so it doesn't distinguish betw capitalization
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word]=1
        else:
            word_counts[word]+=1
    return word_counts
print(words_count1("dostoyevskytext.txt"))

#6.b
def top_10(L):
    L_sort=sorted(L)
    return L_sort[len(L):len(L)-9:-1]

def top10(L): #guerzhoy
    return sorted(L)[:-10:-1] #from lowest (10) to highest(1)
print(top_10([1,2,3,4,5,6,7,89,4,3,2]))

#6.c
def top_words(file):
    words = word_counts(file)
    dict_sorted= sorted(words.items())
    L_new = []
    L_words_top10 = []
    for tuple in dict_sorted:
        L_new.append(tuple[1])
    L_new_10 = top_10(L_new)
    for top10val in L_new_10:
        for tuple in dict_sorted:
            if len(L_words_top10)==10:
                return L_words_top10
            if tuple[1] == top10val:
                if tuple[0] in L_words_top10:
                    break
                else:
                    L_words_top10.append(tuple[0])
    return L_words_top10

def top_10_most_freq(w_counts): #guerzhoy
    inv_counts =[]
    for k, v in w_counts.items():
        inv_counts.append((v,k)) #inversing the tuple so number goes first
    inv_counts_sorted=sorted(inv_counts)[::-1] #sort in reverse order
    res=[]
    for i in range(min(10, len(inv_counts_sorted))): #either go to 10 or to end oflist
        res.append(inv_counts_sorted[i][1])
    return res

w_counts = words_count1("prideandprej.txt")

print(top_10_most_freq(w_counts))
print(top_words("prideandprej.txt"))

#7: HTML (guerzhoy)




#9:
def CCC_results(file):
    results_split=open(file, encoding="latin-1").read().split("\n")
    list_of_results = []
    school_list=[]
    for e in range(len(results_split)):
        list_of_results.append(results_split[e].split(" "))
    for info_name in list_of_results:
        index=-1
        for element in info_name:
            if element.isupper() == True:
                index+=1
            else:
                school_list.append(info_name[index+1:])
                break
    for schools in range(len(school_list)):
        str_skl = ""
        for e in school_list[schools]:
            str_skl += e + " "
        school_list[schools] = str_skl
    print(school_list)
    for e in school_list:
        if e == "":
            school_list.remove(e)
    dict_skl = {}
    for e in range(len(school_list)):
        if not school_list[e] in dict_skl:
            dict_skl[school_list[e]]=1
        else:
            dict_skl[school_list[e]]+=1
    return dict(sorted(dict_skl.items(), key=lambda item:item[1], reverse=True))

