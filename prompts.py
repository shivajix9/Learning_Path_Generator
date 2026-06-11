from langchain_core.prompts import ChatPromptTemplate
from parser import parser


learning_path_prompt = ChatPromptTemplate.from_template(
    """
You are an expert learning roadmap generator.

Generate a structured learning roadmap.

Skill:
{skill}

{format_instructions}

Rules:

1. Create logical learning stages.
2. Create key topics.
3. Generate short learning summary.
4. Output must follow schema exactly.

""",
    partial_variables={
        "format_instructions":
        parser.get_format_instructions()
    }
)