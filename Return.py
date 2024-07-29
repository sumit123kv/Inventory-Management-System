import dt
def Return(Id,contents2):
    list1=contents2.split('\n')
    list2=[]
    for each in list1:
        list2.append(each.split('|'))    
    return1=int(list2[4][4])
    return2=int(list2[5][4])
    return3=int(list2[6][4])
    return4=int(list2[7][4])
    return5=int(list2[8][4])
    if Id=="P013":
        list2[4][4]=return1+1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=return2
        list2[5][4]=str(list2[5][4])
        list2[6][4]=return3
        list2[6][4]=str(list2[6][4])
        list2[7][4]=return4
        list2[7][4]=str(list2[7][4])
        list2[8][4]=return5
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
    elif Id=="P023":
        list2[5][4]=return2+1
        list2[5][4]=str(list2[5][4])
        list2[4][4]=return1
        list2[4][4]=str(list2[4][4])
        list2[6][4]=return3
        list2[6][4]=str(list2[6][4])
        list2[7][4]=return4
        list2[7][4]=str(list2[7][4])
        list2[8][4]=return5
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
    elif Id=="P034":
        list2[6][4]=return3+1
        list2[6][4]=str(list2[6][4])
        list2[4][4]=return1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=return2
        list2[5][4]=str(list2[5][4])
        list2[7][4]=return4
        list2[7][4]=str(list2[7][4])
        list2[8][4]=return5
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
    elif Id=="P038":
        list2[7][4]=return4+1
        list2[7][4]=str(list2[7][4])
        list2[4][4]=return1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=return2
        list2[5][4]=str(list2[5][4])
        list2[6][4]=return3
        list2[6][4]=str(list2[6][4])
        list2[8][4]=return5
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
    elif Id=="P039":
        list2[8][4]=return5+1
        list2[8][4]=str(list2[8][4])
        list2[7][4]=str(list2[7][4])
        list2[4][4]=return1
        list2[4][4]=str(list2[4][4])
        list2[5][4]=return2
        list2[5][4]=str(list2[5][4])
        list2[6][4]=return3
        list2[6][4]=str(list2[6][4])
        list2[7][4]=return4
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

    else:
        print("\n entered equipment not found!!Please enter valid  id!!!")
    return list2

def temp_cart2(Id,value):
    temp=[]
    for each_item in value:
        if Id==each_item[1]:
            for each in each_item:
                temp.append(each)            
            Rent_days=int(input("\nEnter the number of a Rented days:"))
            if Rent_days>5:
                fine=(Rent_days-5)*(0.10*float(each_item[5][1:]))
            else:
                fine=0
            temp.append(str(Rent_days))
            temp.append(str(fine))
    return temp

def total(cart2,sum_):
    for each_item in cart2:
        float1=float(each_item[5][1:])
        float2=float(each_item[8])
        sum_=float1+float2+sum_
    sum_=str(sum_)    
    return sum_        

def return_note(filename,w,cart,user_name,grand_total):
    return_note=cart
    file5=open(filename,w)
    file5.write("*************************************************************************************************************************************")
    file5.write("\n\n")
    file5.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
    file5.write("Return Note:")
    file5.write("\n\n")
    file5.write("Name:"+user_name)
    file5.write("\n\n")   
    file5.write(" ID\t\tEquipment Name\t\t\tPrice\t\tRent Days\t\tFine")
    file5.write("\n\n")
    for each_item in return_note:
      file5.write(each_item[1]+"\t\t"+each_item[2]+"\t\t"+each_item[5]+"\t\t"+each_item[7]+"\t\t\t"+each_item[8])
    file5.write("\n")
    file5.write("\n")
    file5.write("-------------------------------------------------------------------------------------------------------------------------------------")
    file5.write("\n\n")
    file5.write("Grand total (including fine):\t\t\t\t\t\t\t\t\t"+grand_total)
    file5.write("\n")
    file5.write("*************************************************************************************************************************************")
    file5.close()
