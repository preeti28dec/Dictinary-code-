# def count_letters(text):
#       result = {}
#       for letter in text:
#         if letter not in result:
#           result[letter.lower()] = 1
#         else:
#           result[letter.lower()] += 1
#       return result
# print(count_letters(input("enter any name and any thing\n")))


string = input("enter any santence or word\n")
count = {}
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print ("Count of all characters in user input is :\n "+  str(count))