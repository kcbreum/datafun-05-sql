# datafun-05-sql

This project integrates Python and SQL. It demonstrates the skills needed to interact with a SQL database, including creating and managing a database, building a schema, performing various SQL operations, including queries with joins, filters, and aggregations, and logging to document the process. 

## Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell

py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt

```
## Freeze Requirements

```shell
py -m pip freeze > requirements.txt
```

## Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
```

## How to Install and Run the Project

```shell
py -m pip install pyarrow
py -m pip install pandas
py -m pip install requests
py -m pip install -r requirements.txt
py -m pip freeze > requirements.txt
```

## Specification

This project was built to the following specification:

- [datafun-03-spec](https://github.com/denisecase/datafun-05-spec)