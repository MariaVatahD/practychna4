word = list(input("Введіть слово: "))

for no in word:
    def A():
        for i in range(7):  #A
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
            print(row)

for no in word:
    if no == "A": A()

for no in word:
    def B():
        for i in range(7):  #B
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 1 or i == 2 or j == 3 or j == 4:
                        row = row + "*"   
            print(row)

for no in word:
    if no == "B": B()

for no in word:
    def C():
        for i in range(7):  #C
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 5:
                    if j == 1 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2 or i == 3 or i == 4:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)   

for no in word:
    if no == "C": C()
    
for no in word:
    def D():
        for i in range(7):  #D
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 4:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)       

for no in word:
    if no == "D": D()
    
for no in word:
    def E():
        for i in range(7):  #E
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 0:
                        row = row + "*"
                if i == 3:
                    if j == 0 or j == 1 or j == 2:
                        row = row + "*"
                    if j == 3 or j == 4:
                        row = row + " "
            print(row)

for no in word:
    if no == "E": E()
    
for no in word:
    def F():
        for i in range(7):  #F
            row = ""
            for j in range(5):  
                if i == 0:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 0:
                        row = row + "*"
                if i == 3:
                    if j == 0 or j == 1 or j == 2:
                        row = row + "*"
                    if j == 3 or j == 4:
                        row = row + " " 
                if i == 6:
                    if j == 0:
                        row = row + "*"
            print(row) 

for no in word:
    if no == "F": F()
    
for no in word:
    def G():
        for i in range(7):  #G
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 5 or i == 4:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 3 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
                if i == 2:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)

for no in word:
    if no == "G": G()
    
for no in word:
    def H():
        for i in range(7):  #H
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:    
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
            print(row)

for no in word:
    if no == "H": H()
    
for no in word:
    def I():
        for i in range(7):  #I
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "    
            print(row)

for no in word:
    if no == "I": I()

for no in word:
    def J():
        for i in range(7):  #J
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "    
                if i == 6:
                    if j == 0 or j == 1:
                        row = row + "*"
                    if j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)

for no in word:
    if no == "J": J()

for no in word:
    def K():
        for i in range(7):  #K
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 1 or i == 5:
                    if j == 0 or j == 3:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 4:
                        row = row + " "
                if i == 2 or i == 4:
                    if j == 0 or j == 2:
                        row = row + "*"
                    if j == 1 or j == 3 or j == 4:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 2:
                        row = row + "*"
                    if j == 3 or j == 4:
                        row = row + " "        
            print(row)

for no in word:
    if no == "K": K()
 
for no in word:
    def L():
        for i in range(7):  #L
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0:    
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
                if i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
            print(row)

for no in word:
    if no == "L": L()

for no in word:
    def T():
        for i in range(7):  #T
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "
            print(row)
 
for no in word:
        if no == "T": T()
 
for no in word:
    def O():
        for i in range(7):  #O
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)

for no in word:
    if no == "O": O()

for no in word: 
    def U():
        for i in range(7):  #U
            row = ""
            for j in range(5):    
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 6:
                    if j == 0 or j == 4:
                        row = row + " "
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)

for no in word:
    if no == "U": U()

for no in word:
    def V():
        for i in range(7):  #V
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 1 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 2 or j == 4:
                        row = row + " "
                if i == 6:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3:
                        row = row + " "
            print(row)

for no in word:
    if no == "V": V()

for no in word:
    def M():
        for i in range(7):  #M
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 4 or i == 5:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 0 or j == 1 or j == 3 or j == 4 :
                        row = row + "*"
                    if j == 2:
                        row = row + " "
                if i == 3:
                    if j == 1 or j == 3:
                        row = row + " "
                    if j == 2 or j == 0 or j == 4:
                        row = row + "*"
                    
            print(row)

for no in word:
    if no == "M": M()

for no in word:
    def P():
        for i in range(7):  #P
            row = ""
            for j in range(5):
                if i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
                if i == 1 or i == 2:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 0 or i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)

for no in word:
    if no == "P": P()
    
for no in word:
    def S():
        for i in range(7):  #S
            row = ""
            for j in range(5):
                if i == 0 or i == 3 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
     
     
     
                    if j == 0 or j == 4:
                        row = row + " "
                if i == 1 or i == 2:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
                if i == 4 or i == 5:
                    if j == 4:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)

for no in word:
    if no == "S": S()
 
for no in word:
    def W():
        for i in range(7):  #W
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 2 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + "*"
                    if j == 2:
                        row = row + " "  
                    
            print(row)

for no in word:
    if no == "W": W()

for no in word:
    def X():
        for i in range(7):  #X
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2 or i == 4:
                    if j == 1 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 2 or j == 4:
                        row = row + " "
                if i == 3:
                    if j == 2:
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "
            print(row)

for no in word:
    if no == "X": X()

for no in word:
    def N():
        for i in range(7):  #N
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 0 or j == 1 or j == 4:
                        row = row + "*"
                    if j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 2 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 0 or j == 3 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
            print(row)

for no in word:
    if no == "N": N() 

for no in word:
    def R():
        for i in range(7):  #R
            row = ""
            for j in range(5):
                if i == 0 or i == 3:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 0 or j == 2:
                        row = row + "*"
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 0 or j == 3:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
            print(row)

for no in word:
    if no == "R": R()
        
for no in word:
    def Y():
        for i in range(7):  #Y
            row = ""
            for j in range(5):
                if i == 0 or i == 1:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 1 or j == 3:
                        row = row + "*"
                    if j == 0 or j == 2 or j == 4:
                        row = row + " "
                if i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 2 :
                        row = row + "*"
                    if j == 0 or j == 1 or j == 3 or j == 4:
                        row = row + " "
            print(row)

for no in word:
    if no == "Y": Y()

for no in word:
    def Q():
        for i in range(7):  #Q
            row = ""
            for j in range(5):
                if i == 1 or i == 2 or i == 3 or i == 4:
                    if j == 0 or j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 0 or j == 3:
                        row = row + "*"
                    if j == 1 or j == 2:
                        row = row + " "
                if i == 0:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                    if j == 0:
                        row = row + " "
                if i == 6:
                    if j == 1 or j == 2 or j == 4:
                        row = row + "*"
                    if j == 0 or j == 3:
                        row = row + " "
            print(row)

for no in word:
    if no == "Q": Q()
  
for no in word:
    def Z():
        for i in range(7):  #Z
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1:
                    if j == 4:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 0:
                        row = row + " "
                if i == 2:
                    if j == 3:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 4 or j == 0:
                        row = row + " " 
                if i == 3:
                    if j == 2:
                        row = row + "*"
                    if j == 1 or j == 4 or j == 3 or j == 0:
                        row = row + " "
                if i == 4:
                    if j == 1:
                        row = row + "*"
                    if j == 4 or j == 2 or j == 3 or j == 0:
                        row = row + " "
                if i == 5:
                    if j == 0:
                        row = row + "*"
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
            print(row)

for no in word:
    if no == "Z": Z()