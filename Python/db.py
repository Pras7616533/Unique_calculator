def fwrite(m):
    with open("db.txt", "a") as f:
        f.write(m)
        f.write("\n")
        f.close()


def fread():
    with open("db.txt", "r") as f:
        s =  f.read()
        print(s)
        f.close()
