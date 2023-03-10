import sys
import datetime
import os
import readline
version = "v1.4"
help = ["sweatDB was created by 0xsweat AKA https://tryhackme.com/p/0xsweat AKA https://github.com/0xsweat\nIt is a simple database management system you can identify it's files with their .sweatdb extension", "create is a command used to create a db\n    usage : python3 sweatDBms.py create NAME", "add is a command used to add a object to a database, values can be supplied from a file or as an arguement\n   usage : python3 sweatDBms.py add arg DBNAME NAME VALUE\n    or : python3 sweatDBms.py add file-value DBNAME NAME fileWithValue\n     or : python3 sweatDBms.py add file-both DBNAME fileWithName fileWithValue\n     or : python3 sweatDBms.py file-name DBNAME fileWithName value", "help is a command to get some help, you can use it multiple ways :)\n    usage : python3 sweatDBms.py help\n     or : python3 sweatDBms.py help COMMAND", "delete is used for deleting a database or deleting a item\n     usage : python3 sweatDBms.py delete db NAME\n    or : python3 sweatDBms.py delete item db NAME", "view used for viewing items in a database, an items value, or the entire db, or you can view info on the DB\n  usage : python3 sweatDBms.py view DB all\n    or : python3 sweatDBms.py view DB item name\n   or : python3 sweatDBms.py view DB items\n   or : python3 sweatDBms.py view DB info", "edit used to edit the value of a item\n     usage : python3 sweatDBms.py edit DB ITEMNAME NEWVALUE", 'version will print the version of SWEATDB\n    usage : python3 sweatDBms.py version', 'interactive will launch a sweatDB shell\nyou are able to use "clear" to clear screen in interactive mode and "quit" to quit\n    usage : python3 sweatDBms.py interactive']
try:
    action = sys.argv[1]
except:
    print("ERROR : No arguements specified")
    for i in range(0,len(help)):
        print(help[i])
    quit()
def dbcheck(db):
    if os.path.isfile(db + ".sweatdb") == False:
        print("DB not found")
        quit()
def fix(db):
    with open(db + '.sweatdb') as r, open(db + '.sweatdb', 'r+') as w:
        for line in r:
            if line.strip():
                w.write(line)
        w.truncate()
def clear():
    if os.name != "nt":
        os.system('clear')
    else:
        os.system('cls')
