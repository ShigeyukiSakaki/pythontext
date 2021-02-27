import re

text = "キリンは大昔から__複数名詞__の興味の対象でした。キリンは__複数名詞__\
の中で一番背が高いですが、科学者たちはそのような長い__体の一部__をどうやって習得\
したのか説明できません。キリンの身長は__数値__ __単位__ 近くあり、その高さの\
ほとんどはあしと__体の一部__によるものです" \


def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力: ".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        mls = mls.replace("\n","")
        print(mls)
    else:
        print("引数mlsが無効です")

print(text)

mad_libs(text)

