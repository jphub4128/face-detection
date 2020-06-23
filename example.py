import datetime
r"""
this creates an empty file
"""
filename=datetime.datetime.now()
#create empty filename
def create_file():
    """this creates an empty file"""
    with open(filename.strftime("%y-%m-%d-%h-%M"),"w")as file:
        file.write("")

create_file()
