import pandas as pd
excel_data = pd.read_excel('EAPAR PENDING (1).xls')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['SRNO', 'NAME', 'SEX','PHONE NUMBER'])
# Print the content
rows,cols = (len(data['SRNO']),3)
val = [[0]*cols]*rows
pair = val = [[0]*cols]*rows
for i in range(rows):
    val[i][0] = data['NAME'].to_list()[i]
    val[i][1] = data['SEX'].to_list()[i]
    val[i][2] = data['PHONE NUMBER'].to_list()[i]
    pair[i] = ((val[i][0],val[i][1],val[i][2]))
f = open("message.txt", "r")
MESS = f.read()
f.close()
def getmessage(num,message):
    for i,j,k in pair:
        if(str(j) == "M"):
            if(str(num) == str(k)):
                message = message.replace("Dear Sir/Madam","Dear Sri "+str(i))
                return message
        elif(str(j) == "F"):
            if(str(num) == str(k)):
                message = message.replace("Dear Sir/Madam","Madam "+str(i))
                return message

print(getmessage(9573164558,MESS))