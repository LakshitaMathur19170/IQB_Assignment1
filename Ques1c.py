import numpy as np
#Enter Sequences 
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
  Matrix_main[i][0]=i*gap
for j in range(len2+1):
  Matrix_main[0][j]=j*gap

#Step 2 (Matrix Filling)
for i in range(1,len1+1):
  for j in range(1,len2+1):
    # if  Matrix_main[i][j]==Matrix_main[i-1][j-1] :
    #   Matrix_main[i][j]=Matrix_main[i-1][j-1]+match
    # else: 
      Matrix_main[i][j]=max(Matrix_main[i-1][j-1]+Matrix_match[i-1][j-1],
                            Matrix_main[i-1][j]+gap,
                            Matrix_main[i][j-1]+gap)


final_sequence1=[]
final_sequence2 =[]

# Step 3 Traceback
def recursive_traceback(length1, length2, sequence1, sequence2):
  if length1==0 and length2==0 : # base condition
    final_sequence1.append(sequence1)
    final_sequence2.append(sequence2)
    return 
  
  if (Matrix_main[length1][length2] == Matrix_main[length1-1][length2-1]+ Matrix_match[length1-1][length2-1]) :
    recursive_traceback(length1-1, length2-1, seq_1[length1-1] + sequence1, seq_2[length2-1] + sequence2)  
  if (Matrix_main[length1][length2] == Matrix_main[length1-1][length2]+ gap) :
    recursive_traceback(length1-1, length2, seq_1[length1-1]+sequence1,"-"+ sequence2)
  if (Matrix_main[length1][length2] == Matrix_main[length1][length2-1]+ gap): 
    recursive_traceback(length1, length2-1, "-" + sequence1,  seq_2[length1-1] + sequence2)


def show():
    joint = ""
    print("All possible alignments:")
    for t in range(len(final_sequence1)):
      for i in range(0,len(final_sequence1[t])):
        seq1=final_sequence1[t]
        seq2=final_sequence2[t]
        if (final_sequence1[t])[i] == (final_sequence2[t])[i]:
          joint = joint + "|"
        else:
          joint = joint + " "
        print(final_sequence1[t])
        print(joint)
        print(final_sequence2[t])
        joint = ""


#Ques 1 part c(all alignments)
print("DP Matrix \n",Matrix_main) 
recursive_traceback(len1,len2,"","")
show()
print("The optimal path score is ", Matrix_main[len1][len2])