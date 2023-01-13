<<Problem 1  Answer>> 


# Given the string:
s = 'django'

# Use indexing to print out the following:
 print(s[0])
   'd'
 print(s[-1])
   'o'
 print(s[:4])
  'djan'
 print(s[1:4])
  'jan'
  print(s[4:])
   'go'


<<Problem 2 Answer>> 

# Given this nested list:
l = [3,7,[1,4,'hello']]

l[2].remove("hello")
i[2].append("goodbye")

l = [3,7,[1,4,'goodbye']]
 l[2][2] = "goodbye"

 print(l)

 
<<Problem 3 Answer>>

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}

print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d3['k1'][0]['nest_key'][1][0])


<<Problem 4 Answer>> 

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

 print(set(mylist))
 {1, 2, 3}


<<Problem 5 Answer>> 

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

 print("Hello my dog's name is {} and he is {} years old".format(name,age))
 Hello my dog's name is Sammy and he is 4 years old


                              #######################

