from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/', 27017)
print(client.list_database_names())

db = client['Retail']
collection = db['store']

#1.Get all products in the store in json format
list1 = [{"_id": 1,"item1":"Shampoo"},{"_id": 2,"item2":"soap"},{"_id": 3,"item3":"milk"},{"_id": 4,"item4":"drinks"},{"_id": 5,"item5":"fruits"},{"_id": 6,"item6":"vegetables"}]
collection.insert_many(list1)

#2.Insert 10 new products with category soap
collection = db['soap']

list2= [{"_id": 7,"saop_1":"Dove","price": 30,"date": "15/11/2021"},{"_id": 8,"saop_2":"Pears","price": 40,"date": "15/11/2021"},{"_id": 9,"saop_3":"Dettol","price": 30,"date": "15/11/2021"},{"_id": 10,"saop_4":"Nivea","price": 25,"date": "15/11/2021"},{"_id": 11,"saop_5":"Lux","price": 30,"date": "15/11/2021"},{"_id": 12,"saop_6":"Cinthol","price": 30,"date": "15/11/2021"},{"_id": 13,"saop_7":"Santoor","price": 30,"date": "15/11/2021"},{"_id": 14,"saop_8":"Himalaya","price": 30,"date": "15/11/2021"},{"_id": 15,"saop_9":"lifebuoy","price": 20,"date": "07/08/2021"},{"_id": 16,"saop_10":"Godrej","price": 20,"date": "07/08/2021"}]

collection.insert_many(list2)

collection = db['shampoo']
list3= [{"_id": 17,"shampoo_1":"ClinicPlus","price": 80,"date": "15/11/2021"},{"_id": 18,"shampoo_2":"SunSilk","price": 80,"date": "15/11/2021"},{"_id": 19,"shampoo_3":"Pantene","price": 90,"date": "07/08/2021"},{"_id": 20,"shampoo_4":"Nivea","price": 90,"date": "15/11/2021"}]

collection.insert_many(list3)

#3.Update price of product with category shampoo by 10rs
collection = db['shampoo']
prev = {"price": 80}
nextt = {"$inc": {"price": 10}}
collection.update_many(prev, nextt)


#Delete all products with old date (less than 3 months)
collection = db['soap']
oldItem= {"date": "07/08/2021"}
collection.delete_many(oldItem)

collection = db['shampoo']
oldItem= {"date": "07/08/2021"}
collection.delete_many(oldItem)








