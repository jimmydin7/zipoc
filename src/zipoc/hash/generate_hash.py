import hashlib
import time
import random

def generate_commit_hash():
    unique_string = f"{time.time()}-{random.randint(0, 1_000_000)}"
    commit_hash = hashlib.sha1(unique_string.encode()).hexdigest()

    return commit_hash[:8]
