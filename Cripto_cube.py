import numpy as np
import random as rnd
'''
Crypto code made by Aizar E. D.
Submit your message in the first line and then type N in the second line if 
you don't have a decripting key of the form: URL RRDD
where R, L, U, D are the rotations given to a specific cube 
where URL is the sequence for the 1st cube
      RRDD is the sequence for th 2nd cube etc.
'''

Message=input("Introduce the secret message: \n" )
Keywords=input("If you are decrypting introduce the key as \n RRL LLD. If not press N :\n")

#define cube vertices and the center of the cube
r0=1/2*np.array([1.0,1.0,1.0])
vertices=np.array([[0,0,0],[0,0,1],[1,0,1],[1,0,0],[0,1,0],[0,1,1],[1,1,1],[1,1,0]])

Keywords=Keywords.split()
print(Keywords)
print("Your original message is: \n",Message)
#Message=[i for i in Message if i!=" "]   #If you decide to exclude spaces
print("length of message:",len(Message))

#Determining number of cubes needed:
if len(Message)%8 != 0: 
    number_cubes=len(Message)//8+1
else:
    number_cubes=len(Message)//8
nc=number_cubes
print("Number of cubes used:",nc)

#Map   the message string to vertices of n cubes
M=[]
N=[]
for cube in range(nc):
    if (cube)*8<=(len(Message)-8): 
        for vertex in range(8):
            M.append(Message[8*cube+vertex]) 
        N.append(M)
        M=[]
    else:
        d=len(Message)-(cube)*8
        #print('quedan:',d)
        for vertex in range(d):
            M.append(Message[8*cube+vertex])
        for i in range(8-d):
            M.append("+")
        N.append(M) 
        M=[]
                                            
print("Message segmented in cubes  extra space is filled with \'+\': \n", N)

#define rotations
up=np.array([[1,0,0],[0,0,1],[0,-1,0]])
down=np.array([[1,0,0],[0,0,-1],[0,1,0]])
right=([[0,-1,0],[1,0,0],[0,0,1]])
left=([[0,1,0],[-1,0,0],[0,0,1]])

#Generating  a random sequence of rotations of 2<n <7  elements

def sequence():
    actions=["U", "D", "R","L"]
    sequence=[actions[rnd.randint(0,3)] for i in range(rnd.randint(3,7))]   
    return(sequence) 
sec=sequence()

#create dictionary between rotations and the letters U D L R
rotation_dic={"U":up,"D":down, "L":left, "R":right}
#print( rotation_dic.keys())

#Applying 1 rotation to a vertex of the cube
def rotation(rotation,vertex):
     new_vector=r0+np.dot(rotation_dic[rotation],vertex-r0)
     return(new_vector)
#Applying a secuence of rotations to  all the vertices of a cube 
def Apply_sequence(sec,vertices):  
    new_vertices=[]
    for j in range(len(vertices)):
        #copy_vertex=list(vertices[j])    
        copy_vertex=vertices[j]   
        for i in range(len(sec)):
            v2=rotation(sec[i],copy_vertex)
            copy_vertex=v2
        #print("For the sequence: {0}".format(sec))    
        #print("Rotation of {0} is: {1}".format(vertices[j], copy_vertex))
        new_vertices.append(list(copy_vertex))
    return(new_vertices)

#Encripting key (Getting the new order of the vectors of the cube respect to the original order):
def Encripting(sec,vertices):
    V_new=Apply_sequence(sec,vertices)
    key_sec=[]
    for i in range(len(vertices)):
        vv=vertices.tolist()
        vv=vv.index(V_new[i])
        key_sec.append(vv)
    return(key_sec)
#Decripting sequence: For a given sequence of rotations, produce the sequence that restore  the cube to its original form.    
def Decript(sec):
    sec=sec[::-1]
    new_seq=[]
    for i in sec:
        if i=="U":
            new_seq.append("D")
        elif i=="D":
            new_seq.append("U")
        elif i=="R":
            new_seq.append("L")
        elif i=="L":
            new_seq.append("R")
        else:
            continue
    return(new_seq)
#key_sec=Encripting(sec,vertices)    
#print(key_sec) 
#Encripting message  stored in  the nc cubes through the variable N.
N2=[]
N3=[]
REV_KEYS=[]
for cube_number in range(nc):
    if Keywords==['N']:
        new_sequence=sequence()
        #print("Generated Sequences:",new_sequence)
        key_sec=Encripting(new_sequence,vertices)
        #REV_KEYS.append(Decript(new_sequence))
        REV_KEYS.append("".join(Decript(new_sequence)))
        for index_vertex in range(len(N[cube_number])):
            N3.append(N[cube_number][key_sec[index_vertex]])
        N3=''.join(N3)
        N2.append(N3)
        N3=[]
    else: #We decript the message instead
        key_sec=Encripting(Keywords[cube_number],vertices)
        REV_KEYS.append("".join(Decript(Keywords[cube_number])))
        for index_vertex in range(len(N[cube_number])):
            N3.append(N[cube_number][key_sec[index_vertex]])
        N3=''.join(N3)
        N2.append(N3)
        N3=[]
#print("Your secret message is:", N2)    
print("Your secret message is:\n","."+"".join(N2)+".")
#print("Your key is:", REV_KEYS)
print("Your encription/decription key is:\n", " ".join(REV_KEYS))
print("To decript the message run the code again and \n copy the text between the dots . . \n including the spaces and enter sequences of rotations in the second line")
