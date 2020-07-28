my_list = ['apples', 'bananas', 'tofu', 'cats']
my_list2 = [1, 2, 4, "cats"]
my_list3 = [1]
my_list4 = []
# List -> String
# Given a list, produce a string consisting of each element 
# of the list followed by an ',', with 'and' inserted before the last item
def comma_code(my_list):
    if len(my_list) == 0:
        print("")
    elif len(my_list) == 1:
        print(str(my_list[1]))
    else:
        for i in range(len(my_list) - 2):
            print(str(my_list[i]) + ',', end=' ')
        print(str(my_list[-2]) + ' and ' + str(my_list[-1]))
    
comma_code(my_list)
              
                   
    

