import psycopg2
from src.connconfig import configure

class TestPractice():
    @classmethod
    def setup_class(cls):
        """
        """
        cls.conn = psycopg2.connect(dbname='practice', **configure())
        cls.cur = cls.conn.cursor()  

    @classmethod
    def teardown_class(cls):
        """
        """ 
        cls.cur.close()
        cls.conn.close()

    def test_contents(self):
        self.cur.execute( '''
           select first_name from students
           where first_name = 'Violet' 
        ''')
        expected = self.cur.fetchone()[0]
        actual = 'Violet'
        assert expected == actual

    def test_quantity(self):
        self.cur.execute( '''
            select count(student_id) as cnt from students
        ''')
        expected = self.cur.fetchone()[0]
        assert expected >= 10     
