# sweatDB
A database management system with an easier syntax than SQL

## Example usage
![image](https://github.com/0xsweat/sweatDB-package/blob/main/example.png)
```py
from sweatDB import actions as sdb
sdb.create('test')
print(sdb.view('test','info'))
for x in range(100):
    sdb.add('test',f'item{x}',x * 100)
print(sdb.view('test','count'))
print(sdb.view('test',start=50,end=60))
sdb.delete('db','test')
```
![image](https://github.com/0xsweat/sweatDB-package/blob/main/example2.png)
```py
from sweatDB import actions as sdb
dbs = ['inventory','display','orders']
for x in dbs:
    sdb.delete(x,delete_type='db')
    sdb.create(x)
fruits = {'Apple':9,'Pear':3,'Banana':20}
for x in fruits:
    sdb.add('inventory',f'fruits-{x}',fruits[x])
vegetables = {'Broccoli':5,'Carrot':10,'Cauliflower':20}
for x in vegetables:
    sdb.add('inventory',f'vegetables-{x}',vegetables[x])
items = sdb.view('inventory','iv')
for i in items.split("\n")[:-1]:
    item,value = map(str,i.split(" "))
    sdb.add('display',item.split("-")[1],1)
    sdb.edit('inventory',item,int(value) - 1)
print(f"On display :\n{sdb.view('display','items')}")
print(f"In inventory :\n{sdb.view('inventory','iv')}")
orders = {'vegetables-Broccoli':2,'vegetables-Carrot':5,'fruits-Apple':3,'fruits-Banana':10}
for x in orders:
    sdb.add('orders',x,orders[x])
print(f"Current orders :\n{sdb.view('orders','iv')}")
for x in sdb.view('orders','iv').split("\n")[:-1]:
    item,value = map(str,x.split(" "))
    sdb.edit('inventory',item,int(sdb.view('inventory','item',item)) - int(value))
    sdb.delete('orders',item)
print(f"Inventory after fulfilling orders :\n{sdb.view('inventory','iv')}")
v = ''.join([f"{x.replace('vegetables-','')}\n" for x in sdb.view('inventory','iv','vegetables-').split('\n')])[:-1]
f = ''.join([f"{x.replace('fruits-','')}\n" for x in sdb.view('inventory','iv','fruits-').split('\n')])[:-1]
print(f"Vegetables in inventory :\n{v}")
print(f"Fruits in inventory :\n{f}")
```
## Installation
pip install sweatDB
