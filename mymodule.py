import sqlite3


first_time_list = []
conn = sqlite3.connect('bot/base.db',check_same_thread = False)
cursor = conn.cursor()
def put_id(uids:int):    
    print(uids)
    try:
        cursor.execute("INSERT INTO users (id) VALUES('{}')".format(uids))
    except Exception:
        print("Такой id уже существует")
    conn.commit()
    

def proverka_id(uid:int):   
    
    put_id(uids = uid)
    
        

def update_status(uid:int,st:str):
    cursor.execute("UPDATE users SET status == ? WHERE id == ?", (st,uid,))
    conn.commit()
def status_check(uid:int,st:str):
    cursor.execute("SELECT status FROM users WHERE id==?",(uid,))
    if cursor.fetchone() is None:
        print("Нет статуса")
    elif cursor.fetchone() != st:
        print("статус был изменем")
        update_status(uid=uid,st=st)
def update_location(uid,lat,lon):
    cursor.execute("SELECT user_latitude FROM users WHERE id==?", (uid,))
    if cursor.fetchone is None:
        print("None Latitude")
    elif cursor.fetchone() != lat:
        cursor.execute("UPDATE users SET user_latitude==? WHERE id == ?", (lat, uid,))
        conn.commit()
        print("Lat Was Updated")

    cursor.execute("SELECT user_longtitude FROM users WHERE id == ?", (uid,))
    
    if cursor.fetchone is None:
        print("This user haven't location")
    elif cursor.fetchone!= lon:

        cursor.execute("UPDATE users SET user_longtitude == ? WHERE id == ?",(lon,uid,))
        conn.commit()  
def transition(dri:str,lll:list):
    dlist = []
    id_lat = cursor.execute("SELECT id,user_latitude,user_longtitude FROM users WHERE status == ?",(dri,))
    dlist.append(cursor.fetchall())
    x = len(dlist[0])
    for i in range(x):
        tmp = []
        for y in range(3):
            x = dlist[0][i][y]
            tmp.append(x)
        print(tmp)
        lll.append(tmp)

def get_status(uid:int):
    dlist = []
    id_lat = cursor.execute("SELECT status FROM users WHERE id == ?", (uid,))
    dlist.append(cursor.fetchall())
    return(dlist[0][0][0])

def unvailable(uid:int):
    newlat = 0.0
    newlon = 0.0
    cursor.execute("UPDATE users SET user_latitude == ? WHERE id == ?", (newlat, uid,))
    conn.commit()
    cursor.execute("UPDATE users SET user_longtitude == ? WHERE id == ?", (newlon, uid,))
    conn.commit()

def close():
    cursor.close()
    conn.close()