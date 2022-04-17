# import psycopg2
#
# con = psycopg2.connect(database='', user='', password='', host='', port='')
# print('Database opened successfully')
#
# cur = con.cursor()
# # cur.execute('''CREATE TABLE STUDENT
# #       (ADMISSION INT PRIMARY KEY     NOT NULL,
# #       NAME           TEXT    NOT NULL,
# #       AGE            INT     NOT NULL,
# #       COURSE        CHAR(50),
# #       DEPARTMENT        CHAR(50));''')
# print("Table created successfully")
#
# con.commit()
#
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'john', 18, 'Computer Science', 'ICT')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')");
#
# con.commit()
# print("Record inserted successfully")
#
# cur.execute("SELECT * FROM STUDENT")
# rows = cur.fetchall()
#
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[3])
#     print("DEPARTMENT =", row[4], "\n")
# print("Operation done successfully")
# con.close()
#
#