match action:
    case "create":
        try:
            name = sys.argv[2]
        except:
            print("ERROR : No name specified")
            quit()
        if os.path.isfile(name + ".sweatdb") == True:
            print("A database was already found with that name, would you like to overwrite it? (y) or (n)")
            option = str(input("sweatDB[" + str(os.getlogin()) + "]--> "))
            if option == "n":
                quit()
        with open(name + ".sweatdb", 'w') as f:
            f.write("DATABASE NAME : " + name + " TIME CREATED : " + str(datetime.datetime.utcnow()) + " CREATED WITH https://github.com/0xsweat/sweatDB " + version + "\n")
            f.close()
    case "help":
        try:
            helpcommand = sys.argv[2]
        except:
            for i in range(0,len(help)):
                print(help[i])
            quit()
        match helpcommand:
            case "create":
                print(help[1])
                quit()
            case "add":
                print(help[2])
                quit()
            case "help":
                print(help[3])
            case "delete":
                print(help[4])
            case "view":
                print(help[5])
            case "edit":
                print(help[6])
            case "version":
                print(help[7])
    case "delete":
        try:
            ttd = sys.argv[2]
        except:
            print("type of thing to delete was not specified")
            quit()
        try:
            db = sys.argv[3]
        except:
            print("No db name specified")
        dbcheck(db)
        if ttd == "db":
            os.remove(db + ".sweatdb")
        else:
            try:
                item = sys.argv[4]
            except:
                print("No item specified")
                quit()
            with open(db + '.sweatdb', 'r')as f:
                a = f.read()
                f.close()
            b = a.split("\n")
            c = ""
            for i in range(0,len(b)):
                d = b[i].split(" ")
                if d[0] == item:
                    b.pop(i)
                    break
            for i in range(0,len(b)):
                c = c + b[i] + "\n"
            with open(db + '.sweatdb', 'w')as f:
                f.write(c)
                f.close()
            fix(db)
            quit()
    case "add":
        try:
            valuereceive = sys.argv[2]
        except:
            print("No way to receive the value specified")
        try:
            db = sys.argv[3]
        except:
            print("No db specified")
            quit()
        try:
            name = sys.argv[4]
        except:
            print("No name specified")
            quit()
        try:
            value = sys.argv[5]
        except:
            print("No value specified")
            quit()
        dbcheck(db)
        if valuereceive == "arg":
            value = sys.argv[5:]
            newvalue = ""
            for i in range(0,len(value)):
                newvalue = newvalue + value[i] + " "
            value = newvalue
            with open(db + '.sweatdb', 'a')as f:
                f.write(name + " " + value + "\n")
                f.close()
            quit()
        elif valuereceive == "file-value":
            if os.path.isfile(value) == False:
                print("Could not find the value file")
                quit()
            with open(value, 'r')as f:
                a = f.read()
                f.close()
            b = a.split("\n")
            with open(db + ".sweatdb", 'a')as f:
                f.write(name + " " + b[0] + "\n")
                f.close()
            quit()
        elif valuereceive == "file-name":
            if os.path.isfile(name) == False:
                print("Could not find the name file")
                quit()
            with open(name, 'r')as f:
                a = f.read()
                f.close()
            b = a.split("\n")
            c = b[0].split(" ")
            value = sys.argv[5:]
            newvalue = ""
            for i in range(0,len(value)):
                newvalue = newvalue + value[i] + " "
            value = newvalue
            with open(db + ".sweatdb", 'a')as f:
                f.write(c[0] + " " + value + "\n")
                f.close()
            quit()
        elif valuereceive == "file-both":
            if os.path.isfile(name) == False:
                print("Could not find the name file")
                quit()
            if os.path.isfile(value) == False:
                print("Could not find the value file")
                quit()
            with open(value, 'r')as f:
                a = f.read()
                f.close()
            b = a.split("\n")
            with open(name, 'r')as f:
                a = f.read()
                f.close()
            b = a.split("\n")
            d = b[0].split(" ")
            with open(db + ".sweatdb", 'a')as f:
                f.write(d[0] + " " + b[0] + "\n")
                f.close()
            quit()
    case "view":
        try:
            db = sys.argv[2]
        except:
            print("No db specified")
            quit()
        try:
            option = sys.argv[3]
        except:
            print("No option specified")
            quit()
        if option == "all":
            dbcheck(db)
            with open(db + ".sweatdb", 'r')as f:
                c = f.read()
                f.close()
            print(c)
            quit()
        elif option == "item":
            try:
                name = sys.argv[4]
            except:
                print("No item specified")
                quit()
            dbcheck(db)
            with open(db + ".sweatdb", 'r')as f:
                c = f.read()
                f.close()
            b = c.split("\n")
            for i in range(1,len(b)):
                a = b[i].split(" ")
                if name == a[0]:
                    n = ""
                    for i in range(1,100000):
                        try:
                            n = n + a[i] + " "
                        except:
                            break
                    print(n)
                    quit()
        elif option == "items":
            dbcheck(db)
            with open(db + ".sweatdb", 'r')as f:
                c = f.read()
                f.close()
            a = c.split('\n')
            for i in range(1,len(a) - 1):
                b = a[i].split(" ")
                print(b[0])
            quit()
        elif option == "info":
            dbcheck(db)
            with open(db + ".sweatdb", 'r')as f:
                a = f.read()
                f.close()
            b = a.split("\n")
            print(b[0])
            quit()
    case "edit":
        try:
            db = sys.argv[2]
        except:
            print("No DB specified")
            quit()
        try:
            item = sys.argv[3]
        except:
            print("No item specified")
            quit()
        try:
            newvalue = sys.argv[4]
        except:
            print("No new value specified")
            quit()
        dbcheck(db)
        with open(db + '.sweatdb', 'r')as f:
            a = f.read()
            f.close()
        z = ""
        b = a.split("\n")
        for i in range(0,len(b)):
            c = b[i].split(" ")
            if c[0] == item:
                b.pop(i)
                value = ""
                newvalue = sys.argv[4:]
                for i in range(0,len(newvalue)):
                    value = value + newvalue[i] + " "
                newvalue = value
                b.append(item + " " + newvalue)
                break
        for i in range(0,len(b)):
            z = z + b[i] + "\n"
        with open(db + '.sweatdb', 'w')as f:
            f.write(z)
            f.close()
        fix(db)
        quit()
    case "version":
        print(version)
    case "interactive":
        prompt = "sweatDB[" + str(os.getlogin()) + "]--> "
        while True:
            command = str(input(prompt))
            if command == "quit":
                quit()
            elif command == "clear":
                clear()
            elif command != "clear" and command != "quit":
                os.system("python3 sweatDBms.py " + command)
