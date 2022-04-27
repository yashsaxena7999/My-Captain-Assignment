import operator
string1 = input("Enter a string : ")
def most_frequent(string1):
    d = dict()
    for i in string1:
        if i not in d:
            d[i] = string1.count(i)
    return sorted(d.items(), key=operator.itemgetter(1), reverse=True) 
    
res = most_frequent(string1)
print(res)