'''
database stuff class
'''
import csv
from mac import MAC


class Database:

    db_type = ''
    error = None
    dsn = ''

    ''' db handler object'''
    db = None

    def __init__(self, db_type=None, dsn=''):
        if dsn is not '':
            self.dsn = dsn

        if db_type is 'csv':
            self.db_type = 'csv'
            self.init_csv()
        else:
            self.error = 'Database error: not implemented db type'

    def init_csv(self):
        self.db = csv.DictReader(open(self.dsn))

    def find_mac_in_db(self, address):
        candidates = []
        for row in self.db:
            vendoraddress = MAC.standarize_address(row['oui'])
            if address.startswith(vendoraddress):
                candidates.append(row)

        return candidates
