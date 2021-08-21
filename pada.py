import pandas as pd
data = pd.read_csv('data.csv')# data لقراءة ال
# print(data.head())  #print first 5 rows defualt
# print(data.tail())  #print last 5 rows defualt
# print(type(data))
print(data.info())    #بتعطي معلومات عن الداتا
#data.dropna(inplace=True)
data2= data.dropna   #حذف اي داتا فاضيه
print(data.info())
#data2=data.fillna(40) #بتعطي قيمة 40 بالمكان الفاضي
#print(data2.info())
#print(data["Duration"])#بتعامل مع كلوم واحد
data["Calories"].fillna(70,inplace=True) #بعبي مكان الكلورز (فاضي)70
print (data.duplicated()) #اذا في داتا رح يعطيtrue
data.drop_duplicates(inplace=True) #داتا مكررة (بحذفها)
print(data.info)
