def print_formated(content):
    tab_i = 0
    content = content[1:]
    for letter in content:
        i = 0
        if letter not in [",", "{", "["]:
            print(letter, end="")
            i = 1
        elif (letter not in ","):
            tab_i += 4
        if(letter in ["}", "]"]):
            tab_i -= 4
        if (i != 1):
            print(letter)
            print(tab_i * " ", end="")


class Loadjson:
    def __enter__(self):
        try:
            f = open(self.file_name, "r")
            read = f.read()
        except:
            exit("File not found")
        self.fd = f
        self.file = read
        return self

    def __init__(self, file_name):
        self.file_name = file_name

    def getdata(self):
        return (self.file)
    
    def __exit__(self, *args):self.fd.close()

