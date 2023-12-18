from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("comp-data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What is the total compensation in 2019?")
print(response)

