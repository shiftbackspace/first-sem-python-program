# # # # # def add():
# # # # #     x=10
# # # # #     y=20
# # # # #     c=x+y
# # # # #     print(c)
# # # # # add()


# # # # def login(username,password):
# # # #     print(f"your user name is: {username} and your password is: {password}")
# # # # login("sunil","battle")                                                    





# # # def login(username,email,adress,phoneno,password):
# # #      print(f"username is: {username} , email is:{email} , adress is:{adress} , phoneno is:{phoneno} and your password is {password} ")
# # # login("abhay","sah86148@Gmail.com","9825975857","tinkune","abhay123")

# # def sum():
# #     a=[1,2,3,4]
# # sum=0
# # for i in "a":
# #     sum=sum+i
# #     print(sum)



# def show (name,age):
#     print(f"name: {name} age: {age}")
# show(name="sunil" , age=20)


def show(*num):
    z=num[0]+num[1]+num[2]
    print(z)
show(5,4,3)
