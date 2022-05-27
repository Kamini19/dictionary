                                                                                                                                
                                                                                                                                \0   #  i=1
# a=0
# b=1
# print(a)
# print(b)
# for i in rang63 (2,100) :
#     c=a+b
#     a=b
#     b=c
#     print(c)

# x=str(input("Enter the name :"))
# for i in x :
#     print(i)

# i=1
# while i<=20 :
#     print(i**2)
#     i=i+1  

# i=0 
# a=int(input("enter the number:"))
# while i<a:
#     z=(a//10)%10
#     i=i+1
# print(z)

# i=1
# a=int(input("enter the number :"))
# while i<=10 :
#     print(i*a)
#     i=i+1



# i=int(input("enter starting number: "))
# num=int(input("enter ending number: "))
# while i<=num:
#     if i%2==0:
#         print(i)
#     i+=1



# a=int(input("enter the number:"))
# i=1
# sum=0
# while a>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
#     a=a//10
#     if i==sum:
#         print("amstrong number")
#     else:
#         print("not amstrong")


# n=int(input("enter the number:"))
# i=1
# sum=0
# while i<=1:
#     a=n%10
#     b=n//10
#     c=n//10
#     a=a** 3 
#     b=b**3
#     c=c**3
#     sum=a+b+c
#     i=i+1
# if sum==n:
#     print("amstrong")
# else:
#     print("not amstrong")




# i=10
# while i>0:
#     print(i)
#     i-=1


# num=int(input("enter the digit: "))
# sum=0
# while num>0:
#     r=num%10
#     # print(r)
#     sum=sum+r
#     # print(sum)
#     num=num//10
#     # print(num)
# print(sum)

# i=1
# while i<10:
#     print(i,i**2)
#     i+=1


# i=1
# while i<=10:
#     print(i,"whole number")
#     print(i,"natural number")
#     if i%2==0:
#         print(i,"even")

#     else:
#         print(i,"odd")
#     i+=1



# i=1
# while i<10:
#     print(i*10)
#     i=i+1


# i=0
# while i<=10:
#     i=i+1
#     if i==5 :
#         continue
#     print(i) 

# i=0
# while i<=10 :
#     i=i+1
#     if i==5:
#         break
#     print(i) 



# a=int(input("Enter the number:"))
# a,b=0,1
# i=0
# while i<a:
#     if b==0:
#       print(b)
#     a,b=b,a+b
#     i=i+1


# a=0
# b=1
# while b<=100:
#     print(b)
#     a,b=b,a+b



# a=input("enter the number :")
# i=0
# while i<len(a):
#     if a[i]==str(0):
#         print("zero",end=" ")
#     elif a[i]==str(1) :
#         print("one",end=" ")
#     elif a[i]==str(2) :
#         print("two",end=" ") 
#     elif a[i]==str(3) :
#         print("three",end=" ")
#     elif a[i]==str(4):
#         print("four",end=" ")   
#     elif a[i]==str(5):
#         print("five",end=" ")     
#     elif a[i]==str(6):
#         print("six",end=" ")
#     elif a[i]==str(7) :
#         print("seven",end=" ")
#     elif a[i]==str(8) :
#         print("eight",end=" ")
#     elif a[i]==str(9) :
#         print("nine",end=" ")                
#     i=i+1


# i=1500 
# while i<=2700 :
#     if i%7==0 and i%5==0 :
#         print(i)
#     i=i+1


# num = int(input("enter a number: "))
# factorial =1
# i=1
# while i<=num:
#     factorial=factorial*i
#     # i= i+1
#     print(factorial)
#     i=i+1


# a= int(input("Enter a guess :"))
# while (a>9) or (a<1) :
#      a=int(input("Enter a guess :"))
# else:
#    print("Well guessed")

# x=int(input("enter the number :"))
# i=0
# a=1
# b=1
# sum=0
# while i<=x :
#     print(sum,end=" ")
#     a=b
#     b=sum
#     sum=a+b    
#     i=i+1

# num=int(input("Enter a number: "))
# sum=0
# x=num
# while x>0:
#    y= x%10
#    sum+=y** 3
#    x//=10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

# i=10
# while i>0 :
#     print(i,"natural number")
#     i=i-1


# for i in range(1,5):
#     for j in range(1,5):
#      if j<=i:
#       print("*",end=" ")
#     print()



# sum=0
# i=1
# while i<=10 :
#     print(i)
#     sum+=i
#     i=i+1
#     print(sum)

# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)

# i=1
# sum=0
# while i<=10 :
#     if i%2==0:
#         print(i)
#         sum=sum+i
#     i+=1
# print("sum=",sum)


# n=int(input("enter the  number"))
# i=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1



# num = int(input("enter the number :"))
# i=1
# while i<=num:
#     if num%i==0:
#         print(i)
#     i= i+1
# print(num) 



