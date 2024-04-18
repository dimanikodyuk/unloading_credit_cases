import pymssql
import shutil
import os

from config import host_dlm, user_dlm, passowrd_dlm, database_dlm
conn_mssql = pymssql.connect(server=host_dlm, user=user_dlm, password=passowrd_dlm, database=database_dlm, autocommit=True)

# Папка файлу оригіналу
source_directory = ''
# Папка призначення
destination_directory = 'C:\GIT\SD-86236'
# Назва файлу оригіналу
file_name = ''
# Назва нового файлу
new_file_name = ''


# Процедура генерації списку файлів зі шляхами на копіювання
def get_doc_src():
    id_conf = []
    conf = conn_mssql.cursor()
    conf_sql = "EXEC crm..unloading_credit_cases;"
    conf.execute(conf_sql)
    res = conf.fetchall()
    conf.close()

    #for i in res:
    #    id_conf.append(i)
    return res


res = get_doc_src()
for i in res:
    print(i)
    # if i[8] == 'SIGNEDDOCS':
    #     source_directory = 'Z:\ClientsDocuments\SIGNEDDOCS'
    # elif i[8] == '':
    #     source_directory = 'Z:\ClientsDocuments'
    # else:
    #     source_directory = f'Z:\ClientsDocuments\{i[10]}'

    if i[5] == 1:
        source_directory = 'Z:\ClientsDocuments\\SIGNEDDOCS'
    elif i[5] == 2:
        source_directory = 'Z:\ClientsDocuments\F4240\\2DE60'
    elif i[5] == 3:
        source_directory = 'Z:\ClientsDocuments\F4240\\3E8'
    elif i[5] == 4:
        source_directory = 'Z:\ClientsDocuments\989680\\2F1E8'
    elif i[5] == 5:
        source_directory = 'Z:\ClientsDocuments\989680\\84148'
    elif i[5] == 6:
        source_directory = 'Z:\ClientsDocuments\989680\\B0838'
    elif i[5] == 7:
        source_directory = 'Z:\ClientsDocuments\989680\\E4C28'
    elif i[5] == 8:
        source_directory = 'Z:\ClientsDocuments\989680\\E9A48'
    elif i[5] == 9:
        source_directory = 'Z:\ClientsDocuments\989680\\25D78'
    elif i[5] == 10:
        source_directory = 'Z:\ClientsDocuments\F4240\\497C8'
    elif i[5] == 11:
        source_directory = 'Z:\ClientsDocuments\F4240\\4C2C0'
    elif i[5] == 12:
        source_directory = 'Z:\ClientsDocuments\F4240\\497C8'
    elif i[5] == 13:
        source_directory = 'Z:\ClientsDocuments\F4240\\4AF38'
    elif i[5] == 14:
        source_directory = 'Z:\ClientsDocuments\F4240\\59998'
    elif i[5] == 15:
        source_directory = 'Z:\ClientsDocuments\F4240\\41EB0'
    else:
        source_directory = 'Z:\ClientsDocuments'

    file_name = i[7]
    format_file = os.path.basename(rf'{source_directory}{file_name}')
    name_format = os.path.splitext(format_file)[1]
    new_file_name = f"{i[0]},_{i[6]}{name_format}".replace(',', '')
    source_file_path = os.path.join(source_directory, file_name)
    destination_file_path = os.path.join(destination_directory, new_file_name)  # Змінюємо назву файлу тут

    print(f'Перевірка наявності копії файлу: {destination_file_path} (Шлях оригіналу: {source_directory}\{file_name})')
    if os.path.exists(f'{destination_file_path}') == False:
        shutil.copy2(source_file_path, destination_file_path)
        print(f"Файл успішно скопійовано до: {destination_file_path}")
    else:
        print(f"Помилка копіювання файлу: {source_directory}\{file_name}, файл вже було скопійовано")
