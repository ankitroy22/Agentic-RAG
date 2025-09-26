from typing import Any, Dict

from langchain.schema import Document
from langchain_tavily import TavilySearch

from graph.state import GraphState
from dotenv import load_dotenv
load_dotenv()


web_search_tool = TavilySearch(max_results=3)


def web_search(state: GraphState) -> Dict[str, Any]:
    """
    Search the web for documents.

    Args:
        state (dict): The current state of the graph.

    Returns:
        state (dict): A dictionary containing the retrieved documents and the question
    """
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state.get("documents", [])

    tavily_results = web_search_tool.invoke({"query": question})
    results_list = tavily_results.get("results", [])
    tavily_contents = [res.get("content", "") for res in results_list]
    tavily_results_joined = "\n".join(tavily_contents)

    print("Tavily results:", tavily_results)

    


    # create a document object
    web_search_result = Document(page_content=tavily_results_joined)

    # append web search to the list of documents
    if documents is not None:
        documents.append(web_search_result)
    else:
        documents = [web_search_result]

    return {"documents": documents, "question": question}
