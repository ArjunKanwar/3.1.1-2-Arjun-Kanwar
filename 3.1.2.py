x = input("Enter your name: ")
y = input("Enter your age: ")
print("Hello ", x)
print("You are ", y, "years old!")
print(type(x))
print(type(x))

a = int(3.14159)
b = str(8675309)
c = bool(0)
d = bool(1)
e = float(10)

print(a)
print(b)
print(c)
print(d)
print(e)

print(True) 
print(5==5) 
print(2+6==8) 
print(5==5) 
print(5>4) 
print(4<5)

# and operator 
sleep = 4         #Modify this number to see how it changes the output 
breakfast = False  #Modify this number to see how it changes the output 
print (sleep>=8 and breakfast==True) 

# or operator 
food = "cake"     #Modify this food to see how it changes the output 
print(food=="muffin" or food=="grapes") 

# not operator 
movie = "like"    #Modify this to say "dislike" to see how it changes the output 
print (movie=="like")

guesses = 4  # Change this number to see how the code output changes. 

if guesses >= 1: 
  x = int(input("pick a number:")) 
  if x < 5: 
    print("too low") 
  else: 
    print("too high") 
else: 
  print("You have run out of guesses!")