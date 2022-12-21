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
          if j == 0 or j == 1 or j == 3 or j == 4:
            row = row + "*"
          if j == 2:
            row = row + " "
        if i == 3:
          if j == 1 or j == 3:
            row = row + " "
          if j == 2 or j == 0 or j == 4:
            row = row + "*"

      print(row)

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
          if j == 2:
            row = row + "*"
          if j == 0 or j == 1 or j == 3 or j == 4:
            row = row + " "
      print(row)

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

word = input("Введіть слово з великої літери : ").upper()
for no in word:
  if "A" in no:
      A()

  if "B" in no:
      B()

  if "C" in no:
      C()

  if "D" in no:
      D()

  if "E" in no:
      E()

  if "F" in no:
      F()

  if "G" in no:
      G()

  if "H" in no:
      H()

  if "I" in no:
      I()

  if "w" in no:
      J()

  if "K" in no:
      K()

  if "L" in no:
      L()

  if "M" in no:
      M()

  if "N" in no:
      N()

  if "O" in no:
      O()

  if "P" in no:
      P()

  if "Q" in no:
      Q()

  if "R" in no:
      R()

  if "S" in no:
      S()

  if "T" in no:
      T()

  if "U" in no:
      U()

  if "V" in no:
      V()

  if "W" in no:
      W()

  if "X" in no:
      X()

  if "Y" in no:
      Y()

  if "Z" in no:
      Z()

  else:
      pass
