#-------------------------------------------------------------------------------
# Name:        read_words_function.py
# Purpose:  This sample function opens a file with the name words_file_name
#   reads the text, converts everything to lowercase and returns a list
#   of the words.
#
# Author:       various online sources cited in the comment above function
#
# Originally created:     25/08/2014
#-------------------------------------------------------------------------------
import time
## This function is adapted from
##  http://stackoverflow.com/questions/13259288/returning-a-list-of-words-after-reading-a-file-in-python
## with exception handling built into it. Also integrated is a method to
## strip punctuation usingideas/code from
##      http://stackoverflow.com/questions/19414161/removing-punctuation-in-lists-in-python
def read_words(words_file_name):
    '''This function opens a file with the name in 'words_file', reads in
    the contents and returns a list of the words, stripped of whitespace.
    pre: none, as this function handles IOError for when the file is not there gracefully
    post: returns the list of words in the file, which is empty on an open fail. '''
    words_list =[]
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readlines()

        # replace punctuation with a blank space
        punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
        for i in punctuation:
            for j in range(len(contents)):
                contents[j] = contents[j].replace(i,"")

        for i in range(len(contents)):
            contents[i].lower()
            words_list.extend((contents[i].lower()).split()) # puts words into list
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    return words_list

def linear_search(input_words, target):      # this function goes through a list and find the specific item and returns how many it
    '''
    :param target: This is the item of the list that i am looking for
    :param words_list: this is stores the list of words  are in the file text
    :return: the function returns the variable that holds how many times each words occurs in the list
    '''

    linear_searchtime= time.time()          # this is to record time
    count = 0
    for word in input_words:                # searching linearly
        if target == word:
            count +=1
    print('Linear count is ',count)
    linear_searchend= time.time()
    total_searchtime= linear_searchend - linear_searchtime          # To calculate the total time
    print("The total linear search time is ",  total_searchtime, "second")

def binary_search(input_words, target):
    '''
    :param item: This is stores the target word that I am trying to find
    :param mylist: this holds the sorted list that I am looking through
    :return: This returns the number of times that each item occurs in the list
    '''
    # this functions searches a lists and divides until it finds the item it is looking for

    befor_sort=time.time()                      #tracking time before sorting
    input_words.sort()                              # this sort input words
    after_sort=time.time()                      #tracking time after sorting
    # print(input_words)
    my_list =[]
    first = 0                                           # this is starting from left
    last = len(input_words)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2                        # this is doing binary which is by dividing by 2
        if input_words[midpoint] == target:
            if input_words[midpoint -1] != target:
                found = True
                my_list.append(midpoint)                    # adding to mylist
            else:
                last = midpoint -1
        elif target < input_words[midpoint]:
            last = midpoint-1

        else:
            first = midpoint+1
    # print(my_list)
    low = 0                                             # here searching from right
    high = len(input_words)-1                            # this is tracking length of word from bottom
    Found = False
    while low<=high and not Found:
        mid = (low + high)//2                                       # doing binary by dividing by 2
        if input_words[mid] == target:
            if input_words[mid + 1] != target:
                Found = True
                my_list.append(mid)
            else:
                low = mid + 1
        elif target < input_words[mid]:
            high = mid-1

        else:
            low = mid+1

    if len(my_list)==0:
        print("Word you are searching for Not Found")
    else:
        count= my_list[1]- my_list[0]+1                             # here is counting number of target that are found
        print("Binary search is", count)

    end_time=time.time()                                         # tracking time
    total_timebefore=end_time - befor_sort                      # tracking before sorting time
    total_timeafter= end_time - after_sort
    print("Time before sort {0} seconds and the time after sorting is {1} seconds". format(total_timebefore, total_timeafter))



def main():
    '''a simple main() driver'''
    input_words = read_words("war_and_peace.txt") # Change this line or use input for the filename
    # print(input_words)
    target=input("what do you want to search?")    # this is target or a word that user want to search for
    linear_search(input_words, target)              # calling function here
    binary_search(input_words, target)

main()
