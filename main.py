from fastapi import FastAPI, HTTPException
import requests

from models import *
from dbmanager import DbManager

app = FastAPI()  # FastAPI 애플리케이션 인스턴스

dburl = "127.0.0.1"
dbport = "8001"
dbfile = "sample.pdf"
dbmanager = DbManager(dburl, dbport, dbfile)

@app.post("/aiagent/query")
async def query(query: AIAgentQuery):
    # Simulating file upload to the first server
    #return dbmanager.dbload()
    return dbmanager.dbquery(query)


    #make_prompt
    #mkke_result

    return "test"







if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port= 8000)