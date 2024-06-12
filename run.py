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
    with open("file2.csv", "w", encoding="utf8") as file:
        for i in range(split, len(lines)):
            outLine = removeChars(lines[i])
            file.write(outLine)
    return

def removeChars(line):
    allowedChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 - ! # ( ) [ ] { } . , : ^ \\ /"
    for char in line:
        if char not in allowedChars:
            print("Removing: " + char)
            line = line.replace(char, "") + "\n"
    return line

if __name__ == '__main__':
    run()
