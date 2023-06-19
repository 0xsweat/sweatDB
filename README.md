# About sweatDB
SweatDB is a cutting-edge database management system that offers a simplified syntax, making it an ideal choice for users seeking an easier alternative to SQL. With SweatDB, you can efficiently organize, store, and retrieve your data without the complexities associated with traditional database systems.

## Installation
```bash
pip install sweatDB
```
## SQL Comparison to sweatDB

### SQL
```sql
CREATE TABLE people (Name TEXT,Location TEXT);
INSERT INTO people (
    Name,
    Location,
    Name,
    Location) 
VALUES ('Dorito man',
    'Dallas Texas',
    'John Adams',
    'New york New york');
SELECT Name FROM people WHERE Name like 'D%';
```

### Python
```py
from sweatDB import actions as sdb

sdb.create('people')

data = {
    '!Name!Dorito': 'man',
    '!Location!Dorito': 'Dallas, Texas',
    '!Name!John': 'Adams',
    '!Location!John': 'New York, New York'
}

for key, value in data.items():
    sdb.add('people', key, value)

results = sdb.view('people', 'iv', '!Name!D')
print(results)

```

## First example Usage
```py
from sweatDB import actions as sdb

sdb.create('test')
print(sdb.view('test', 'info'))

for x in range(100):
    sdb.add('test', f'item{x}', x * 100)

print(sdb.view('test', 'count'))
print(sdb.view('test', start=50, end=60))

sdb.delete('test', delete_type='db')

```

<details>
<summary><b>Preview</b></summary>

![image](https://github.com/0xsweat/sweatDB-pypi/blob/main/images/example.png?raw=true)
</details>


## Second example Usage

```py
from sweatDB import actions as sdb

dbs = ['inventory', 'display', 'orders']

for db in dbs:
    sdb.delete(db, delete_type='db')
    sdb.create(db)

fruits = {'Apple': 9, 'Pear': 3, 'Banana': 20}
for fruit, quantity in fruits.items():
    sdb.add('inventory', f'fruits-{fruit}', quantity)

vegetables = {'Broccoli': 5, 'Carrot': 10, 'Cauliflower': 20}
for vegetable, quantity in vegetables.items():
    sdb.add('inventory', f'vegetables-{vegetable}', quantity)

items = sdb.view('inventory', 'iv')
for item in items.split("\n")[:-1]:
    item, value = map(str, item.split(" "))
    sdb.add('display', item.split("-")[1], 1)
    sdb.edit('inventory', item, int(value) - 1)

print(f"On display:\n{sdb.view('display', 'items')}")
print(f"In inventory:\n{sdb.view('inventory', 'iv')}")

orders = {'vegetables-Broccoli': 2, 'vegetables-Carrot': 5, 'fruits-Apple': 3, 'fruits-Banana': 10}
for order, quantity in orders.items():
    sdb.add('orders', order, quantity)

print(f"Current orders:\n{sdb.view('orders', 'iv')}")

for order in sdb.view('orders', 'iv').split("\n")[:-1]:
    item, value = map(str, order.split(" "))
    sdb.edit('inventory', item, int(sdb.view('inventory', 'item', item)) - int(value))
    sdb.delete('orders', item)

print(f"Inventory after fulfilling orders:\n{sdb.view('inventory', 'iv')}")

vegetables_inventory = ''.join([f"{x.replace('vegetables-', '')}\n" for x in sdb.view('inventory', 'iv', 'vegetables-').split('\n')])[:-1]
fruits_inventory = ''.join([f"{x.replace('fruits-', '')}\n" for x in sdb.view('inventory', 'iv', 'fruits-').split('\n')])[:-1]

print(f"Vegetables in inventory:\n{vegetables_inventory}")
print(f"Fruits in inventory:\n{fruits_inventory}")

```
<details>
<summary><b>Preview</b></summary>

![image](https://github.com/0xsweat/sweatDB-pypi/blob/main/images/example2.png?raw=true)
</details>

## Website example
<details>
<summary><b>Gif Preview</b></summary>
    
![siteexample](https://github.com/0xsweat/sweatDB-pypi/assets/83222877/33f2d706-e867-4301-afc3-d67ca1579a5a)

</detail>
