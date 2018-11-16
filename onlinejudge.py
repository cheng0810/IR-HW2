
# coding: utf-8

# In[9]:


query_num = int(input())

query = [ ]
for i in range(query_num):
        sol = input().replace(',',' ')
        query.append(sol)

doc = [ ]   
for i in range(query_num):
        sub = input().replace(',',' ')
        doc.append(sub)
        
avg = 0.000

MAP = [ ]

for i in range(query_num):
    query_t = query[i].split()
    del query_t[0]
    doc_t = doc[i].split()
    del doc_t[0]
    
    no = [ ]
    for j in range(2265):
        for k in range(len(query_t)):
            if doc_t[j] == query_t[k]:
                no.append(j)
                
    precision = 0.000            
    for y in range(len(no)):
        precision += (y+1)/(no[y]+1)
        
    precision = precision/len(no)
    MAP.append(precision)

for i in range(query_num):
    avg += MAP[i]

avg = avg/query_num
avg = round(avg,6)
print(avg)
    


# In[8]:




