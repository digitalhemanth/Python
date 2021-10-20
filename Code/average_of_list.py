


def Average(lst):
    print("----------------- The List Items ----------------- ")
    for i in lst:
        print(i)
    print("----------------- The List Details ----------------- ")
    sum_of_list = sum(lst)
    print ("Sum of the List is :  ", sum_of_list)
    len_of_list = len(lst)
    print ("Length of the List is :  ", len_of_list)
    #Avg = sum(lst) / len(lst)
    Avg = sum(lst) / len(lst)
    print("Average of the list =", round(Avg, 2))

def list_item():
    global lst
    lst=[]
    check = 'y'
    while check == 'y':
       check = input("Do you want to add more items ? Y/N ")
       if check == 'y':
          item=int(input("Enter item : "))
          lst.append(item)
       else:
            check = 'N'
    else:
       Average(lst)

list_item()
