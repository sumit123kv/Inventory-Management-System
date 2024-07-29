import dt

def Rent(Id,contents2):
    list1=contents2.split('\n')
    list2=[]
    for each in list1:
        list2.append(each.split('|'))    
    rent1=int(list2[4][4])
    rent2=int(list2[5][4])
    rent3=int(list2[6][4])
    rent4=int(list2[7][4])
    rent5=int(list2[8][4])
    if Id=="P013" and rent1>0:
        list2[4][4]=rent1-1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=rent2
        list2[5][4]=str(list2[5][4])
        list2[6][4]=rent3
        list2[6][4]=str(list2[6][4])
        list2[7][4]=rent4
        list2[7][4]=str(list2[7][4])
        list2[8][4]=rent5
        list2[8][4]=str(list2[8][4])
        file3=open("Rent (hide).txt","w")
        file3.write("||..................................................................................||")
        file3.write("\n")
        file3.write(" |    |Name ofequiment                |Brand          |Available                |Amt |")
        file3.write("\n")
        file3.write(" |ID  |                               |name           |equipment(Quantity)      |    |")
        file3.write("\n")
        file3.write(" |....................................|...............|.........................|....|")
        file3.write("\n")
        file3.write(" |P013|Velvet Table Cloth             | Saathi        |"+list2[4][4]+"\t\t\t|$8.0|")
        file3.write("\n")
        file3.write(" |P023|Microphone Set                 | Audio Technica|"+list2[5][4]+"\t\t\t|$189|")
        file3.write("\n")
        file3.write(" |P034|Disco Light Set                |Sonoff         |"+list2[6][4]+"\t\t\t|$322|")
        file3.write("\n")
        file3.write(" |P038 |7.1 Surround Sound Speaker Set|Dolby          |"+list2[7][4]+"\t\t\t|$489|")
        file3.write("\n")
        file3.write(" |P039|Dinner Table 8x5               |PandaFurnitures|"+list2[8][4]+"\t\t\t|$344|")
        file3.write("\n")
        file3.write("||..................................................................................||")
        file3.close()
    elif Id=="P023" and rent2>1:
        list2[5][4]=rent2-1
        list2[5][4]=str(list2[5][4])
        list2[4][4]=rent1
        list2[4][4]=str(list2[4][4])
        list2[6][4]=rent3
        list2[6][4]=str(list2[6][4])
        list2[7][4]=rent4
        list2[7][4]=str(list2[7][4])
        list2[8][4]=rent5
        list2[8][4]=str(list2[8][4])
        file3=open("Rent (hide).txt","w")
        file3.write("||..................................................................................||")
        file3.write("\n")
        file3.write(" |    |Name ofequiment                |Brand          |Available                |Amt |")
        file3.write("\n")
        file3.write(" |ID  |                               |name           |equipment(Quantity)      |    |")
        file3.write("\n")
        file3.write(" |....................................|...............|.........................|....|")
        file3.write("\n")
        file3.write(" |P013|Velvet Table Cloth             | Saathi        |"+list2[4][4]+"\t\t\t|$8.0|")
        file3.write("\n")
        file3.write(" |P023|Microphone Set                 | Audio Technica|"+list2[5][4]+"\t\t\t|$189|")
        file3.write("\n")
        file3.write(" |P034|Disco Light Set                |Sonoff         |"+list2[6][4]+"\t\t\t|$322|")
        file3.write("\n")
        file3.write(" |P038 |7.1 Surround Sound Speaker Set|Dolby          |"+list2[7][4]+"\t\t\t|$489|")
        file3.write("\n")
        file3.write(" |P039|Dinner Table 8x5               |PandaFurnitures|"+list2[8][4]+"\t\t\t|$344|")
        file3.write("\n")
        file3.write("||..................................................................................||")
        file3.close()
    elif Id=="P034" and rent3>1:
        list2[6][4]=rent3-1
        list2[6][4]=str(list2[6][4])
        list2[4][4]=rent1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=rent2
        list2[5][4]=str(list2[5][4])
        list2[7][4]=rent4
        list2[7][4]=str(list2[7][4])
        list2[8][4]=rent5
        list2[8][4]=str(list2[8][4])
        file3=open("Rent (hide).txt","w")
        file3.write("||..................................................................................||")
        file3.write("\n")
        file3.write(" |    |Name ofequiment                |Brand          |Available                |Amt |")
        file3.write("\n")
        file3.write(" |ID  |                               |name           |equipment(Quantity)      |    |")
        file3.write("\n")
        file3.write(" |....................................|...............|.........................|....|")
        file3.write("\n")
        file3.write(" |P013|Velvet Table Cloth             | Saathi        |"+list2[4][4]+"\t\t\t|$8.0|")
        file3.write("\n")
        file3.write(" |P023|Microphone Set                 | Audio Technica|"+list2[5][4]+"\t\t\t|$189|")
        file3.write("\n")
        file3.write(" |P034|Disco Light Set                |Sonoff         |"+list2[6][4]+"\t\t\t|$322|")
        file3.write("\n")
        file3.write(" |P038 |7.1 Surround Sound Speaker Set|Dolby          |"+list2[7][4]+"\t\t\t|$489|")
        file3.write("\n")
        file3.write(" |P039|Dinner Table 8x5               |PandaFurnitures|"+list2[8][4]+"\t\t\t|$344|")
        file3.write("\n")
        file3.write("||..................................................................................||")
        file3.close()
    elif Id=="P038" and rent4>1:
        list2[7][4]=rent4-1
        list2[7][4]=str(list2[7][4])
        list2[4][4]=rent1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=rent2
        list2[5][4]=str(list2[5][4])
        list2[6][4]=rent3
        list2[6][4]=str(list2[6][4])
        list2[8][4]=rent5
        list2[8][4]=str(list2[8][4])
        file3=open("Rent (hide).txt","w")
        file3.write("||..................................................................................||")
        file3.write("\n")
        file3.write(" |    |Name ofequiment                |Brand          |Available                |Amt |")
        file3.write("\n")
        file3.write(" |ID  |                               |name           |equipment(Quantity)      |    |")
        file3.write("\n")
        file3.write(" |....................................|...............|.........................|....|")
        file3.write("\n")
        file3.write(" |P013|Velvet Table Cloth             | Saathi        |"+list2[4][4]+"\t\t\t|$8.0|")
        file3.write("\n")
        file3.write(" |P023|Microphone Set                 | Audio Technica|"+list2[5][4]+"\t\t\t|$189|")
        file3.write("\n")
        file3.write(" |P034|Disco Light Set                |Sonoff         |"+list2[6][4]+"\t\t\t|$322|")
        file3.write("\n")
        file3.write(" |P038 |7.1 Surround Sound Speaker Set|Dolby          |"+list2[7][4]+"\t\t\t|$489|")
        file3.write("\n")
        file3.write(" |P039|Dinner Table 8x5               |PandaFurnitures|"+list2[8][4]+"\t\t\t|$344|")
        file3.write("\n")
        file3.write("||..................................................................................||")
        file3.close()
    elif Id=="P039" and rent5>1:
        list2[8][4]=rent5-1
        list2[8][4]=str(list2[8][4])
        list2[4][4]=rent1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=rent2
        list2[5][4]=str(list2[5][4])
        list2[6][4]=rent3
        list2[6][4]=str(list2[6][4])
        list2[7][4]=rent4
        list2[7][4]=str(list2[7][4])
        file3=open("Rent (hide).txt","w")
        file3.write("||..................................................................................||")
        file3.write("\n")
        file3.write(" |    |Name ofequiment                |Brand          |Available                |Amt |")
        file3.write("\n")
        file3.write(" |ID  |                               |name           |equipment(Quantity)      |    |")
        file3.write("\n")
        file3.write(" |....................................|...............|.........................|....|")
        file3.write("\n")
        file3.write(" |P013|Velvet Table Cloth             | Saathi        |"+list2[4][4]+"\t\t\t|$8.0|")
        file3.write("\n")
        file3.write(" |P023|Microphone Set                 | Audio Technica|"+list2[5][4]+"\t\t\t|$189|")
        file3.write("\n")
        file3.write(" |P034|Disco Light Set                |Sonoff         |"+list2[6][4]+"\t\t\t|$322|")
        file3.write("\n")
        file3.write(" |P038 |7.1 Surround Sound Speaker Set|Dolby          |"+list2[7][4]+"\t\t\t|$489|")
        file3.write("\n")
        file3.write(" |P039|Dinner Table 8x5               |PandaFurnitures|"+list2[8][4]+"\t\t\t|$344|")
        file3.write("\n")
        file3.write("||..................................................................................||")
        file3.close()   
    elif Id=="P013" and rent1<1:
        print("The equipment is out of stock.")
    elif Id=="P023" and rent2<1:
        print("The equipment is out of stock.")
    elif Id=="P034" and rent3<1:
        print("The equipment is out of stock.")
    elif Id=="P038" and rent4<1:
        print("The equipment is out of stock.")
    elif Id=="P039" and rent5<1:
        print("The equipment is out of stock.")    
    else:
        print("\nentered equipment not found!!Please enter valid  id!!!")
    return list2
        
def temp_cart(Id,value):
    temp=[]
    for each_item in value:
        if Id==each_item[1]:
            if int(each_item[4])>0:
                temp.append(each_item)
    return temp

def rent_note(filename,w,cart,user_name):
    rent_note=cart
    file4=open(filename,w)
    file4.write("*************************************************************")
    file4.write("\n\n")
    file4.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
    file4.write("Rent Note:")
    file4.write("\n\n")
    file4.write("Name:"+user_name)
    file4.write("\n\n")   
    file4.write(" ID\t\t\t\tEquipmentName\t\t\t\tPrice")
    file4.write("\n\n")
    for each_item in rent_note:
        file4.write(each_item[1]+"\t\t"+each_item[2]+"\t\t"+each_item[5])
        file4.write("\n")
    file4.write("\n")
    file4.write("*************************************************************")
    file4.close()
