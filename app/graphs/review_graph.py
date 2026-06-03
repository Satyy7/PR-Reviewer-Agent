from langgraph.graph import (
    StateGraph,
    END
)

from app.schemas.review_state import (
    ReviewState
)

from app.agents.security_agent import (
    security_agent
)

from app.agents.performance_agent import (
    performance_agent
)

from app.agents.quality_agent import (
    quality_agent
)

from app.agents.architecture_agent import (
    architecture_agent
)

from app.agents.aggregate_agent import (
    aggregate_agent
)


builder = StateGraph(
    ReviewState
)

builder.add_node(
    "security",
    security_agent
)

builder.add_node(
    "performance",
    performance_agent
)

builder.add_node(
    "quality",
    quality_agent
)

builder.add_node(
    "architecture",
    architecture_agent
)

builder.add_node(
    "aggregate",
    aggregate_agent
)

builder.set_entry_point(
    "security"
)

builder.add_edge(
    "security",
    "performance"
)

builder.add_edge(
    "performance",
    "quality"
)

builder.add_edge(
    "quality",
    "architecture"
)

builder.add_edge(
    "architecture",
    "aggregate"
)

builder.add_edge(
    "aggregate",
    END
)

review_graph = builder.compile()