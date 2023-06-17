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
## Installation
pip install sweatDB
