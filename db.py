import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               database='db',
                               user='root',
                               password='helenSHARMILA777')

my_cursor = mydb.cursor()
#my_cursor.execute("SHOW DATABASES")


def add_std():
    # print("Enter student ID")
    # id = int(input())
    print("Enter student name")
    name = input()
    print("Enter Department name")
    dpt_name = input()
    print("Enter College name")
    clg_name = input()
    print("Enter Mark 1")
    m1 = int(input())
    print("Enter Mark 2")
    m2 = int(input())
    print("Enter Mark 3")
    m3 = int(input())
    print("Enter Mark 4")
    m4 = int(input())
    print("Enter Mark 5")
    m5 = int(input())
    print("Total mark")
    tot_mrk = m1 + m2 + m3 + m4 + m5
    print (tot_mrk)
    print("Average")

    avg = tot_mrk // 5
    print (avg)
    if avg >= 91 and avg <= 100:
        grade = "A"
    elif avg >= 71 and avg <= 91:
        grade = "B"
    elif avg >= 51 and avg <= 71:
        grade = "C"
    else:
        grade = "FAIL"

    print(grade)

    mydb = mysql.connector.connect(host='localhost',
                                   database='db',
                                   user='root',
                                   password='helenSHARMILA777')

    my_cursor = mydb.cursor()

    query = """ INSERT INTO db.student_data (STUDENT_NAME, DEPARTMENT_NAME, COLLEGE_NAME, M_1,M_2,M_3,M_4,M_5,TOTAL_MARK, AVERAGE, GRADE) VALUES ( %s , %s , %s , %s , %s , %s , %s, %s, %s, %s,%s)"""
    record = (name, dpt_name, clg_name, m1, m2, m3, m4, m5, tot_mrk, avg,grade)
    my_cursor.execute(query,record)
    mydb.commit()
    print("Record inserted successfully into Student Data table")


    #for i in my_cursor:
     #     print(i)


# CREATE TABLE student_data (STUDENT_ID INT AUTO_INCREMENT primary key, VARCHAR(20) not null, VARCHAR(20) not null,  VARCHAR(20) not null, M_1 INT,M_2 INT,M_3 INT,M_4 INT,M_5 INT,TOTAL_MARK FLOAT,AVERAGE FLOAT,GRADE varchar(1));

def std_id(ele):
    #print ("Enter Student ID")


    mydb_1 = mysql.connector.connect(host='localhost',
                                   database='db',
                                   user='root',
                                   password='helenSHARMILA777')

    cursor_1 = mydb_1.cursor(prepared=True)
  #  cursor_2 = mydb_1.cursor(prepared=False)
    sql_query = """Select * from student_data where STUDENT_ID = %s"""
   # sql_query1 = """Select * from student_data where STUDENT_ID != %s"""
    cursor_1.execute(sql_query, (ele,))
    result = cursor_1.fetchall()

    if len(result) == 0 :
        print("Enter Valid Student ID")

    else:
     for i in result:
          print(i)






def std_det():

    mydb_2 = mysql.connector.connect(host='localhost',
                                     database='db',
                                     user='root',
                                     password='helenSHARMILA777')

    cursor_2 = mydb_2.cursor(prepared=True)
    #  cursor_2 = mydb_1.cursor(prepared=False)
    sql_query2 = """Select * from student_data"""
    # sql_query1 = """Select * from student_data where STUDENT_ID != %s"""
    cursor_2.execute(sql_query2)

    result1 = cursor_2.fetchall()

    for j in result1:
        print(j)


def upd_std(st_id):
    print("Enter student name")
    name = input()
    print("Enter Department name")
    dpt_name = input()
    print("Enter College name")
    clg_name = input()
    print("Enter Mark 1")
    m1 = int(input())
    print("Enter Mark 2")
    m2 = int(input())
    print("Enter Mark 3")
    m3 = int(input())
    print("Enter Mark 4")
    m4 = int(input())
    print("Enter Mark 5")
    m5 = int(input())
    print("Total mark")
    tot_mrk = m1 + m2 + m3 + m4 + m5
    print(tot_mrk)
    print("Average")

    avg = tot_mrk // 5
    print(avg)
    if avg >= 91 and avg <= 100:
        grade = "A"
    elif avg >= 71 and avg <= 91:
        grade = "B"
    elif avg >= 51 and avg <= 71:
        grade = "C"
    else:
        grade = "FAIL"

    print(grade)

    mydb_3 = mysql.connector.connect(host='localhost',
                                     database='db',
                                     user='root',
                                     password='helenSHARMILA777')

    cursor_3 = mydb_3.cursor(prepared=True)
    sql_query3 = """UPDATE student_data SET STUDENT_NAME = %s,  DEPARTMENT_NAME = %s,  COLLEGE_NAME =%s, M_1 = %s, M_2 = %s, M_3 = %s , M_4 = %s,M_5= %s,TOTAL_MARK= %s, AVERAGE= %s, GRADE= %s WHERE STUDENT_ID = %s"""
    record1 = (name, dpt_name, clg_name, m1, m2, m3, m4, m5, tot_mrk, avg,grade,st_id)
    cursor_3.execute(sql_query3,record1)
    mydb_3.commit()
    print("Successfully Updated")

    result3 = cursor_3.fetchall()


      for k in result3:
         print(k)


def del_std(ele2):
    mydb_4 = mysql.connector.connect(host='localhost',
                                     database='db',
                                     user='root',
                                     password='helenSHARMILA777')

    cursor_4 = mydb_4.cursor(prepared=True)
    sql_query4 = """DELETE FROM student_data WHERE STUDENT_ID = %s"""
    cursor_4.execute(sql_query4, (ele2,))
    mydb_4.commit()
    print("Successfully Deleted")


while True:
    print("\nMAIN MENU")
    print("1. Add Student")
    print("2. Get a Student ID")
    print("3. Get all Student")
    print("4. Update Student")
    print("5. Delete a Student")
    print("6. Exit")
    choice = int(input("Enter the Choice:"))

    if choice == 1:
        add_std()
    elif choice ==2:
        print("Enter the Student ID")
        stud_id = int(input())
        std_id(stud_id)

    elif choice == 3:
        print ("Get all Students Detials")
        std_det()

    elif choice == 4:
        print("Enter Student ID to update the details")
        ele1 = int(input())
        upd_std(ele1)

    elif choice == 5:
        print("Enter Student ID to delete the details")
        ele2 = int(input())
        del_std(ele2)

    else:
        exit()

# for i in my_cursor:
#    print(i)
