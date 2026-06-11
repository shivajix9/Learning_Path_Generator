from langchain_core.runnables import RunnableLambda

from prompts import learning_path_prompt
from parser import parser
from model import llm


learning_path_chain = (
    learning_path_prompt
    | llm
    | parser
)