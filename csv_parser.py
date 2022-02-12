import csv

def parse_csv() -> list:
    data = []
    with open("questions.csv") as file:
        reader = csv.reader(file, delimiter=",", quotechar="\"")
        reader = list(reader)
        line_cnt = 0
        for line in reader:
            if line_cnt == 0:
                line_cnt+=1
                continue
            data2 = {}
            for i in range(0, len(reader[0])):
                data2[reader[0][i]] = line[i]
            data.append(data2)
    return data


