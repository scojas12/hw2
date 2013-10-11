# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

n = 100

total = 0

i = 1

while i <= n :

    total = total + i
   
    i = i + 1

print total
# ... write your code and comments here (and remove this line)


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

T = range(2,11)

for i in T:
   
    print 1.0/i

# ... write your code and comments here (and remove this line)


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0

for i in range(1,n+1):
    
    triangular = triangular + i

print triangular

print n*(n+1)/2

# ... write your code and comments here (and remove this line)

###
### Problem 4
###

n = 10

total = 1

for i in range ( 1 , n + 1 ) :

	total = total * i

print total

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10

total = 1

for i in range ( 1 , n + 1 ) :

	total = total * i

print total

# ... write your code and comments here (and remove this line)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

n = 10

while n > 0:

	total = 1

	for i in range ( 1 , n + 1 ) :

		total = total * i

	print total
	n = n - 1

# ... write your code and comments here (and remove this line)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

n = 1

total2 = 1.0

while n <= 10:

	total = 1

	for i in range ( 1 , n + 1 ) :

		total = total * i

	total2 = total2 + ( 1.0 / total)
	n = n + 1

print total2

# ... write your code and comments here (and remove this line)

###
### Collaboration
### Russ and Ian

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
