import csv

#No.1
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())

#No.2
st = open("test.txt", "w")
st.write("ken,yoshikai")
st.close()

#No.3
testList = [["Top Gun", "Risky Business", "Minority Report"],\
            ["Titanic","The Revenat","Inception"],\
            ["Training Day", "Man on Fire", "Flight"]]

with open("textCSV.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(testList[0])
    w.writerow(testList[1])

#No.4
testList = [["トップガン", "リスキービジネス", "マイノリティレポート"],\
            ["タイタニック","ザ・レヴェナント","インセプション"],\
            ["トレーニング・デイ", "マンオンファイア", "フライト"]]

with open("textCSV.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(testList[0])
    w.writerow(testList[1])

#シンプルなもの
st = open("simple.txt", "w")
st.write("Hello, World!")
st.close()

st = open("simple.txt", "r")
text = st.read()
print(text)
st.close()

#withをつけることで、close()を省略
with open("simple.txt", "w") as f:
    f.write("Hello, World!")

#withでcsv読み込み / writeとちょっと違う
with open("textCSV.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(row)