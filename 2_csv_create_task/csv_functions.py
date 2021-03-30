import csv

'''
# открытие - закрытие файла
f = open('filename.txt', 'r')
m = f.read()
f.close()

# менеджер контекста with
with open('filename.txt', 'r') as f:
    m = f.read()
'''

def write_rows_to_csv(file, rows):
    # запись в csv файл
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def read_rows_from_csv(file):
    rows = []
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows

def delete_task_by_id(file, id):
    # 1) получить все строки из файла file
    # 2) найти индекс строки, которую надо удалить (ищите по id циклом for)
    # 3) удалить эту строку из списка
    # 4) записать новый список обратно в файл (затирая все данный из файла (используйте 'w'))
    pass

write_rows_to_csv('db2222222.csv', [[1, 2]])
