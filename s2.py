#write a python function using lambda function to check a every element of a list is an integer or string.
arr = [10,501,22,37,100,999,87,351] 
v = 10
def x(arr, v): return arr.count(v) 
if(x(arr, v)): 
	print("Element is an integer") 
else: 
	print("Element is a string")
