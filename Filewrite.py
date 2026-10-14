import os
if os.path.exits("practice.txt"):
    with open("pratice.txt","a") as file:
        content=file.read()
        print(content)
else:
    print("file doen't exist")

    