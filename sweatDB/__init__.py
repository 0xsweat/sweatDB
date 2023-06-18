import datetime
import os
import lzma
version = "v2.0"
e = os.path.isfile
lf = lzma.LZMAFile
class actions :
    
    # Create a database.
    
    def create(db):
        if e(db):
            raise Exception(f"{db} already exists")
        else:
            a = bytes(f"DATABASE NAME : {db} TIME CREATED : {datetime.datetime.utcnow()} CREATED WITH https://pypi.org/project/sweatDB/ {version}\n",'utf-8')
            lf(db,'wb').write(a)

    # Delete an item or database.
    
    def delete(db,item='',delete_type='item'):
        if e(db) != True:
            return f"Database : {db} doesn't exist"
        if delete_type == "db":
            os.remove(db)
        elif item == '':
            raise Exception('No item specified')
        else:
            with lf(db, 'rb') as f:
                a = str(f.read(),'utf-8').split("\n")
                f.close()
            with lf(db, 'wb')as f:
                f.write(bytes("".join([f"{x}\n" for x in a if x.startswith(f'{item}') == False])[:-1],'utf-8'))
                f.close()
    # Add an item to a database.

    def add(db,name,value):
        if e(db):
            with lf(db,'ab') as f:
                f.write(bytes(f'{name} {value}\n','utf-8'))
                f.close()
        else:
            raise Exception(f'Database {db} not found')

    # View ALL items, An item, item names, info, item count, and you can specify the limit with start && end.

    def view(db,option='all',item='',start=1,end=0):
        option = option.lower()
        if e(db) != True:
            raise Exception(f'Database {db} not found')
        elif option == "all":
            c = str(lf(db, 'rb').read(),'utf-8')
            if start < end and start > 0:
                return ''.join(f'{x}\n' for x in c.split("\n")[start + 1:end + 2])
            else:
                return c[:-1]
        elif option == "item":
            with lf(db, 'r')as f:
                b = str(f.read(),'utf-8').split("\n")[1:]
                f.close()
            output = ''
            for i in b:
                if i.startswith(f'{item}'):
                    output += ''.join([f'{x} ' for x in i.split(" ")[1:]])[:-1] + "\n"
            return output
        elif option == "items":
            if start > end and start == 1:
                return(''.join([f'{x.split(" ")[0]}\n' for x in str(lf(db, 'rb').read(),'utf-8').split('\n')[1:]])[:-1])
            else:
                return(''.join([f'{x.split(" ")[0]}\n' for x in str(lf(db, 'rb').read(),'utf-8').split('\n')[start + 1:end + 2]])[:-1])
        elif option == "info":
            return(str(lf(db, 'rb').read(),'utf-8').split("\n")[0])
        elif option == "count":
            return(str(lf(db, 'rb').read(),'utf-8').count("\n") - 1)
        elif option == "iv":
            b = str(lf(db, 'rb').read(),'utf-8').split("\n")[1:]
            output = ''
            if item != '':
                for x in b:
                    if x.startswith(f'{item}'):
                        output += f'{x}\n'
                return output
            else:
                return(''.join([f'{x}\n' for x in str(lf(db, 'rb').read(),'utf-8').split('\n')[1:]])[:-1])
        else:
            return(''.join([f'{x}\n' for x in str(lf(db, 'rb').read(),'utf-8').split('\n')[1:]])[:-1])
                
    # Edit an item in a database.

    def edit(db,item,value,t='value'):
        if e(db) != True:
            return f'Database {db} does not exist'
        b = str(lf(db, 'rb').read(),'utf-8').split("\n")
        for x in range(len(b)):
            if b[x].startswith(f'{item}') and t=='value':
                b[x] = f"{item} {value}"
            elif b[x].startswith(f'{item}') and t!='value':
                b[x] = f"{value} {''.join(f'{a} ' for a in [b[x].split(' ')[1:]])[:-1]}"
        lf(db, 'wb').write(bytes("".join([f"{x}\n" for x in b])[:-1],'utf-8'))
