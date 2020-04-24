# MySQL database with python

## Sumário

* [Objetivo / Objectives](#Objetivo)
* [Requirementos / Requirements](#Requirements)
* [Instalação / Installation](#Installation)
* [Funções / Functions](#Function)
* [Payload](#Payload) 
* [Autor / Author](#Author)

## Objetivo <a name="objetivo"></a>
_MySQL database with python_ é um exemplo simples, em python, para fazer CRUD em um banco de dados MySQL.
O código cria uma tabela de usuário, em num database preexistente, cria uma senha criptografada, cria o registro do
usuário, seleciona os dados do usuário criado e exclui (opcional) o usuário.

_MySQL database with python_ is a simple example, in python, for CRUD in a MySQL database.
The code creates a user table, in a pre-existing database, creates an encrypted password, creates the record of
user, selects the data of the created user and excludes (optional) the user.

## Requirements <a name="Requirements"></a>
#### 1. Bibliotecas / Libraries:  
>bcrypt==3.1.7       
>cffi==1.14.0        
>password==0.2       
>pycparser==2.20     
>PyMySQL==0.9.3      
>secure-smtplib==0.1.1       
>six==1.14.0     

#### 2. Banco de Dados MySQL / MySQL database:     
>MySQL >=5.5     
>MariaDB >=5.5

## Instalação / Installation <a name="Installation"></a>
Use o **requirements.txt** para instalar as bibliotecas.

Use **requirements.txt** to install the libraries.

```
pip install -r requirements.txt
```

Clique no link para instalar o [MariaDB](https://downloads.mariadb.org/) em Linux (CentOS, Fedora, Red Hat, Debian, 
Ubuntu, openSUSE).

Click the link to install [MariaDB](https://downloads.mariadb.org/) on Linux (CentOS, Fedora, Red Hat, Debian,
Ubuntu, openSUSE).

## Funções / Functions <a name="Function"></a>
##### Função / Function 'main.py'

Exemplo para as chamadas de **criar** uma tabela de usuários, **gerar** uma senha criptografada, **criar** um registro 
de usuário na tabela de usuário, **recuperar** as informações na tabela usuário do usuário criado e **excluir** um 
registro na tabela de usuário. 
O exemplo pode ser adaptado conforme a necessidade. Por exemplo, para a criação e manipulação de outras tabelas,
basta somente alterar as entradas. 
Pode também, efetuar chamadas nas funções de forma isolada. Por exemplo, somente para inserir e/ou excluir um usuário. 

Example for calls to **create** a user table, **generate** an encrypted password, **create** a record
user in the user table, **retrieve** the information in the user table of the created user and **delete** a
record in the user table.
The example can be adapted as needed. For example, for creating and manipulating other tables,
just change the entries.
You can also make calls to the functions in isolation. For example, only to insert and / or delete a user.

##### Função / Function 'connect.py'
Efetua a conexão com o banco de dados MySQL.
As informações para acesso ao Bando de Dados estão em variáveis de ambiente. 

Connects to the MySQL database.
The information for accessing the Database is in environment variables.

```
db = pymysql.connect(host=os.environ['MYSQL_HOST'],
                     user=os.environ['MYSQL_USERNAME'],
                     password=os.environ['PASSWORD_MYSQL_USER'],
                     db=database)

```

##### Função / Function 'working_db.py'
Contém a classe com as funções que executa a criação da tabela, a criação do registro do usuário, a recuperação dos 
dados do usuário e a exclusão do usuário. 

It contains the class with the functions that perform the creation of the table, the creation of the user record, the
recovery of user data and user deletion.

```
class Execute_Sql(object):

    @staticmethod
    def create_table(database, table, query_sql):

    @staticmethod
    def insert_user(database, payload):

    @staticmethod
    def select_users(database, payload):

    @staticmethod
    def delete_user(database, username):

```  

##### Função / Function 'password.py'
Criar uma senha de 16 caracteres, insere um hash na senha e valida a senha para acesso.
É acionada pela função **'insert_user'** no momento de criar o registro do usuário na tabela de usuário.

Create a 16-character password, insert a hash in the password and validate the password for access.
It is triggered by the function **'insert_user'** when creating the user record in the user table.

```
def create_password(num_caract):


class TrataHash(object):

    @staticmethod
    def insere_hash(passwd):

    @staticmethod
    def validates_senha(password, hash_passwd):

```

## Payload <a name="Payload"></a>
O **payload** contém os dados de entrada. 
O **payload** pode ser alterado conforme a necessidade. Por exemplo, se usar o código para a criação de uma outra
tabela com o nome 'dados_cliente' que contém informação do cliente, basta alterar as entradas requeridas e usá-las 
na função 'working_db.py', conforme a necessidade. 

The **payload** contains the input data.
The **payload** can be changed as needed. For example, if you use the code to create another
table with the name 'data_client' that contains customer information, just change the required entries and use them
in the 'working_db.py' function, as needed.

```
    """
    Input data. Inserted in the frontend of the application.  
    """
    payload = {
        'database': 'cfg',
        'name_table': 'users',
        'username': 'admin',
        'email': 'admin@admin.com'
    }
```

## Autor / Author <a name="Author"></a> 
```
- Renato de Carvalho Machado (renatodicmachado@gmail.com)
```
