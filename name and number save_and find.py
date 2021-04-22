n = int(input("How many name and number you want to save in your phone\n "))
i = 0
save = dict()
while(i < n):
    name , number = input("enter name and number\n").split()
    save[name] = number
    i+=1
while True:
    check_name  = input("enter the name which number you save ") 
    val = save.get(check_name,0)
    if val != 0:
        print(check_name + "=" + save[check_name])
    else:
        print("Not found")
