
import os, datetime

class Reporter:
    def __init__(self, config):
        self.config = config
        self.datadir = config['datadir']
        if not os.path.isdir(self.datadir):
            os.mkdir(self.datadir)
    def date(self):
        return datetime.datetime.now()
    def add(self, name, data):
        filename = f'{self.datadir}/{name}.log'
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                f.write(f'{self.date()} - {name} created;\n')
            print(f'New user {name}')
        with open(filename, 'a') as f:
            f.write(f'{self.date()} - {data};\n')
        return {"status": 200, "user": name}
    def get(self, name):
        filename = f'{self.datadir}/{name}.log'
        if not os.path.isfile(filename):
           return { "status": 404 }
        with open(filename, 'r') as f:
            return {"status": 200, "data": f.readlines()[-10:]}
