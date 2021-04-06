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
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def read_rows_from_csv(file):
    rows = []
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows


def get_task_index_by_id(file, id):
    tasks = read_rows_from_csv(file)
    for task in tasks:
        # [id, description]
        if int(task[0]) == id:
            return task
    return []


def delete_task_by_id(file, id):
    # 1) получить все строки из файла file
    tasks = read_rows_from_csv(file)
    # 2) найти индекс строки, которую надо удалить (ищите по id циклом for)
    i = 0
    for task in tasks:
        if int(task[0]) == id:
            break
        i += 1
    # 3) удалить эту строку из списка
    if i < len(tasks):
        del tasks[i]
        # 4) записать новый список обратно в файл (затирая все данный из файла (используйте 'w'))
        write_rows_to_csv(file, tasks)


def get_last_id(file):
    tasks = read_rows_from_csv(file)
    # id = 0
    # for task in tasks:
    #     id = tasks[0]
    # return id
    return int(tasks[-1][0])


def create_task(file, description):
    id = get_last_id(file) + 1
    task = [id, description]
    tasks = read_rows_from_csv(file)
    # добавили свой task ко всем
    tasks.append(task)
    write_rows_to_csv(file, tasks)



# rows = [
#     ['1', 'сделать 1'],
#     ['2', 'сделать 2'],
#     ['3', 'сделать 3'],
#     ['4', 'сделать 4'],
#     ['5', 'сделать 5'],
#     ['6', 'сделать 6'],
# ]

# print(get_task_index_by_id('db.csv', 7))
# delete_task_by_id('db.csv', 2)
