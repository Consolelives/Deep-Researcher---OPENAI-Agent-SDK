from pydantic import BaseModel
from agents import Agent

follow_up_decision_prompt = """
You are a researcher that decides whether we have enough information to stop researching or whether we need to generate follow-ip queries.
You will be given the original query and summaries of information found so far.

IMPORTANT: for simple factual questions(e.g What is the capital of Spain?,'What is the height of Mount Everest?') If this basic information is already present in the findings, you should NOT request 
follow up queries."

Complex questions about processes, comparisons, or multifaceted topics may need follow-ups, but simple factual questions rarely need more than one round of research.

If you think we have enough information, return should_follow-up=False. If otherwise should_follow-up=True.

If you return True, you will also need to generate 2-3 follow-up queries that address the specific gaps of the current findings

Always provide detailed reasoning for your decision.

"""

class FollowUpDecisionResponse(BaseModel):
    should_follow_up: bool
    reasoning: str 
    queries: list[str]


follow_up_decision_agent= Agent(
    name='Follow up decison Agent',
    instructions= follow_up_decision_prompt,
    output_type= FollowUpDecisionResponse,
    model='gpt-4o-mini',
)