import mysql.connector
import os
import datetime
import time
import getpass

print(" \n  \t Bem Vindo. \n \n")
print("Base de dados: ")


host_endereco = input("MYSql Endereço: ")
usuario = input("Usuário: ")
senha = getpass.getpass("Senha: ")


mySQLconnection = mysql.connector.connect(
host=host_endereco,
user=usuario,
password=senha,
#  port=3306
)
datetime = time.strftime('%Y%m%d-%H%M%S')
diretorio = 'C:\igor'
diretrio_backup = diretorio + '/' + datetime

try:
    os.stat(diretrio_backup)
except:
    os.mkdir(diretrio_backup)

print("Selecione uma opção:\n")
print("(1) - Backup de Todas as bases.\n(2) - Backup customizado.\n\n")

opcao_selecionada = input("Opção: ")

if int(opcao_selecionada) == 1:
  
  cursor = mySQLconnection.cursor()
  cursor.execute("show databases")
  tables = []
  for table in cursor.fetchall():
    tables.append(table[0])
    for table in tables:

          dumpcmd = "mysqldump -v " + "-h" + host_endereco + "  " + "-u" + usuario + "  " + "-p" + senha + "  " +  str(table) + " > " + diretrio_backup + "/" + str(table) + ".sql"
          os.system(dumpcmd)

     
elif int(opcao_selecionada) == 2:
  seleciona_db = input("Selecione a base de dados:")     
  cursor = mySQLconnection.cursor()
  cursor.execute("use " + seleciona_db)

  cursor.execute("show tables")
  tables = []
  for table in cursor.fetchall():
    tables.append(table[0])
    for table in tables:
         
                  
          dumpcmd = "mysqldump -v " + "-h" + host_endereco + "  " + "-u" + usuario + "  " + "-p" + senha + "  " + seleciona_db + " --single-transaction " + str(table) + " > " + diretrio_backup + "/" + str(table) + ".sql"
          os.system(dumpcmd)

else:
  print("OPÇÃO INVALIDA!")

