# Check the file is exist or not.

import os
if os.path.isfile("data.txt"):
    f=open("data.txt")
    f.close()
else:
    print("File is not exist")


