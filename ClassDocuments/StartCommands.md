# Start Commands

## To start the Mongo Server

1. cd <mongodb installation dir>/bin
2. mongo
3. user SoftwareEngineering
4. db.createCollection("ArtRepo",{capped:true, size:50000})
5. exit
6. mongod

## To finish installing the project

1. cd <project installation dir>
2. pipenv install
3. cd frontend
4. npm install

## To start the Flask APIs

1. cd <project installation dir>
2. cd Read/Write
3. set FLASK_APP=endpoints.py
4. pipenv run flask run --port 5000
5. (in another window) cd <the other API>
6. pipenv run flask run --port 5001
7. (Remember which one you picked for each)

## To start the React app

1. cd <project installation dir>
2. cd frontend
3. npm run start-pc (make sure you have your env vars set in this command)
4. SAMPLE COMMAND: "start-pc": "set CLIENT_ID=(Your client ID) OKTA_DOMAIN=(Your Okta domain)/ PORT=8080&& react-scripts start"
