import os

os.environ["LANGCHAIN_HANDLER"] = "langchain"
os.environ['OPENAI_API_KEY'] = "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"

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis

embeddings = OpenAIEmbeddings()

rds = Redis.from_existing_index(embedding=embeddings, redis_url="redis://10.0.0.4:6379",  index_name='link')
print(rds.index_name)

#query = "What did the president say about Ketanji Brown Jackson"
#results = rds.similarity_search(query)
#print(results[0].page_content)

#print(rds.add_texts(["Ankush went to Princeton"]))

#query = "Princeton"
#results = rds.similarity_search(query)
#print(results[0].page_content)

query = "What did the president say about Ketanji Brown Jackson"
results = rds.similarity_search(query)
print(results[0].page_content)