"""
Author: Ilja Lom...
Publication-Date: 10/09/2021
Description: 
    A matching algorithm to find the total number of perfect matchings of basepair edges possible for a bonding graph for a sequence of RNA

    This application assumes that there are equal numbers of adenine and uracil, and, guanine and cytosine.
"""

#Initialising variables
matchings = 0 #Number of perfect matches possible

#This is the RNA sequence
RNA_sequence = input("---Enter the RNA sequence:---\n---")

#Calculating the number of specific nucleotides in the sequence
a = RNA_sequence.count('A')
u = RNA_sequence.count('U')
g = RNA_sequence.count('G')
c = RNA_sequence.count('C')

#Factorial processing
def factorial(bases):
    fact = 1 #If set to 0 the multiplier will always be 1 less. E.g, instead of '2x1', it would be '1x0'
    for i in range(bases):
        fact *= (i + 1) #i+1 because i starts at 0. Forms a recursion sequence
    return(fact)

#Checking whether the sequence permits complete complementary pairing
if (a==u and g==c):
    #Calculating the total number of matchings possible
    matchings = factorial(a) * factorial(g) 
    print(f"---The number of perfect matching permutations possible: {matchings}---")
else:
    print("---There is an uneven number of nucleotides---\n---Cannot perform a perfect matching---")





















