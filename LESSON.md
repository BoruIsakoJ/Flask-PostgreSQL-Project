# Julius Code Along Postgresql

- sudo systemctl start postgresql
- sudo systemctl restart postgresql
- sudo systemctl status postgresql
- sudo systemctl stop postgresql
- sudo -u postgres psql
- sudo -u postgres createuser admin --interactive : n,y,n
- sudo -u postgres createdb school
- sudo adduser admin password: admin123
- sudo -u admin psql -d school :/conninfo ->to know the port number
- pgadmin4
- sudo passwd admin changes admin password
- sudo -u postgres psql : ALTER USER admin WITH PASSWORD 'admin123';
- install  pip install psycopg2-binary




- 