from tools.search import SearchTool


search = SearchTool()

results = search.search(
    "Top automobile companies in India"
)

for r in results:

    print("=" * 80)

    print(r.title)

    print(r.url)

    print(r.snippet)
