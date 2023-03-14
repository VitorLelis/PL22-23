from re import search, findall
from statistics import mean
from sys import argv
from json import dump

filename = str(argv[1]) 
fh = open(filename, 'r')

first_line = fh.readline()
mode = search(r',Notas{', first_line)

data = dict()
i = 0

for line in fh:
    
    regex = r'(?P<Número>\d+),(?P<Nome>[\w|\s]+),(?P<Curso>[\w|\s]+)'
    result = search(regex,line.strip('\n'))
    data[i] = result.groupdict()

    if mode:
        grade_regex = r',(\d+)'
        grades = [int(x) for x in findall(grade_regex,line)]

        if search('sum',first_line):
            data[i]['Notas_sum'] = sum(grades)
        elif search('media',first_line):
            data[i]['Notas_media'] = mean(grades)
        else:
            data[i]['Notas'] = grades

    i += 1

fh.close()

json_file = filename.replace('.csv', '.json')

with open(json_file, "w") as outfile:
    dump(list(data.values()), outfile, indent=3, ensure_ascii=False)