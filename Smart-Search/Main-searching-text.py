#Author: Tirtha Subedi
#UserName: Subedit
# Purpose:  This sample function opens a file with the name words_file_name
#   reads the text, converts everything to lowercase and returns a list
#   of the words.

import time


def linearsearch():     # this is for the linear search
    b= input("insert a file name")
    userfile= open(b, "r")
    target= input("what do you want to search?")
    count=0
    start_time= time.time()
    e= userfile.readlines()
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
    for i in punctuation:
        for j in range(len(e)):
            e[j] = e[j].replace(i,"")
    for i in range(len(e)):
            e[i].lower()

    for lines in e:
        a= lines.split()
        # print(a)
        for word in a:
            if target == word:
                count +=1
    print (count)
    end_time= time.time()
    print(end_time - start_time)

def binarysearch():
    b= input("insert a file name")
    userfile= open(b, "r")
    target= input("what do you want to search?")

    count=0
    readtext=userfile.readlines()

    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
    for i in punctuation:
        for j in range(len(readtext)):
            readtext[j] = readtext[j].replace(i,"")

    for i in range(len(readtext)):
        readtext[i].lower()
    lists=[]

    for lines in readtext:
        lines.split()
        print(lines)
    sortlist= sorted(readtext)
    print(sortlist)

    first=0
    last= len(readtext)-1

    while first<=last:
        mid=(first + last)
        text= readtext [mid]
        if target == text:
            return mid
        elif target < text:
            last=mid - 1
        else :
            first= mid + 1
            return -1

      # print(readtext)
    # listtext=[]
    # a = readtext.split()
    # readtext.sort()
    # print(listtext)

    # for lines in readtext:
    #     lines.lower()
    #     listtext.append(lines.split())
    # print (listtext)
    # # print ('test', sorted(listtext))
    # # listtext=listtext.lower()
    # listtext.sort()
    # print(listtext)



    # for text in readtext:
    # #     mid =  userfile[len(readtext)/2]
    # #     print(mid)
    # #
#  first = 0
# 3	    last = len(alist)-1
# 4	    found = False
# 5
# 6	    while first<=last and not found:
# 7	        midpoint = (first + last)//2
# 8	        if alist[midpoint] == item:
# 9	            found = True
# 10	        else:
# 11	            if item < alist[midpoint]:
# 12	                last = midpoint-1
# 13	            else:
# 14	                first = midpoint+1
# 15
# 1	    return found




def main():

    typeofsearch=input("What type of search you want to do? Linear or Binary")

    while typeofsearch != "Binary" or typeofsearch != "Linear":

        if typeofsearch =="Binary" or typeofsearch== "binary":
            return binarysearch()

        if typeofsearch=="Linear" or typeofsearch=="linear":
            return linearsearch()

        typeofsearch=input("Try again using correct word binary or linear")


    # else:
    #    while  typeofsearch != "Linear" or typeofsearch!= "Binary":
    #          typeofsearch=input("try again using binary or linear ")

        # return typeofsearch
    #     print("Please type Linear or Binary correctly!")
    #     # return type_search



    # a=type_search()  #function for type of search linear or binary.
    # b= input("insert a file name")
    # userfile= open(b, "r")
    # target= input("what do you want to search?")
    #
    # linearsearch()
    #
    # binarysearch()
main()
