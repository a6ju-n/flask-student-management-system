import sqlite3

conn = sqlite3.connect("dbase.db")
cursor = conn.cursor()

students = [
    (102, 'Arun',    'CSE',   78, 'arun102'),
    (103, 'Meena',   'ECE',   82, 'meena103'),
    (104, 'Suresh',  'MECH',  69, 'suresh104'),
    (105, 'Divya',   'IT',    91, 'divya105'),
    (106, 'Rakesh',  'EEE',   74, 'rakesh106'),
    (107, 'Kavya',   'CSE',   88, 'kavya107'),
    (108, 'Manoj',   'CIVIL', 65, 'manoj108'),
    (109, 'Priya',   'IT',    93, 'priya109'),
    (110, 'Nithin',  'ECE',   79, 'nithin110'),
    (111, 'Asha',    'CSE',   85, 'asha111'),
    (112, 'Rahul',   'MECH',  72, 'rahul112'),
    (113, 'Neha',    'IT',    90, 'neha113'),
    (114, 'Ajay',    'EEE',   68, 'ajay114'),
    (115, 'Pooja',   'ECE',   81, 'pooja115'),
    (116, 'Sanjana', 'CSE',   95, 'sanjana116'),
    (117, 'Vikas',   'CIVIL', 70, 'vikas117'),
    (118, 'Ritu',    'IT',    87, 'ritu118'),
    (119, 'Amit',    'MECH',  76, 'amit119'),
    (120, 'Bhavya',  'CSE',   92, 'bhavya120'),
    (121, 'Kunal',   'EEE',   73, 'kunal121')
]

cursor.executemany(
    "INSERT INTO student (ID, Name, Department, Mark, pwd) VALUES (?, ?, ?, ?, ?)",
    students
)

conn.commit()
conn.close()

print("✅ 10 students inserted successfully")
