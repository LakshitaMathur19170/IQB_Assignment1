import numpy as np
#Enter SequenceSequences 
seq_1="ATCAGAGTA"
seq_2="TTCAGTA"
len1=len(seq_1)
len2=len(seq_2)

#Create Matrices
Matrix_main=np.zeros(((len1+1),(len2+1)), dtype=int)
Matrix_match=np.zeros((len1,len2), dtype=int)

#Scores
match=2
mismatch=-1
gap=-1

#Fill the Matrix_match according to mismatch and match
for i in range(len1):
  for j in range(len2):
    if seq_1[i]==seq_2[j] :
      Matrix_match[i][j]=match
    else:
      Matrix_match[i][j]=mismatch
#print(Matrix_match)


#Filling Matrix_main
#Step 1 (Initialisation)
for i in range(len1+1):
  Matrix_main[i][0]=0
for j in range(len2+1):
  Matrix_main[0][j]=0

#Step 2 (Matrix Filling)
for i in range(1,len1+1):
  for j in range(1,len2+1):
    Matrix_main[i][j]=max(Matrix_main[i-1][j-1]+Matrix_match[i-1][j-1],
                            Matrix_main[i-1][j]+gap,
                            Matrix_main[i][j-1]+gap,0)


final_sequence1=""
final_sequence2=""
l1=len1
l2=len2
while Matrix_main[l1][l2]!=0 :
  if Matrix_main[l1][l2]==Matrix_main[l1-1][l2-1]+Matrix_match[l1-1][l2-1] :
    final_sequence1=seq_1[l1-1] + final_sequence1
    final_sequence2 = seq_2[l2-1] + final_sequence2
    l1 = l1 - 1
    l2 = l2 - 1
    
  elif Matrix_main[l1][l2]==Matrix_main[l1-1][l2] + gap :
    final_sequence1 = seq_1[l1-1] + final_sequence1
    final_sequence2 = "-" + final_sequence2

    l1 = l1 -1
  else:
    final_sequence1 = "-" + final_sequence1
    final_sequence2 = seq_2[l2-1] + final_sequence2
    l2 = l2 - 1


def printMatrix(a):
  for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='  ')
    print()


def printer():
    join = ""
    for i in range (len(final_sequence1)):
      if final_sequence1[i] == final_sequence2[i]:
        join = join + "|"
      else:
        join = join + " "
    print("The optimal alignment:")
    print(final_sequence1)
    print(join)
    print(final_sequence2)


def findMaxIndex(row, column, matrix):
    maxRowIndex = row;
    maxColIndex = column;
    max = 0;
    for currRow in range(row, len(matrix)):
        if (max < matrix[currRow][column]):
            max = matrix[currRow][column]
            maxRowIndex = currRow;
            maxColIndex = column;
    for currCol in range(column, len(matrix[0])):
        if (max <= matrix[row][currCol]):
            max = matrix[row][currCol]
            maxRowIndex = row
            maxColIndex = currCol;
    return [maxRowIndex, maxColIndex];

# Ques 2 part a 
print("DP Matrix")
printMatrix(Matrix_main)
# Ques 2 part b
printer()
t=findMaxIndex(len1,len2,Matrix_main)
print("The optimal path score is ", Matrix_main[len1][len2], " at (",t[0] ,",",t[1],")")