import ItemDB
from fuzzywuzzy import fuzz


class Engine:
    def __init__(self):
        self.db = ItemDB()
        self.index = [i for i in self.db.keys() if i not in ["name", "version"]]

    def search(self, query):
        results = []
        smallest_fuzz = 0
        for i in self.index:
            for j in range(len(self.db[i])):
                current_values = self.db[i][j].values()
                for k in current_values:
                    if fuzz.ratio(query, k) == smallest_fuzz:
                        results.append(self.db[i][j]["id"])
                    elif fuzz.ratio(query, k) > smallest_fuzz:
                        results = [self.db[i][j]["id"]]
                        smallest_fuzz = fuzz.ratio(query, k)
        return results
