from langgraph.graph import END, START

from .state import ProfileAgentState


def build_edges(graph):

    graph.add_edge(
        START,
        "scrape"
    )

    graph.add_edge(
        "scrape",
        "prepare_context"
    )

    graph.add_edge(
        "prepare_context",
        "extract"
    )

    graph.add_edge(
        "extract",
        "spreadsheet"
    )

    graph.add_edge(
        "spreadsheet",
        END
    )

    return graph