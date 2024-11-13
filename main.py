import prediction_market_agent_tooling

import prediction_market_agent_tooling.deploy
import prediction_market_agent_tooling.deploy.agent
from dotenv import load_dotenv

load_dotenv()


class MyAgent(prediction_market_agent_tooling.deploy.agent.DeployableTraderAgent):
    """
    TODO: Implement market betting agent.
    """
