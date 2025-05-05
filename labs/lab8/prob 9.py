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
                school_list.append(info_name[index+1:len(element)-2])
                break
    for schools in range(len(school_list)):
        str_skl = ""
        for e in school_list[schools]:
            str_skl += e + " "
        school_list[schools] = str_skl
    print(school_list)
    dict_words = {}
    for e in range(len(school_list)):
        if not school_list[e] in dict_words:
            dict_words[school_list[e]]=1
        else:
            dict_words[school_list[e]]+=1
    return dict_words



print(CCC_results("ccc2022.txt"))