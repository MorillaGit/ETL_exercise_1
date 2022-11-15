# Extract transform load (ETL)
## Introduction 

* This repository has the function of capturing, files hosted locally .csv, transform them, extracting some features of the data as an example. Then load them into a Posgres database.

## Organization

The organization of this repository is as follows:

<pre>
├───src
│   ├─── extraction.py
│   ├─── loading.py
│   ├─── setting.py
│   ├─── transformation.py
│   └─── tables.sql
├─── pyproject.toml
├─── poetry.lock
├─── README.md
└─── requirements.txt
</pre>

## Requirements

* You must have installed Docker Desktop. In case you do not have it installed, go to the following sites according to the operating system used:
    * https://docs.docker.com/desktop/install/windows-install/ for Windows
    * https://docs.docker.com/desktop/install/mac-install/ for Mac.  
    * https://docs.docker.com/desktop/install/linux-install/ for Linux.

* you must have installed Poetry. In case you do not have it installed, go to the following site: https://python-poetry.org/docs/



### Instructions

1. Clone the repository. whit command: git clone, or download the repository in zip format.
```
git clone https://github.com/MuttData/ETL_exercise_1
cd ETL_exercise_1
```
2. Open a terminal in the repository folder.

3. Run the command (if you do not have the image it will take a few minutes)

```
docker pull postgres
```

4. This comand build the image of Docker. Official image of postgres in Docker Hub https://hub.docker.com/_/postgres 

4. Execute the command
```

```docker
docker run -d -h <hostname or ip address>  -p <port>:5432 --name <name_dontainer> -e POSTGRES_USER=<User> -e POSTGRES_PASSWORD=<Password> -e POSGRES_DB=<DB> postgres
```
This command creates a Docker container with the postgres image. That will connect to the database <DB> with the user <User> and the password <Password> on the port <port> of the host. Replace the values between <> with the desired values.

[ Nota ] En caso de tener instalado un cliente de SQL como [DBeaver](https://dbeaver.io/),  o [pgAdmin](https://www.pgadmin.org/) Es posible correr las consultas SQL desde estos clientes. con las siguientes configuraciones:

[ Nota ] If you have an SQL client installed such as [DBeaver](https://dbeaver.io/), or [pgAdmin](https://www.pgadmin.org/) It is possible to run the SQL queries from these clients, whitout docker. with the following configurations:

```
Host: <localhost>
Port: <Port>
User: <User>
Password: <Password>
DB: <DB>
Schema: <Schema>
``` 
7. It is necessary to get the packages of poetry stored in the poetry.toml For this run the command

```python
poetry install 
```
```python
poetry run python <script_name>.py
```
to run the scripts. The scripts are in the src folder.
```python
poetry run python main.py
```


[ Note ] It is not necessary to use poetry, you can install the packages with pip. The packages are in the requirements.txt file. Alternative installation with Conda or pip. Using a package manager such as Conda, you can install the packages with the following command:

```python
pip install -r requirements.txt
```
In case you do not have pip installed, you can install it with the following command:

```python
python -m pip install --upgrade pip
```
Next you can install the packages with the following command:

```python
pip install -r requirements.txt
```

To use the scripts, you must run the following command:

```python
python main.py
```

## Description 
This repository has the function of capturing, files hosted locally .csv, transform them, extracting some features of the data as an example. Then load them into a Posgres database. Just for practice.