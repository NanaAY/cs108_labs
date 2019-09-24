'''A Python program that 
Created Spring 2018
lab06
@author: Nana Osei Asiedu Yirenkyi (na29) '''


#Exercise 6.2
empty_list = []

pets = ['dog']

toppings = ['bacon', 'cheese', 'onions', 'pepperoni']

green_eggs_and_ham = [ "i", "am", "sam", "sam", "i", "am", "that",
            "sam-i-am", "that", "sam-i-am", "i", "do", "not", "like", "that", "sam-i-am", "do",
            "you", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them",
            "sam-i-am", "i", "do", "not", "like", "green", "eggs", "and", "ham", "would", "you",
            "like", "them", "here", "or", "there", "i", "would", "not", "like", "them", "here",
            "or", "there", "i", "would", "not", "like", "them", "anywhere", "i", "do", "not",
            "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am",
            "would", "you", "like", "them", "in", "a", "house", "would", "you", "like", "them",
            "with", "a", "mouse", "i", "do", "not", "like", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would",
            "you", "eat", "them", "in", "a", "box", "would", "you", "eat", "them", "with", "a",
            "fox", "not", "in", "a", "box", "not", "with", "a", "fox", "not", "in", "a", "house",
            "not", "with", "a", "mouse", "i", "would", "not", "eat", "them", "here", "or", "there",
            "i", "would", "not", "eat", "them", "anywhere", "i", "would", "not", "eat", "green",
            "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would", "you",
            "could", "you", "in", "a", "car", "eat", "them", "eat", "them", "here", "they", "are",
            "i", "would", "not", "could", "not", "in", "a", "car", "you", "may", "like", "them",
            "you", "will", "see", "you", "may", "like", "them", "in", "a", "tree", "not", "in",
            "a", "tree", "i", "would", "not", "could", "not", "in", "a", "tree", "not", "in", "a",
            "car", "you", "let", "me", "be", "i", "do", "not", "like", "them", "in", "a", "box",
            "i", "do", "not", "like", "them", "with", "a", "fox", "i", "do", "not", "like", "them",
            "in", "a", "house", "i", "do", "not", "like", "them", "with", "a", "mouse", "i", "do",
            "not", "like", "them", "here", "or", "there", "i", "do", "not", "like", "them",
            "anywhere", "i", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not",
            "like", "them", "sam-i-am", "a", "train", "a", "train", "a", "train", "a", "train",
            "could", "you", "would", "you", "on", "a", "train", "not", "on", "a", "train", "not",
            "in", "a", "tree", "not", "in", "a", "car", "sam", "let", "me", "be", "i", "would",
            "not", "could", "not", "in", "a", "box", "i", "could", "not", "would", "not", "with",
            "a", "fox", "i", "will", "not", "eat", "them", "with", "a", "mouse", "i", "will",
            "not", "eat", "them", "in", "a", "house", "i", "will", "not", "eat", "them", "here",
            "or", "there", "i", "will", "not", "eat", "them", "anywhere", "i", "do", "not", "like",
            "them", "sam-i-am", "say", "in", "the", "dark", "here", "in", "the", "dark", "would",
            "you", "could", "you", "in", "the", "dark", "i", "would", "not", "could", "not", "in",
            "the", "dark", "would", "you", "could", "you", "in", "the", "rain", "i", "would",
            "not", "could", "not", "in", "the", "rain", "not", "in", "the", "dark", "not", "on",
            "a", "train", "not", "in", "a", "car", "not", "in", "a", "tree", "i", "do", "not",
            "like", "them", "sam", "you", "see", "not", "in", "a", "house", "not", "in", "a",
            "box", "not", "with", "a", "mouse", "not", "with", "a", "fox", "i", "will", "not",
            "eat", "them", "here", "or", "there", "i", "do", "not", "like", "them", "anywhere",
            "you", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like",
            "them", "sam-i-am", "could", "you", "would", "you", "with", "a", "goat", "i", "would",
            "not", "could", "not", "with", "a", "goat", "would", "you", "could", "you", "on", "a",
            "boat", "i", "could", "not", "would", "not", "on", "a", "boat", "i", "will", "not",
            "will", "not", "with", "a", "goat", "i", "will", "not", "eat", "them", "in", "the",
            "rain", "i", "will", "not", "eat", "them", "on", "a", "train", "not", "in", "the",
            "dark", "not", "in", "a", "tree", "not", "in", "a", "car", "you", "let", "me", "be",
            "i", "do", "not", "like", "them", "in", "a", "box", "i", "do", "not", "like", "them",
            "with", "a", "fox", "i", "will", "not", "eat", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "you",
            "do", "not", "like", "them", "so", "you", "say", "try", "them", "try", "them", "and",
            "you", "may", "try", "them", "and", "you", "may", "i", "say", "sam", "if", "you",
            "will", "let", "me", "be", "i", "will", "try", "them", "you", "will", "see", "say",
            "i", "like", "green", "eggs", "and", "ham", "i", "do", "i", "like", "them", "sam-i-am",
            "and", "i", "would", "eat", "them", "in", "a", "boat", "and", "i", "would", "eat",
            "them", "with", "a", "goat", "and", "i", "will", "eat", "them", "in", "the", "rain",
            "and", "in", "the", "dark", "and", "on", "a", "train", "and", "in", "a", "car", "and",
            "in", "a", "tree", "they", "are", "so", "good", "so", "good", "you", "see", "so", "i",
            "will", "eat", "them", "in", "a", "box", "and", "i", "will", "eat", "them", "with",
            "a", "fox", "and", "i", "will", "eat", "them", "in", "a", "house", "and", "i", "will",
            "eat", "them", "with", "a", "mouse", "and", "i", "will", "eat", "them", "here", "and",
            "there", "say", "i", "will", "eat", "them", "anywhere", "i", "do", "so", "like",
            "green", "eggs", "and", "ham", "thank", "you", "thank", "you", "sam-i-am"]


