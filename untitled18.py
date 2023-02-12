#Write a program to find all pairs of an integer array whose sum is equal to a given number
def getCount(arr, n, sum):
  
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
  
    return count
  

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getCount(arr, n, sum))

#Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 

A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
#Write a program to check if two strings are a rotation of each other?

def checkRotation(s1, s2): 
    temp = '' 
  
    
    if len(s1) != len(s2): 
        return False
    temp = s1 + s1 
  
    if s2 in temp: 
        return True 
    else: 
        return False
  
 
string1 = "HELLO"
string2 = "LOHEL"
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")
    
    
#Write a program to print the first non-repeated character from a string?
def RepeatingFunc(myStr):
	char_order = []
	counts = {}

	for c in myStr:
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1
			char_order.append(c)
	for c in char_order:
		if counts[c] == 1:
			return c
	return None

print("First Non-Repeating Character = ",RepeatingFunc('thisisit'))

#Read about the Tower of Hanoi algorithm. Write a program to implement i

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
 

N = 3
 
TowerOfHanoi(N, 'A', 'C', 'B')

# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
	stack = []
	
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
		
			stack.append(prefix[i])
			i -= 1
		else:
		
			
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

if __name__=="__main__":
	str = "*-A/BC-/AKL"
	print(prefixToInfix(str))
    
    
    
    
#Write a program to check if all the brackets are closed in a given code snippet.


def areBracketsBalanced(expr):
	stack = []

	
	for char in expr:
		if char in ["(", "{", "["]:

			
			stack.append(char)
		else:

			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	if stack:
		return False
	return True



if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")

#Write a program to find the smallest number using a stack.




class MinStack:


	def __init__(self):
		self.s = []

	class Node:
		def __init__(self, val, Min):
			self.val = val
			self.min = Min

	def push(self, x):
		if not self.s:
			self.s.append(self.Node(x, x))
		else:
			Min = min(self.s[-1].min, x)
			self.s.append(self.Node(x, Min))

	def pop(self):
		return self.s.pop().val

	def top(self):
		return self.s[-1].val

	def getMin(self):
		return self.s[-1].min

s = MinStack()

s.push(-1)
s.push(10)
s.push(-4)
s.push(0)
print(s.getMin())
print(s.pop())
print(s.pop())
print(s.getMin())



    
    