# Start Commands

## To start the Mongo Server

1. cd <mongodb installation dir>/bin
2. mongo
3. use SoftwareEngineering
4. db.createCollection("ArtRepo",{capped:true, size:50000})
5. db.ArtRepo.createIndex( { Title: "text", Description: "text" } )
6. exit
7. mongod

## To finish installing the project

1. cd <project installation dir>
2. pipenv install
3. cd frontend
4. npm install

## To start the Flask APIs

1. cd <project installation dir>
2. pipenv run python RunBoth.py

## To start the React app

1. cd <project installation dir>
2. cd frontend
3. npm run start-pc (make sure you have your env vars set in this command)
4. SAMPLE COMMAND: "start-pc": "set CLIENT_ID=(Your client ID) OKTA_DOMAIN=(Your Okta domain)/ PORT=8080&& react-scripts start"
  
## To Bulk Load

1. cd <project installation dir>
2. cd DailyServer
3. cd GetData
4. pipenv run python BulkLoad.py (may have to update hard-coded dates)
