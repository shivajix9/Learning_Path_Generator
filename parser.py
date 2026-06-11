from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class LearningPathOutput(BaseModel):

    learning_stages: list[str] = Field(
        description="Stage wise learning roadmap"
    )

    key_topics: list[str] = Field(
        description="Important topics to learn"
    )

    learning_goal_summary: str = Field(
        description="Summary of learning goal"
    )


parser = PydanticOutputParser(
    pydantic_object=LearningPathOutput
)