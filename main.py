import sys
import time
import psycopg2
from src.connconfig import configure
from src.createdb import create_practice_db
from src.queries import create_prac_table, prac_insert
from src.values import values_for_inserting
from src.practicelog import get_logger

if __name__ == '__main__':

    logger = get_logger(__name__)
    logger.debug('---- Script Started ----')

    for i in range(2):
        try:
            create_practice_db()
            logger.debug('database dropped && created')
        except:
            logger.debug('unable to connect to db yet, waiting')
            time.sleep(5)

    try:
        create_practice_db()
        logger.debug('database dropped && created')
    except:
        logger.exception('unable to connect to db')
        sys.exit()

    conn = psycopg2.connect(dbname='practice', **configure())
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()    

    cur.execute(create_prac_table())

    for row in values_for_inserting:
        try:
            cur.execute(prac_insert(), row)
            logger.debug(f"inserted {', '.join(row)}")
        except:
            logger.exception('unable to insert')

    cur.close()
    conn.close()
    logger.debug('---- Script Finished ----')