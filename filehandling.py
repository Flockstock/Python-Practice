def count_words(textfile):
    with open('textfile.txt','r')as file:
        text = file.read()
        return(len(text.split()))
print(f"Total words in a file: {count_words('textfile.txt')}")
    # with open('textfile.txt')as file:
#     text = file.read()
#     print(len(text.split()))


# def count_lines(textfile):
#     with open('textfile.txt','r') as file:
#         print(sum( 1 for s in file))
# print(count_lines('textfile.txt')Write a function which count number of lines and number of words in a text. All the files are in the data the folder:)
#
# def count_lines(textfile):
#     with open('textfile.txt','r') as file:
#         return sum( 1 for s in file) # here we need the result later hence return is used.
# print(count_lines('textfile.txt'))






# text_file = open('text.txt')
# # to count the number of lines in a file
# print(len(text_file.readlines()))








# import csv
# with open("office_dataset.csv") as f:
#     csv_file = csv.reader(f, delimiter=',')
#     print("Contents are:")
#      line_count = 0
#     for row in csv_file:
#             if row :
#                 print(f'{" - ".join(row)}')
#             else:
#                 print(
#                     'No record available'
#                 )
        #         line_count += 1
        #     print(f'number of lines are:',{line_count})
            
     

   




# expenses = []

# for i in range(5):
#     product = input("What did you buy?:   ")
#     cost = float(input("How much did it cost?: "))
#     category = input("Category?: ")

   
#     expenses.append([product,cost,category])
#     print("----Expense Recorded--")
#     print(expenses)
    
       
