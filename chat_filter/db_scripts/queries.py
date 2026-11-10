
def showtablecontent(connexion, table_name):
    cursor = connexion.cursor()
    cmd_sql = f"SELECT * FROM {table_name}"
    cursor.execute(cmd_sql)
    results = cursor.fetchall()
    if not results:
        print(f"Tabela {table_name} este goală.")
        return

    for result in results:
        print(result)

#FUNCTIONS FOR CONTROLLING BAN_WORDS DATA
def wordadd(connexion, word):
    cursor = connexion.cursor()
    cmd_sql = "INSERT INTO banned_words (bannedword) VALUES (%s)"
    cursor.execute(cmd_sql, (word,))
    connexion.commit()
    print(f"I have added {word} into banned_words")

def worddelete(connexion, word):
    cursor = connexion.cursor()
    cmd_sql = "DELETE FROM banned_words WHERE bannedword=%s"
    cursor.execute(cmd_sql, (word,))
    connexion.commit()
    print(f"I have removed {word} from banned_words")

def searchword(connexion,word):
    cursor = connexion.cursor()
    cmd_sql = "SELECT * FROM banned_words WHERE bannedword=%s "
    cursor.execute(cmd_sql, (word,))
    found = cursor.fetchone()
    if found is not None : return 1
    return 0

#FUNCTIONS FOR CONTROLLING USER DATA
def checkstatus(connexion, addr):
    cursor = connexion.cursor()
    cmd_sql = "SELECT * FROM users WHERE status = 1 and username=%s"
    cursor.execute(cmd_sql, (addr,))
    status = cursor.fetchone()
    if status is None :
        return 0
    return 1

def updatestatus(connexion, addr):
    cursor = connexion.cursor()
    cmd_sql = "UPDATE users SET status = 1 WHERE username=%s"
    cursor.execute(cmd_sql, (addr,))
    connexion.commit()

def adminupdatestatus(connexion, addr):
    cursor = connexion.cursor()
    cmd_sql = "UPDATE users SET status = 1 WHERE status = 0 and username=%s"
    cursor.execute(cmd_sql, (addr,))
    connexion.commit()

def insertaddr(connexion, addr):
    cursor = connexion.cursor()
    cmd_sql = "INSERT INTO users (username) VALUES (%s)"
    cursor.execute(cmd_sql, (addr,))
    connexion.commit()
    print(f"I have added {addr} into users!")

def checkaddr(connexion, addr):
    cursor = connexion.cursor()
    cmd_sql = "SELECT * FROM users WHERE username=%s"
    cursor.execute(cmd_sql, (addr,))
    status = cursor.fetchone()
    if status is None:
        return 0
    return 1

# CHECK/UPDATE LOGS
def checklogs(connexion, addr):
    cursor = connexion.cursor()
    cmd_sql = """
        SELECT chat_logs.log, chat_logs.time 
        FROM chat_logs 
        JOIN users ON chat_logs.id_user = users.id_user 
        WHERE users.username = %s
    """
    cursor.execute(cmd_sql,(addr,))
    results = cursor.fetchall()
    if not results:
        print("No results")

    for result in results:
        print(result[0],result[1])

def insertlogs(connexion, decodedMessage, addr):
    cursor = connexion.cursor()
    cmd_sql = """
              INSERT INTO chat_logs (id_user, log) 
              VALUES ((SELECT id_user FROM users WHERE username = %s), %s)
                 """
    cursor.execute(cmd_sql, (addr, decodedMessage))
    connexion.commit()
    print(f"Logs have been updated for {addr}")
