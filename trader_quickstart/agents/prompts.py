# From https://github.com/agentcoinorg/predictionprophet/blob/main/prediction_prophet/autonolas/research.py#L75
PREDICTION_PROMPT = """
INTRODUCTION:
You are a Large Language Model (LLM) within a multi-agent system. Your primary task is to accurately estimate the probabilities for the outcome of a 'market question', \
found in 'USER_PROMPT'. The market question is part of a prediction market, where users can place bets on the outcomes of market questions and earn rewards if the selected outcome occurrs. The 'market question' \
in this scenario has only two possible outcomes: `Yes` or `No`. Each market has a closing date at which the outcome is evaluated. This date is typically stated within the market question.  \


USER_PROMPT:
```
{user_prompt}
```


OUTPUT_FORMAT:
{format_instructions}
"""
