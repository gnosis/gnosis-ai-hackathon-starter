from prediction_market_agent_tooling.deploy.betting_strategy import BettingStrategy, KellyBettingStrategy
from prediction_market_agent_tooling.markets.agent_market import AgentMarket

from trader_quickstart.agents.agent_with_tavily import AgentWithTavily


class KellyAgentWithTavily(AgentWithTavily):
    def get_betting_strategy(self, market: AgentMarket) -> BettingStrategy:
        # Kelly strategy -> https://en.wikipedia.org/wiki/Kelly_criterion
        return KellyBettingStrategy(
            max_bet_amount=10,
            max_price_impact=None,
        )