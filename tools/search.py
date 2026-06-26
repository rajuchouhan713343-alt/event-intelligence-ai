from duckduckgo_search import DDGS
from core.models import SearchResult
from loguru import logger


class SearchTool:

    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query: str, max_results: int = 10):

        logger.info(f"Searching: {query}")

        results = []

        try:

            search_results = self.ddgs.text(
                keywords=query,
                max_results=max_results
            )

            for item in search_results:

                results.append(
                    SearchResult(
                        title=item.get("title", ""),
                        url=item.get("href", ""),
                        snippet=item.get("body", "")
                    )
                )

        except Exception as e:

            logger.error(e)

        logger.success(f"Found {len(results)} results")

        return results
