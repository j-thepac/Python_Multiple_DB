
## SQLITE
```sqlite:///Test.db```

## MYSQL 
1. pip3 install PyMySQL
2. docker run -d -it -p 3306:3306  -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=TestDB -e MYSQL_USER=test -e MYSQL_PASSWORD=test mysql
3. mysql+pymysql://test:test@0.0.0.0:3306/TestDB

## POSTGRES
1. pip3 install psycopg2-binary
2. docker run -d -it -p 5432:5432 -e POSTGRES_USER=test  -e POSTGRES_PASSWORD=test -e POSTGRES_DB=TestDB postgres
3. postgresql://test:test@0.0.0.0:5432/TestDB