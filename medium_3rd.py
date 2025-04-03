# FOR NOW GETTING INPUT MANUALLY
ec=input("ENTER THE ENCODED MESSAGE: ").upper().split() #STORING THE ENCODED MESSAGE AS A LIST 
dc=[] #CREATING A LIST FOR FINAL OUTPUT
for i in ec:
    dw="" #CREATING A STRING TO APPEND EACH WORD IN FINAL LIST
    for j in range(len(i)):
        dw+=chr(ord(i[j]) - j - 1) #TO THE DECODED CHARACTER
    dc.append(dw) #APPENDING EACH WORD ON THE LIST        
#PRINTING EACH WORD IN THE LIST
for i in dc:
    print(i,end=" ")


