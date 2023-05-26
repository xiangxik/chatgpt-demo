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

query = (
    Query("*=>[KNN 2 @vector $vec as score]")
     .sort_by("score")
     .return_fields("id", "score")
     .paging(0, 2)
     .dialect(2)
)

query_params = {
    "vec": np.random.rand(VECTOR_DIMENSIONS).astype(np.float32).tobytes()
}
result = r.ft(INDEX_NAME).search(query, query_params).docs
print(result)