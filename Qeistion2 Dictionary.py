sentence = input('enter your sentences: ') # prompt user to enter sentence 
my_list = sentence.split() # change sentence into list of strings
my_dict = dict() # initialize empty dictionary
def lst_to_dic(): # function changing list into dictionary
    for string in my_list: # iterate through string 
        my_dict[string] = my_dict.get(string,0)+1 # forming dictionary of string as key and frequency as value 
    print(my_dict)
lst_to_dic() # function call