import pickle

dbfilename = 'test3_4.dat'
scdb_total = []


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []

    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    for p in scdb:
        scdb_age = int(p['Age'])
        scdb_score = int(p['Score'])
        scdb_total.append({'Name': p['Name'], 'Age': scdb_age, 'Score': scdb_score})
    return scdb_total


# write the data into person db
def writeScoreDB(scdb_total):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb_total, fH)
    fH.close()


def doScoreDB(scdb_total):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb_total += [record]
            except IndexError:
                print("이름과 나이, 점수를 입력하세요")
        elif parse[0] == 'del':
            try:
                for p in scdb_total:
                    if p['Name'].lower() == parse[1].lower():
                        scdb_total.remove(p)
            except IndexError:
                print("이름을 입력하세요")
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb_total, sortKey)
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    print("Age=" + p['Age'], "Name=" + p['Name'], "Score=" + p['Score'])
        elif parse[0] == 'inc':
            for p in scdb_total:
                if p['Name'] == parse[1]:
                    num = parse[2]
                    intnum = int(num)
                    p['Score'] += intnum
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb_total, keyname):
    for p in sorted(scdb_total, key=lambda person: person[keyname]):

        for k, v in p.items():
            if type(v) == int:
                print(k + '=%d' % v, end=' ')
            else:
                print(k + '=' + v, end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
