class SaveResult(object):
    def save_to(self, format="json", string=""):
        try:
            if format == "json":
                file = open('history.json', 'a')
                file.write(string + "\n")
            else:
                file = open('history.xml', 'ab')
                file.write(string)
        except:
            print("can not write to file")
        else:
            print("thank you, your data was recorded")
        finally:
            file.close()