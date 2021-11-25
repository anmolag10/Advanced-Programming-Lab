import sqlite3
db = sqlite3.connect("appointments.db")
cur = db.cursor()


def insert():
    id = int(input("\nENTER ID: "))
    name = input("ENTER NAME: ")
    age = int(input("ENTER AGE: "))
    grade = input("ENTER TIME: ")
    clas5 = input("ENTER DOCTOR: ")
    cur.execute("SELECT ID FROM APPOINTMENT WHERE ID = " + str(id) + ";")
    ifex = cur.fetchall()
    if ifex:
        print("\nID ALREADY EXISTS")
    else:
        cur.execute("INSERT INTO APPOINTMENT VALUES(" + str(id) + ",'" + str(name) +
                    "'," + str(age) + ", '" + str(grade) + "','" + str(clas5) + "');")


def delete():
    x = int(input("\nENTER ID TO DELETE: "))
    cur.execute("SELECT ID FROM APPOINTMENT WHERE ID = " + str(x) + ";")
    ifex = cur.fetchall()
    if ifex:
        cur.execute("DELETE FROM APPOINTMENT WHERE ID=" + str(x) + ";")
        print("DELETED SUCCESFULLY")
    else:
        print("ID NOT FOUND")


def update():
    x = int(input("\nENTER ID TO UPDATE: "))
    cur.execute("SELECT ID FROM APPOINTMENT WHERE ID = " + str(x) + ";")
    ifex = cur.fetchall()
    if ifex:
        id = int(x)
        name = input("ENTER NAME: ")
        age = int(input("ENTER AGE: "))
        grade = input("ENTER TIME: ")
        clas5 = input("ENTER DOCTOR: ")
        cur.execute("DELETE FROM APPOINTMENT WHERE ID=" + str(x) + ";")
        cur.execute("INSERT INTO APPOINTMENT VALUES(" + str(id) + ",'" + str(name) +
                    "'," + str(age) + ", '" + str(grade) + "','" + str(clas5) + "');")
    else:
        print("ID NOT FOUND")


def display():
    print("\nDisplaying all patients: ")
    cur.execute("SELECT * FROM APPOINTMENT;")
    for item in cur.fetchall():
        print("\nID:", item[0])
        print("NAME:", item[1])
        print("AGE: ", item[2])
        print("TIME: ", item[3])
        print("DOCTOR: ", item[4])


def search():
    x = int(input("ENTER ID TO SEARCH FOR: "))
    cur.execute("SELECT * FROM APPOINTMENT WHERE ID = " + str(x) + ";")
    for item in cur.fetchall():
        print("\nID:", item[0])
        print("NAME:", item[1])
        print("AGE: ", item[2])
        print("TIME: ", item[3])
        print("DOCTOR: ", item[4])


def main():

    cur.execute('''CREATE TABLE IF NOT EXISTS APPOINTMENT
    (ID INT PRIMARY KEY NOT NULL, 
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    TIME TEXT,
    DOCTOR TEXT);''')

    print("Choose one of the following options:\n1)INSERT\n2)DELETE\n3)UPDATE\n4)DISPLAY\n5)SEARCH\n6)EXIT")
    n = int(input("\nENTER CHOICE: "))

    if n == 1:
        insert()
    elif n == 2:
        delete()
    elif n == 3:
        update()
    elif n == 4:
        display()
    elif n == 5:
        search()
    elif n == 6:
        db.close()
        exit()

    db.commit()
    n = input("\nPRESS ENTER TO CONTINUE... ")


if __name__ == "__main__":
    while(True):
        main()
