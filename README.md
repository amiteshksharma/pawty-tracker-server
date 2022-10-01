# pawty-tracker-server

Server to control all backend features of the pawty tracker app. 

To run in the special environment, run the following commands

```
python3 -m venv .venv
source .venv/bin/activate
```

if on windows, run this command instead:

`
.\.venv\Scripts\activate.ps1
`

To run the server, type the following command:

`python -m flask run`

libraries:
    - flask
    - sqlalchemy
    - psycopg2-binary
    - flask_sqlalchemy
    - flask-cors

## Connecting to the SQL databse

```
engine:[//[user[:password]@][host]/[dbname]]


engine -> postgresql
user -> postgres (see `owner` field in previous screenshot)
password -> password (my db password is the string, `password`)
host -> localhost (because we are running locally on out machine)
dbname -> flasksql (this is the name I gave to the db in the previous step)
```
