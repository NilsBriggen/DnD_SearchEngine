import ItemDB
from fuzzywuzzy import fuzz

class crawler:

    def __init__(self):
        self.db = ItemDB.DB
        self.to_crawl = []
        self.index = {}
        print(f"Database: {self.db['name']} | Version: {self.db['version']}")

    def crawl(self):
        print("Crawling...")
        # return keys of self.db if key not equal to "name" or "version"
        self.to_crawl = [i for i in self.db.keys() if i != "name" and i != "version"]
        for i in self.to_crawl:
            current_keys = self.db[i].keys()
            for j in current_keys:
                if j not in self.index.keys() and not j == "content":
                    self.index[j] = []
                self.index[j].append(i)
        print("Crawling complete.")

    def search(self, query):
        results = []
        smallest_fuzz = 0
        for i in self.index.keys():
            for j in self.index[i]:
                if fuzz.ratio(query, i) >= smallest_fuzz:
                    smallest_fuzz = fuzz.ratio(query, i)
                    results.append(j)
