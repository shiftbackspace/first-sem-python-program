# # # # # from re import X


# # # # # y=10
# # # # # def outer():
# # # # #     z=4
# # # # #     def inner():
# # # # #         x=4
# # # # #         nonlocal  z
# # # # #         z=z+1
# # # # #         print(x)
# # # # #         print("inside the function y", y)
# # # # #     inner()
# # # # #     print("z:", z)
# # # # # outer()        



# # # # y=10
# # # # def inner():
# # # #     x=4
# # # #     print(x)
# # # #     print("inside the function y", y)
# # # # print("y:", y)
# # # # inner()   



# # # def outer():
# # #     x="local"
# # #     def inner():
# # #         nonlocal x
# # #         x="nonlocal"
# # #         print("inner:", x)
# # #     inner()
# # #     print("outer:", x)
# # # outer()




    
# # result=lambda n1, n2, n3: n1 + n2 + n3
# # print("sum of three values :", result(10, 20, 25)

# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)

data=[1,2,3,4,5,6,6,7,9,10]
var=list(filter(lambda x: x%2==0 , data))
print(var)