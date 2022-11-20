import csv
file_read=open('Student_marks_list.csv')         #file in the same folder
values=csv.reader(file_read,delimiter=',')       #splitting into separate lists
sets=[]
Maths_markset=[]
Chem_markset=[]
Phy_markset=[]
Bio_markset=[]
Eng_markset=[]
Hin_markset=[]
Total_markset=[]
student_rank=[]
for i in values:
    sets.append(i)
    if(i[0]!='Name'):
        Maths_markset.append(int(i[1]))
        Bio_markset.append(int(i[2]))
        Eng_markset.append(int(i[3]))
        Phy_markset.append(int(i[4]))
        Chem_markset.append(int(i[5]))
        Hin_markset.append(int(i[6]))
mmax=max(Maths_markset)                                   #finding max in the given set
indm=Maths_markset.index(mmax)                            #finding index  of the max_value 
print("Topper in Maths is",sets[indm+1][0])
mmax=max(Bio_markset)
indm=Bio_markset.index(mmax)
print("Topper in Biology is",sets[indm+1][0])
mmax=max(Eng_markset)
indm=Eng_markset.index(mmax)
print("Topper in English is",sets[indm+1][0])
mmax=max(Phy_markset)
indm=Phy_markset.index(mmax)
print("Topper in Physis is",sets[indm+1][0])
mmax=max(Chem_markset)
indm=Chem_markset.index(mmax)
print("Topper in Chemistry is",sets[indm+1][0])
mmax=max(Hin_markset)
indm=Hin_markset.index(mmax)
print("Topper in Hindi is",sets[indm+1][0])
for i in range(len(sets)-1):
    d=Maths_markset[i]+Eng_markset[i]+Phy_markset[i]+Bio_markset[i]+Hin_markset[i]+Chem_markset[i]
    Total_markset.append(d)
n=0
student_rank=[]
while(n<3):
    n+=1
    mt=max(Total_markset)
    indt=Total_markset.index(mt)
    student_rank.append(sets[indt+1][0])
    Total_markset[indt]=0                               #making the max value to 0 so that next ranks can be found
print("Best student in the class are ({},{},{})".format(student_rank[0],student_rank[1],student_rank[2]))


"""this code is big and may be more space consuming but according to me its very easy to understand
    just by looking it
"""

"""
time complexity  -  O(n^2)
"""




    

    


    



    
    
    


    
    
        
    
