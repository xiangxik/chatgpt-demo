import redis
from redis.commands.search.field import TagField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis(host="10.0.0.4", port=6379, db=3)

INDEX_NAME = "index"                              # Vector Index Name
DOC_PREFIX = "doc:"      

# define vector dimensions
VECTOR_DIMENSIONS = 1536

import numpy as np

# instantiate a redis pipeline
pipe = r.pipeline()

# define some dummy data
objects = [
    {"name": "a", "tag": "foo"},
    {"name": "b", "tag": "foo"},
    {"name": "c", "tag": "bar"},
]

# write data
for obj in objects:
    # define key
    key = f"doc:{obj['name']}"
    # create a random "dummy" vector
    obj["vector"] = np.random.rand(VECTOR_DIMENSIONS).astype(np.float32).tobytes()
    # HSET
    pipe.hset(key, mapping=obj)

res = pipe.execute()