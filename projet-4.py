#!/usr/bin/env python
# coding: utf-8

# In[10]:


class departement:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self):
        print(self.name)
    
class Etudiant(departement):

    def __init__(self, name, code, m1, m2):
        self.code = code
        self.m1 = m1
        self.m2 = m2
        super ().__init__(name)
    def accept(self, Name, code, moy1, moy2):
   
        ob = Etudiant(Name, code, moy1, moy2)
        ls.append(ob)
 
    def display(self, ob):
        print("Name : ", ob.name)
        print("code : ", ob.code)
        print("Moy1 : ", ob.m1)
        print("Moy2 : ", ob.m2)
        print("\n")
 
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].code== rn):
                return i
 
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
 
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].code = roll
 
 
ls = []
obj = Etudiant('', 0, 0, 0)
 

obj.accept("makrem", 1,18, 19)
obj.accept("mahdi", 2, 20, 15)
obj.accept("saif", 3, 18, 20)
obj.accept("moataz", 4, 19, 20)


print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

    
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])


obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])
    
    
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])

    

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




