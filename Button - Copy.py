def input_():
    print("Click button 1 to view equipment")
    print("Click button 2 to Rent equipment")
    print("Click button 3 to return equipment")
    print("Click button 4 to exit")
    
def read():
    file1=open("equipment.txt","r")
    contents1=file1.read()
    print("\n")
    print(contents1)
    file1.close()

def read2():
    file2=open('Rent (hide).txt','r')
    contents2=file2.read()
    print(contents2)
    return contents2


