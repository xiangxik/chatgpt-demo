import redis
r = redis.Redis(host='10.0.0.4', port=6379, db=3)
print(r.ping())

import numpy as np

# define vector dimensions
VECTOR_DIMENSIONS = 1536

print(np.random.rand(VECTOR_DIMENSIONS).astype(np.float32))