import sqlite3
from pprint import pprint

DB_PATH = 'schools_db'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    # homework 23
    # create table
    query = """
        CREATE TABLE IF NOT EXISTS city_schools(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            address TEXT NOT NULL,
            floors INTEGER CHECK (floors > 1)  
        );
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            surname TEXT NOT NULL,
            name TEXT NOT NULL,
            specialization TEXT,
            school_id INTEGER,
            FOREIGN KEY (school_id) REFERENCES city_schools(id)      
        )
    """
    cursor.executescript(query)

    # add one school data
    address = 'Govorovo 3'
    floors = 2
    values = [address, floors]
    query = """
            INSERT INTO city_schools(address, floors)
            VALUES (?, ?)
    """
    cursor.execute(query, values)

    # add one student data
    surname = 'Ponchinskiy'
    name = 'Ponchik'
    specialization = ''
    school_id = 1
    values = [surname, name, specialization, school_id]
    query = """
            INSERT INTO students(surname, name, specialization, school_id)
            VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, values)

    # add some school data
    values = [
        ('Tenchitskaja 10', 3),
        ('Pinchinskaja 6', 2),
        ('Honskaja 9', 2),
    ]
    query = """
            INSERT INTO city_schools(address, floors)
            VALUES (?, ?)
    """
    cursor.executemany(query, values)

    # add some student data
    values = [
        ('Nopnin', 'Ivan', '', 4),
        ('Cinchik', 'Sasha', 'ecologist', 1),
        ('Kofanija', 'Dasha', '', 3),
        ('Nopnin', 'Ivan', '', 4),
        ('Cinchik', 'Sasha', 'ecologist', 1),
        ('Kofanija', 'Dasha', '', 3),
        ('Nopnin', 'Ivan', '', 4),
        ('Cinchik', 'Sasha', 'ecologist', 2),
        ('Kofanija', 'Dasha', '', 2),
        ('Nopnin', 'Ivan', '', 3),
        ('Cinchik', 'Sasha', 'ecologist', 4),
        ('Kofanija', 'Dasha', '', 1),
    ]
    query = """
            INSERT INTO students(surname, name, specialization, school_id)
            VALUES (?, ?, ?, ?)
    """
    cursor.executemany(query, values)

    # read data
    query = """
        SELECT surname, name, specialization, school_id
        FROM students
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=70)

    111
    # homework 24
    # READ
    # left join
    query = """
        SELECT students.id, school_id, city_schools.id, city_schools.address, city_schools.floors
        FROM students
        LEFT JOIN city_schools
        ON students.school_id = city_schools.id
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=100)

    # UPDATE
    # add column
    query = """
        ALTER TABLE students
        ADD COLUMN phone TEXT
    """
    cursor.execute(query)

    # add phone
    query = """
            UPDATE students
            SET
                phone = '38099659418'
            WHERE id = 5

        """
    cursor.execute(query)

    # DELETE
    query = """
            DELETE FROM STUDENTS
            WHERE id >= 2 AND id <= 4
        """

    cursor.execute(query)

    # READ BY DESC
    query = """
        SELECT id, surname, name, specialization, school_id
        FROM students


        ORDER BY students.id DESC
        LIMIT 3
        OFFSET 2
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=80)














