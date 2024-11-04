import os

class Config:
    NEO4J_URI = "bolt://localhost:7687"  # Adjust if using a different port or URL
    NEO4J_USER = "neo4j"                 # Your Neo4j username
    NEO4J_PASSWORD = "password"          # Your Neo4j password

# You can load these from environment variables instead for security
