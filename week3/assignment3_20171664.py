import pickle

dbfilename = 'test3_4.dat'
scdb_total = []


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []
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
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
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
            rmlist = []
            for p in scdb:
                if p['Name'] == parse[1]:
                    rmlist.append(p)
            for p in rmlist:
                scdb.remove(p)
            if not (rmlist):  # 빈 리스트는 false값을 가지므로,, rmlist가 비어있으면 프린트할것.
                print("There is no person matches with input name")
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    print("Age=" + p['Age'], "Name=" + p['Name'], "Score=" + p['Score'])
        elif parse[0] == 'inc':
            try:  # 미입력시 예외 처리
                for p in scdb_total:
                    if p['Name'] == parse[1]:  # 입력받은 이름과 같은 이름이 있으면
                        num = parse[2]  # str을 int로 바꾸어준다
                        intnum = int(num)
                        p['Score'] += intnum
                    else:
                        print("똑바로 입력하세요")
            except IndexError:
                print("이름과 합할 점수를 입력하세요")
                break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)