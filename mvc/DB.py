import pandas as pd
from cassandra.cluster import Cluster

class DB():
    
    def __init__(self):
        cluster = Cluster(['127.0.0.1'],port=9042)
        self.session = cluster.connect()
        self.session.execute('USE pharmacy')
        
    def getSession(self):
        return self.session