# n=int(input("enter the number :"))
# i=1
# sum=0
# while i<=0 :
#     a=(n%10)
#     b=(n//10)%10
#     c=(n//100)%10
#     i=i+1
#     sum=a+b+c
# if sum%n :
#     print("it is harshad number")
# else :
#     print("it is not harshad number")


# i=0 
# s=0 
# while i<10:
#    n=int(input("enter the number :")) 
#    s=s+n 
#    i+=1 
# avg = s/10 
# print("The sum is = ",s)
# print("The average is =",avg)

# n=int(input("enter the number :"))
# for i in range (n) :
#     for j in range (i+1) :
#         print(j+1,end=" ")
#     print() 


# n=int(input("enter the number :"))
# i=1
# while (i<=n):
#     j=1
#     while (j<=i):
#         print(j,end=" ")
#         j+=1
#     print()
#     i=i+1    

# n=int(input("enter the number :"))
# i=1
# while i<=n:
#     j=1
#     while j<=10:
#         print(j,"=",j*i)
#         j+=1
#     print()
#     i=i+1            



# i=5
# while i>=1 :
#     b=5-i 
#     while b>0 :
#         print("",end="")
#         b=b-1 
#     j=1
#     while j<=i :
#         print(j,end="")
#         j=j+1
#     print()
#     i=i-1    

# i=1
# while i<=5 :
#     b=5-i
#     while b>0 :
#         print("",end="")
#         b=b-1
#     j=1
#     while j<=i :
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1       


# i=5
# while i>=1 :
#     b=5-i
#     while b>0 :
#         print("",end="")
#         b=b-1
#     j=1
#     while j<=i :
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1       

# i=5
# while i>=1 :
#     b=5-i
#     while b>0 :
#         print(" ",end=" ")
#         b=b-1
#     j=1
#     while j<=i :
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1       



# i=1
# while i<=5 :
#     b=5-i
#     while b>0 :
#         print(" ",end=" ")
#         b=b-1
#     j=1
#     while j<=i :
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1       


# i=1
# while i<=5 :
#     b=5-i
#     while b>0 :
#         print(" ",end="")
#         b=b-1
#     j=1
#     while j<=i :
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1       



# i=5
# while i>=1 :
#     b=5-i 
#     while b>0 :
#         print("",end="")
#         b=b-1 
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i-1    



# i=1
# while i<=10:
#     b=5-i
#     while b>0:
#         print("",end="")
#         b=b-1
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+2
#     print()
#     i=i+2


# i=10
# while i>=1:
#     b=5-i
#     while b>0:
#         print("",end="")
#         b=b-1
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+2
#     print()
#     i=i-2
 


# i=1
# while i<=5:
#     b=5-i 
#     while b>0 :
#         print("",end=" ")
#         b=b-1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print() 
#     i=i+1   
# i=5
# while i>=1:
#     b=5-i 
#     while b>0 :
#         print("",end=" ")
#         b=b-1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print() 
#     i=i-1 



# i=1
# while i<=4 :
#     j=1
#     while j<=5 :
#         print(j,end=" ")
#         j=j+1
#     print( )
#     i=i+1        

# i=1
# while i<=5 :
#     j=1
#     while j<=5 :
#         print(i,end=" ")
#         j=j+1
#     print( )
#     i=i+1        

# i=1
# while i<=4 :
#     b=5-i 
#     while b>0 :
#         print(" ",end=" ")
#         b=b-1 
#     j=1
#     while j<=i :
#         print(" ",end=" ")
#         j=j+1    
#     print()
#     i=i+1


# i=5
# while i>=1:
#     b=5-i 
#     while b>0 :
#         print("",end=" ")
#         b=b-1
#     j=1
#     while j<=i :
#         print("#",end=" ")
#         j=j+1
#     print( )
#     i=i-1  




# x=1
# i=1
# while i<=5 :
#     j=1
#     while j<=5-i :
#         print(" ",end=" ")
#         j=j+1
#     b=1
#     while b<=x :
#         print(i,end=" ")
#         b=b+1
#     x=x+2 
#     print()
#     i=i+1 

# i=1
# while i<=5 :



#     j=1
#     while j<=5-i :
#         print("",end="")
#         j=j+1
#     b=1
#     while b<=i :
#         print(i,end=" ")
#         b=b+1 
#     print( ) 
#     i=i+1   

# n=int(input("Enter the number of rows :"))
# k=ord("A")
# for i in range (n) :
#     for j in range (i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()    



# n=int(input("Enter the Number of Rows :"))
# count=1
# for i in range (1,n+1) :
#     for j in range (1,i+1) :
#         print(count%2,end=" ")
#     print() 
#     if i%2==0 :
#         count=1
#     else :
#         count=0  




# x=str(input("enter the number :"))
# i=0
# for i in x :
#     print(i)


# x=str(input("enter the number :"))
# i=0
# while  :
#     i=i+1
#     print(i)

# i=0
# sum=0
# while i<5 :
#     a=int(input("enter the weight :"))
#     sum=sum+a 
#     i=i+1
#     avg=sum/10
# print("the sum=",sum)
# print("the avg=",avg)    



