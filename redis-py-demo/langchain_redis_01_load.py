import os
#import getpass

os.environ["LANGCHAIN_HANDLER"] = "langchain"
os.environ['OPENAI_API_KEY'] = "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" #getpass.getpass('OpenAI API Key:')

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.redis import Redis

from langchain.document_loaders import TextLoader

loader = TextLoader('data/state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

rds = Redis.from_documents(docs, embeddings, redis_url="redis://10.0.0.4:6379",  index_name='link')
print(rds.index_name)
