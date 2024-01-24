mysql> CREATE TABLE student (student_id INT AUTO_INCREMENT PRIMARY KEY,firstName VARCHAR(20),lastName VARCHAR(20),age INT, grade FLOAT);
Query OK, 0 rows affected (0.03 sec)

mysql> insert into student values("Alice", "Smith", 18, 95.5);
ERROR 1136 (21S01): Column count doesn't match value count at row 1
mysql> insert into student values(1,"Alice", "Smith", 18, 95.5);
Query OK, 1 row affected (0.00 sec)


mysql> update student set grade = 95.5 where firstName = "Alice";
Query OK, 0 rows affected (0.00 sec)
Rows matched: 1  Changed: 0  Warnings: 0


mysql> delete from student where lastName = 'Smith';
Query OK, 1 row affected (0.01 sec)

mysql> select * from student;
Empty set (0.00 sec)
