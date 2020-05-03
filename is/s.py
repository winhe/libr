# import sqlite3
 
# conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
# cursor = conn.cursor()
 

# cursor.execute("""CREATE TABLE books2
#                   (who TEXT,avtor TEXT,book TEXT,data TEXT)
#                """)

# Вставляем данные в таблицу
# cursor.execute("INSERT INTO books2 VALUES (?,?,?,?)",['ss','sss','aa','qqq'])

# cursor.execute("DELETE FROM books2")

# # Сохраняем изменения
# conn.commit()


# for row in cursor.execute("SELECT * FROM albums ORDER by login"):
# 	print(row[1])

# print(cursor.execute("SELECT * FROM albums ORDER by login"))
# git commit -m 'dir' -a
#   324  git push origin master 
#   325  git remote add origin https://github.com/winhe/libr.git
