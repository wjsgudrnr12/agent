import requests
from fastapi import FastAPI, HTTPException

class DbManager:
    def __init__(self, url, port, file):
        self.dburl = url
        self.dbport = port
        self.dbfile = file
        self.dbtargeturl = "http://{}:{}/".format(self.dburl,self.dbport)    

        self.init = False
        self.dbload()

    def dbload(self):

        try:
            
            targeturi = self.dbtargeturl+"chromadb/load"
            print(targeturi)
            # Create the payload
            payload = {"path": self.dbfile}

            # Make the POST request
            response = requests.post(targeturi, json=payload)

            response.raise_for_status()  # Raise an exception for HTTP error codes

            # Return the JSON response from the first server
            return response.json()
        except requests.HTTPError as http_err:
            if response.status_code == 400:
                raise HTTPException(status_code=400, detail=f"Bad Request: {response.text}")
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail=f"Not Found: {response.text}")
            elif response.status_code == 500:
                raise HTTPException(status_code=500, detail=f"Server Error: {response.text}")
            else:
                raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {http_err}")




    def dbquery(self, query):

        try:
            
            targeturi = self.dbtargeturl+"chromadb/query"
            print(targeturi)
            # Create the payload
            payload = {"filename": self.dbfile, "query": query.query, "top_k":1}
            print(payload)

            # Make the POST request
            response = requests.post(targeturi, json=payload)

            response.raise_for_status()  # Raise an exception for HTTP error codes

            # Return the JSON response from the first server
            return response.json()
        except requests.HTTPError as http_err:
            if response.status_code == 400:
                raise HTTPException(status_code=400, detail=f"Bad Request: {response.text}")
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail=f"Not Found: {response.text}")
            elif response.status_code == 500:
                raise HTTPException(status_code=500, detail=f"Server Error: {response.text}")
            else:
                raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {http_err}")

