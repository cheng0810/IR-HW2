
# coding: utf-8

# In[1]:


import numpy as np

"""
open the submission file and put the document name into a 2-dimension array
"""
sub = np.zeros((16,2265+1),dtype = object)
query = []
answer = open('C:/Users/Cheng/Desktop/jupyter/IRHomework2/submission.txt')
answer.readline()
for i in range(16):
    query = answer.readline().replace(',',' ').split(' ')
    del query[-1]
    sub[i] = query

"""
use a for loop to calculate every query's solution
del the '\n' and the query name
after compare the solution and submission 
put the location into an array and sort the answer because the MAP formula
(we cant cal the MAP if denominator(分母) is not sorted)
"""
query = []
MAP =[]
answer = open('C:/Users/Cheng/Desktop/jupyter/IRHomework2/solution.txt')
answer.readline()
for k in range(16):
    query = answer.readline().replace(',', ' ').split(' ')
    del query[-1]
    del query[0]

    no = []
    for i in range(len(query)):
        for j in range(2265+1):
            if(query[i] == sub[k][j]):
                no.append(j)

    no.sort() 
    precision = 0    
    for i in range(len(no)):
        precision += (i+1)/no[i]

    precision = precision/len(no)
    MAP.append(precision)

"""
cal the final MAP and the answer is 0.11724788124480491
"""
ans = 0
for i in range(16):
    ans += MAP[i]

ans = ans/16
print(ans)
    

