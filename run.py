#read in a large csv file, and split into two files
#for each line remove any characters that are not contained in the allowed character list
def run():
    filePath = "file.csv"
    with open(filePath, encoding="utf8") as file:
        lines = file.readlines()
    split = int(len(lines) / 2)
    with open("file1.csv", "w", encoding="utf8") as file:
        for i in range(split):
            outLine = removeChars(lines[i])
            file.write(outLine)
            if i % 100000 == 0:
                print(str(i) + "/" + str(len(lines)))
    with open("file2.csv", "w", encoding="utf8") as file:
        for i in range(split, len(lines)):
            outLine = removeChars(lines[i])
            file.write(outLine)
            if i % 100000 == 0:
                print(str(i) + "/" + str(len(lines)))
    print("done")
    return


def removeChars(line):
    allowedChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 - ! # ( ) [ ] { } . , : ^ \\ / \" \n"
    for char in line:
        if char not in allowedChars:
            print("Removing: " + char)
            line = line.replace(char, "")
    return line


if __name__ == '__main__':
    run()
