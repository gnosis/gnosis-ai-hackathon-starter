# Important to load this before loading PMAT.
from dotenv import load_dotenv
load_dotenv()
from trader_quickstart.agents.llm_agent import LLM
from trader_quickstart.utils import print_positions_from_user
from prediction_market_agent_tooling.markets.omen.omen_contracts import (
    OmenConditionalTokenContract,
)
from prediction_market_agent_tooling.markets.markets import MarketType


if __name__ == "__main__":
    print("starting script")
    # sanity check
    w3 = OmenConditionalTokenContract().get_web3()
    print(f"provider {w3.provider.endpoint_uri}")  # type: ignore

    # agent = Coinflip()
    agent = LLM()
    # Run once
    agent.deploy_local(market_type=MarketType.OMEN, sleep_time=0.01, timeout=0)

    print_positions_from_user(w3)
    print("end")
