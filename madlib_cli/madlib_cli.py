  
    


# from textwrap import dedent
# import re  
   
# def greeting_the_user():
#     line_one = 'Welcome to madlibs game !!!!'
#     line_two = 'You will be asked to input some words to play the game !!!'
#     line_three = 'To exit the game please , type "quit"'

#     print(dedent(f'''
#         {'*' * 60}
#         {line_one}
#         {line_two}
#         {line_three}
#         {'*' * 60}
#         '''))



# def read_the_template():
    
#     with open("assets/template.txt") as file:
#         data = file.read()
#         return data

# def all_the_process(template):
#     key_list = []
#     end = 0

#     repetitions = template.count('{')
#     for i in range(repetitions):
#         start = template.find('{', end) + 1
#         end = template.find('}', start)
#         key_value = template[start : end]

#         key_list.append(key_value)   

#     template = re.sub(r'\{.*?\}' , '{}' , template )
#     print('template',template)







#     # ask user to input 
#     print('Now  enter your words!!!')

#     words_out = []

#     for i in range(len(key_list)):
#         user_input = input(key_list[i] + ': ')
#         if user_input == 'quit':
#             exit()

#         words_out.append(user_input)
    



#     template = template.format(*words_out)
#     print(template)

#     ## to output the new template


#     with open("assets/filled_template.txt", "w") as file:

#         file.write(template)



# if __name__ == "__main__":

#     greeting_the_user()

#     x  = read_the_template()
    
#     all_the_process(x)


import re  # for regex 

def read_template():
    """
    Returns the template.txt file 
    """
    file = open("assets/template.txt",'r')
    content = file.read()
    return content

def parse(constant): # constant refers to the text
    """
    Returns a list of words inside {} in a given text
    Arguments:
        constant {string} -- text contains words inside {}
    Output:
        lst {list of string} -- the words inside {} 
    """
    lst=[]
    res = re.findall(r'\{.*?\}', constant) # to find all the curly braces which have value inside it too then put all of them and their values inside res
    for i in res:
        lst.append(i.strip("{ }"))    # to remove every value in curly braces ,and get empty curly braces 
    return lst

def merge(constant , words):  

    """
    Returns a string with user input strings
    Arguments:
        constant {string} -- text contains empty {}
    Output:
         {string} -- replacing {} to words from the user 
    """
    lst = parse(constant)  # constant is the parsed text which has text and empty{} to put things inside curly braces in te step below
    
    return (re.sub(r' {[^}]*}',' {}',constant)).format(*words) # we use string.format() to give the string text which have text and empty curly braces values one by one from the values in format 
                                            # we put * before the name of array so it will take elements one by one in the array which is (words), then put each value into empty braces

def copyFile(text):
    print(text)
    file = open('assets/filled_template.txt','w')
    file.write(text)

# here the execting happen
if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("You will be asked to input some words to play the game !!!")
    content = read_template()
    lst = parse(content)
    words=[]
    for i in range(len(lst)):
        words.append(input("enter a {} ".format(lst[i])))
    toCopy = merge(content, words)
    copyFile(toCopy)