stop_words = [ "a", "able", "about", "across", "after", "all",
            "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be",
            "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does",
            "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have",
            "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is",
            "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most",
            "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or",
            "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so",
            "some", "than", "that", "the", "their", "them", "then", "there", "these", "they",
            "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when",
            "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you",
            "your" ]





#Exercise 6.1
print('length of green eggs and ham list:',len(green_eggs_and_ham)) 





def search(str_list, target): #function definition
    '''Searches through a given list for a given
     target and returns the index at which the target is found or returns -1 if 
     the target is not in this given list or the list is empty.'''
    
    i = 0
    for element in str_list:
        if element == target:
            return i 
        i += 1
    return -1



def test_search():  #function definition
    '''Tests the search() function defined above by calling
     it and printing the results'''
    
    print('\nTesting with empty list:',search(empty_list,'bacon'))
    print('Testing with invalid target:',search(toppings, 'dog'))
    print('Testing with valid target:',search(green_eggs_and_ham,'good'))
    print('Testing with valid target:',search(toppings, 'cheese'))
    
    




def longest_and_shortest(str_list):
    '''receives a list of words and prints the length 
    of the shortest and the longest word in the list.
                ALGORITHM
    initialize the variables 'longest' and 'shortest' to the first words of the given list
    loop for each string in list
    if length of string > length 'longest', make 'longest' refer to the current string
    and if length of string < length 'shortest', make 'shortest' refer to the current string
    '''
    if str_list == []:
        print('\nThe given list was empty.')
    else:
        longest = str_list[0]
        shortest = str_list[0]
        for element in str_list:
            if len(element) > len(longest):
                longest = element
            if len(element) < len(shortest):
                shortest = element
        print('\nLongest word is:',longest)
        print('Shortest word is:',shortest)
        
        
def test_longest_and_shortest():
    print('\nTests....')
    longest_and_shortest(toppings)
    longest_and_shortest(pets)   
    longest_and_shortest(empty_list)
    





def count_words_not_present(list_1,list_2):
    '''Receives two lists of words and returns the number of words in the first list that are not in the second list
    initialize count to 0
    loop for each word in list 1 
    loop for each word in list 2 
    if both words are the same, increment count'''
    count = 0
    for item in list_1:
        for word in list_2:
            if item == word:
                count += 1
    print(count)
    
    
def test_count_words_not_present():
    print('\nTesting count_words_not_present...\n',count_words_not_present(empty_list, pets))
    print(count_words_not_present(empty_list, toppings))
    print(count_words_not_present(pets, toppings))






def green_eggs_and_ham_analysis():
    '''Goes through the green eggs and ham list and prints
     out an index for the words "i", "boat", "fox","thank","book"'''
    print('\nIndex for "i":',search(green_eggs_and_ham,'i'))
    print('Index for "boat":',search(green_eggs_and_ham,'boat'))
    print('Index for "fox":',search(green_eggs_and_ham,'fox'))
    print('Index for "book":',search(green_eggs_and_ham,'book'))
    longest_and_shortest(green_eggs_and_ham)
    count_words_not_present(green_eggs_and_ham, stop_words)
    
    
    



# def count_unique_words(str_list):
#     '''counts the number of unique words in the text'''
#     count = 0
#     unique_words = []
#     for word in str_list:
#         if word not in uniqueWords:
#             unique_words.append(word)
#             count += 1
#     return count
# 
# 
# def test_count_unique_words():
#     
    
    
    
#calling the test function   
test_search() 
green_eggs_and_ham_analysis()    
test_longest_and_shortest()
test_count_words_not_present()