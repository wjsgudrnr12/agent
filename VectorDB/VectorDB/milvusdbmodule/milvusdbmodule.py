import json
from tqdm import tqdm
from fastapi import FastAPI, HTTPException
from VectorDB.milvusdbmodule.milvus import Milvus, DataProcess
from models import Document, File, Query
from modulemanager import classregistry

@classregistry.register('milvusdb', )
class MilvusdbModule:
    def __init__(self, name):
        self.name = name
        self.milvus = Milvus()
        self.dataProcess = DataProcess()
        pass

    def some_method(self):
        pass

    def load(self, file: File, collection):
        filename = file.filename
        try:
            content = file.file.read()
            data = json.loads(content)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON file")
        print(collection.value)
        if collection.value == 'grepp':
            self.dataProcess.insert_grepp(data)
        if collection.value == 'leetcode':
            self.dataProcess.insert_leetcode(data)
        if collection.value == 'robotics':
            self.dataProcess.insert_robotics(data)
        if collection.value == 'suresoft':
            self.dataProcess.insert_suresoft(data)
        if collection.value == 'solutions':
            self.dataProcess.insert_solutions(data)

        return {
            "filename": filename
        }
    
    def query(self, query, collection) -> list[Document]:
        print(collection.value)
        coll = self.milvus.connect_collection(collection.value)
        result = self.milvus.search(coll, query.query, query.top_k)

        return result
    