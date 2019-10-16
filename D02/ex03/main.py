from json_reader import Loadjson, print_formated

if __name__ == "__main__":
    with Loadjson('list.json') as js:
        data = js.getdata()
        print_formated(data)