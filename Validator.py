from pathlib import Path
import config

class Validator:
    def __init__(self, txt):
        self.txt = txt
    

    def validate(self) -> str:
        print (self.txt)



#print (config.files)