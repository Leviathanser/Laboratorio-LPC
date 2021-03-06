from ftplib import FTP, FTP_PORT
import os
import re

def save_file(con: FTP, remote_file_path:str, local_file_path:str):
    with open(local_file_path,'wb') as local_file:
        con.retrbinary(f'RETR {remote_file_path}', local_file.write)

def get_txt_file(con: FTP, file_path:str):
    listado = []
    con.retrlines(f'RETR {file_path}', listado.append)
    return listado

def list_folder(con: FTP, directory:str):
    print(directory)
    listado = []
    con.retrlines(f'LIST {directory}', listado.append)
    print(listado)
    archivo = open('FTP_server.txt','w')
    archivo.write(str(listado))
    archivo.close()
    for i in listado:
        print(i)
    return listado

def get_file_dir(con: FTP, directory:str):
    listado = list_folder(con,directory)
    return [file_info for file_info in listado if file_info.startswith('-')], [file_info for file_info in listado if not file_info.startswith('-')]

#\
def connect_ftp(host:str, usr:str = '', pwd:str = '', save_path:str = '.'):
    connection = FTP()
    connection.connect(host=host, timeout=3)
    connection.login(usr,pwd)
    l_file, l_dir = get_file_dir(connection, 'debian')
    print(l_file,l_dir)
    #print(f'files:\n{l_file}\ndirs:\n{l_dir}')
    #print(get_txt_file(connection, 'welcome.msg'))
    file_name = 'welcome.msg'
    save_file(connection, file_name, f'{save_path}/{file_name}')
    #print(list_folder(connection, 'debian'))
    
if __name__ == '__main__':
    # connect_ftp('192.168.56.1', 8022)
    #connect_ftp('ftp.us.debian.org', '/home/w')
    connect_ftp('ftp.us.debian.org')

