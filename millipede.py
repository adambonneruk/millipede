import re

def main():
    rule = [
        [r"[aeiou]",""],
        [r"\.","_"],
        [r" ",""],
    ]

    row = []
    file = open(r'test/foobar.txt', "r")
    for line in file:
        row.append(line.strip('\n'))
    file.close()

    rows = len(row)
    rules = len(rule)

    for i in range(0,rows):
        for j in range(0,rules):
            row[i] = re.sub(rule[j][0],rule[j][1],row[i])
        print(row[i].lower())

if __name__ == "__main__":
    main()
