from langgraph.graph import StateGraph

from .edges import build_edges
from .nodes import (
    scrape_node,
    prepare_context_node,
    extraction_node,
    spreadsheet_node,
)
from .state import ProfileAgentState


def create_profile_graph():

    graph = StateGraph(ProfileAgentState)

    graph.add_node(
        "scrape",
        scrape_node
    )

    graph.add_node(
        "prepare_context",
        prepare_context_node
    )

    graph.add_node(
        "extract",
        extraction_node
    )

    graph.add_node(
        "spreadsheet",
        spreadsheet_node
    )

    graph = build_edges(graph)

    return graph.compile()