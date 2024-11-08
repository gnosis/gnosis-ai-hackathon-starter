from prediction_market_agent_tooling.config import APIKeys
from prediction_market_agent_tooling.markets.omen.omen import OmenAgentMarket, get_conditional_tokens_balance_for_market
from prediction_market_agent_tooling.markets.omen.omen_contracts import OmenConditionalTokenContract
from prediction_market_agent_tooling.markets.omen.omen_subgraph_handler import OmenSubgraphHandler
from web3 import Web3


def print_positions_from_user(w3: Web3) -> None:
    better_address = APIKeys().public_key
    conditional_tokens_contract = OmenConditionalTokenContract().get_web3_contract(w3)
    ls = conditional_tokens_contract.events.TransferSingle().get_logs(
        fromBlock=w3.eth.block_number - 1)  # type: ignore[attr-defined]

    market_contract = ls[-1]['args']['operator']
    market = OmenSubgraphHandler().get_omen_market_by_market_id(Web3.to_checksum_address(market_contract))
    agent_market = OmenAgentMarket.from_data_model(market)
    positions = get_conditional_tokens_balance_for_market(market=agent_market, from_address=better_address, web3=w3)
    print(positions)
