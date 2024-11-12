import random

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from prediction_market_agent_tooling.config import APIKeys
from prediction_market_agent_tooling.deploy.agent import DeployableTraderAgent
from prediction_market_agent_tooling.gtypes import Probability
from prediction_market_agent_tooling.markets.agent_market import AgentMarket
from prediction_market_agent_tooling.markets.data_models import ProbabilisticAnswer
from prediction_market_agent_tooling.markets.markets import MarketType

from trader_quickstart.agents.prompts import PREDICTION_PROMPT


class LLM(DeployableTraderAgent):
    model = "gpt-4o-2024-08-06"

    def verify_market(self, market_type: MarketType, market: AgentMarket) -> bool:
        return True

    def load(self) -> None:
        super().load()
        # Make sure OPENAI_API_KEY is set on .env file.
        keys = APIKeys()
        self.agent = ChatOpenAI(
            model=self.model,
            temperature=0,
            api_key=keys.openai_api_key.get_secret_value(),
        )

    def answer_binary_market(self, market: AgentMarket) -> ProbabilisticAnswer | None:
        # Set up a parser + inject instructions into the prompt template.
        parser = PydanticOutputParser(pydantic_object=ProbabilisticAnswer)
        prediction_prompt = ChatPromptTemplate.from_template(
            template=PREDICTION_PROMPT,
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        # And a query intended to prompt a language model to populate the data structure.
        prompt_and_model = prediction_prompt | self.agent
        output = prompt_and_model.invoke({"user_prompt": market.question})
        output = parser.invoke(output)
        return output
