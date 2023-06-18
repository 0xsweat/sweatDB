import datetime
import os
version = "v2.0"
e = os.path.isfile

class actions :
    
    # Create a database.
    
    def create(db):
        if e(db):
            raise Exception(f"{db} already exists")
        else:
            open(db,'w').write(f"DATABASE NAME : {db} TIME CREATED : {datetime.datetime.utcnow()} CREATED WITH https://pypi.org/project/sweatDB/ {version}\n")
    
    # Delete an item or database.
    
    def delete(db,item='',delete_type='item'):
        if e(db) != True:
            return f"Database : {db} doesn't exist"
        if delete_type == "db":
            os.remove(db)
        elif item == '':
            raise Exception('No item specified')
        else:
            a = open(db, 'r').read().split("\n")
            open(db, 'w').write("".join([f"{x}\n" for x in a if x.startswith(f'{item}') == False])[:-1])

    # Add an item to a database.

    def add(db,name,value):
        if e(db):
            open(db, 'a').write(f'{name} {value}\n')
        else:
            raise Exception(f'Database {db} not found')

    # View ALL items, An item, item names, info, item count, and you can specify the limit with start && end.

    def view(db,option='all',item='',start=1,end=0):
        option = option.lower()
        if e(db) != True:
            raise Exception(f'Database {db} not found')
        elif option == "all":
            c = open(db, 'r').read()
            if start < end and start > 0:
                return ''.join(f'{x}\n' for x in c.split("\n")[start + 1:end + 2])
            else:
                return c[:-1]
        elif option == "item":
            b = open(db, 'r').read().split("\n")[1:]
            output = ''
            for i in b:
                if i.startswith(f'{item}'):
                    output += ''.join([f'{x} ' for x in i.split(" ")[1:]])[:-1] + "\n"
            return output
        elif option == "items":
            if start > end and start == 1:
                return(''.join([f'{x.split(" ")[0]}\n' for x in open(db, 'r').read().split('\n')[1:]])[:-1])
            else:
                return(''.join([f'{x.split(" ")[0]}\n' for x in open(db, 'r').read().split('\n')[start + 1:end + 2]])[:-1])
        elif option == "info":
            return(open(db, 'r').read().split("\n")[0])
        elif option == "count":
            return(open(db, 'r').read().count("\n") - 1)
        elif option == "iv":
            b = open(db, 'r').read().split("\n")[1:]
            output = ''
            if item != '':
                for x in b:
                    if x.startswith(f'{item}'):
                        output += f'{x}\n'
                return output
            else:
                return(''.join([f'{x}\n' for x in open(db, 'r').read().split('\n')[1:]])[:-1])
        else:
            return(''.join([f'{x}\n' for x in open(db, 'r').read().split('\n')[1:]])[:-1])
                
    # Edit an item in a database.

    def edit(db,item,value,t='value'):
        if e(db) != True:
            return f'Database {db} does not exist'
        b = open(db, 'r').read().split("\n")
        for x in range(len(b)):
            if b[x].startswith(f'{item}') and t=='value':
                b[x] = f"{item} {value}"
            elif b[x].startswith(f'{item}') and t!='value':
                b[x] = f"{value} {''.join(f'{a} ' for a in [b[x].split(' ')[1:]])[:-1]}"
        open(db, 'w').write("".join([f"{x}\n" for x in b])[:-1])
