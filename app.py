import requests
from fuzzywuzzy import fuzz
from multiprocessing import Pool
from flask import Flask, request, render_template, jsonify


baseUrl = "https://dnd5eapi.co"
categoryList = [
    "/api/ability-scores",
    "/api/alignments",
    "/api/backgrounds",
    "/api/classes",
    "/api/conditions",
    "/api/damage-types",
    "/api/equipment",
    "/api/equipment-categories",
    "/api/feats",
    "/api/features",
    "/api/languages",
    "/api/magic-items",
    "/api/magic-schools",
    "/api/monsters",
    "/api/proficiencies",
    "/api/races",
    "/api/rule-sections",
    "/api/rules",
    "/api/skills",
    "/api/spells",
    "/api/subclasses",
    "/api/subraces",
    "/api/traits",
    "/api/weapon-properties",
]


def searcher(args):
    target, query = args
    results = []
    bestFuzz = -1
    response = requests.get(baseUrl + target)
    if response.status_code == 200:
        for item in response.json().get("results", []):
            ratio = fuzz.ratio(query.lower(), item["name"].lower())
            if ratio > bestFuzz:
                bestFuzz = ratio
                results = [item]
            elif ratio == bestFuzz:
                results.append(item)
        results.append(bestFuzz)
    return results

def formatter(results):
    content = [requests.get(baseUrl + result["url"]).json() for result in results]
    print(content)
    exit()


def search(query):
    if __name__ == "__main__":
        pool = Pool()
        results = pool.map(searcher, [(target, query) for target in categoryList])
        # sort by best fuzz ratio
        results.sort(key=lambda x: x[-1], reverse=True)
        results = results[:3]
        # remove fuzz ratio
        for i in range(len(results)):
            results[i] = results[i][0]
        formatter(results)
        return results

search("fireball")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form.get('query')
        results = search(query)
    return render_template('index.html', results=results)

@app.route('/fetch', methods=['POST'])
def fetch_data():
    url = request.json.get('url')
    response = requests.get(baseUrl + url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
