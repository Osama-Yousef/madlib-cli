  
    


from textwrap import dedent
import re  
   
def greeting_the_user():
    line_one = 'Welcome to madlibs game !!!!'
    line_two = 'You will be asked to input some words to play the game !!!'
    line_three = 'To exit the game please , type "quit"'

    print(dedent(f'''
        {'*' * 60}
        {line_one}
        {line_two}
        {line_three}
        {'*' * 60}
        '''))



def read_the_template():
    
    with open("assets/template.txt") as file:
        data = file.read()
        return data

def all_the_process(template):
    key_list = []
    end = 0

    repetitions = template.count('{')
    for i in range(repetitions):
        start = template.find('{', end) + 1
        end = template.find('}', start)
        key_value = template[start : end]

        key_list.append(key_value)   

    template = re.sub(r'\{.*?\}' , '{}' , template )
    print('template',template)







    # ask user to input 
    print('Now  enter your words!!!')

    words_out = []

    for i in range(len(key_list)):
        user_input = input(key_list[i] + ': ')
        if user_input == 'quit':
            exit()

        words_out.append(user_input)
    



    template = template.format(*words_out)
    print(template)

    ## to output the new template


    with open("assets/filled_template.txt", "w") as file:

        file.write(template)



if __name__ == "__main__":

    greeting_the_user()

    x  = read_the_template()
    
    all_the_process(x)












