class CsvReader():
    def __init__(self, file_name, sep=',', header=False, skip_top=0, skip_bottom=0):
        try: self.file = open(file_name, 'r')
        except OSError as e: self.file = None
        else:
            row = self.file.read()
            self.data = [elem.split(sep) for elem in row.splitlines()[(1 if (header) else 0) + skip_top:None if (not skip_bottom) else -skip_bottom]]
            try: assert (len(elem) == 2 for elem in self.data)
            except: print('error')
            else: self.header = row.splitlines()[0].split(sep) if (header) else None
    def __enter__(self):
        return (self if (self.file) else None)
    def __exit__(self, exception_type, exception_value, traceback):
        if (self.file):
            self.file.close()
    def getdata(self):
        return (self.data)
    def getheader(self):
        return (self.header)
