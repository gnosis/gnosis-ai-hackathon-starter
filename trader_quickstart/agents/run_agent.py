import dotenv
dotenv.load_dotenv()
from prediction_market_agent_tooling.markets.markets import MarketType

from trader_quickstart.agents.coinflip import Coinflip


from prediction_market_agent_tooling.markets.omen.omen_contracts import OmenConditionalTokenContract

if __name__ == "__main__":
    print('starting script')
    # sanity check
    w3 = OmenConditionalTokenContract().get_web3()
    print(f"provider {w3.provider.endpoint_uri}")  # type: ignore

    agent = Coinflip()
    # Run once
    agent.deploy_local(market_type=MarketType.OMEN, sleep_time=0.01, timeout=0)
