def create_prac_table():
    return '''
    create table if not exists students (
        student_id SERIAL,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        phone VARCHAR NOT NULL,
        PRIMARY KEY (student_id)
    );
    '''

def prac_insert():
    return '''
        INSERT INTO students 
        (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)
    '''
    
