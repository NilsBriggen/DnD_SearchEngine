import ItemDB

db = ItemDB.DB
keys = [i for i in db.keys() if i not in ["name", "version"]]
id = 0

for i in keys:
    for j in range(len(db[i])):
        db[i][j]["id"] = id
        id += 1

db["name"] = "ItemDB Database (Reformated)"
db["version"] = "2.0"

with open("ItemDB.py", "w") as f:
    f.write(f"DB = {str(db)}")
