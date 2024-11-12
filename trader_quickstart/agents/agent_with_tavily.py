from langchain_community.retrievers import TavilySearchAPIRetriever
from langchain_core.documents import Document
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from prediction_market_agent_tooling.config import APIKeys
from prediction_market_agent_tooling.deploy.agent import DeployableTraderAgent
from prediction_market_agent_tooling.markets.agent_market import AgentMarket
from prediction_market_agent_tooling.markets.data_models import ProbabilisticAnswer
from prediction_market_agent_tooling.markets.markets import MarketType


def format_docs(docs: list[Document]) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


class AgentWithTavily(DeployableTraderAgent):
    model = "gpt-4o-mini"

    def verify_market(self, market_type: MarketType, market: AgentMarket) -> bool:
        return True

    def answer_binary_market(self, market: AgentMarket) -> ProbabilisticAnswer | None:
        parser = PydanticOutputParser(pydantic_object=ProbabilisticAnswer)

        prediction_prompt = ChatPromptTemplate.from_template(
            template="""Answer the question based only on the context provided.

        Context: {context}

        Question: {question}
        
        OUTPUT_FORMAT:
        {format_instructions}
        
        """,
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        retriever = TavilySearchAPIRetriever(
            k=3, api_key=APIKeys().tavily_api_key.get_secret_value()
        )

        llm = ChatOpenAI(model=self.model)

        chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prediction_prompt
            | llm
            | parser
        )

        result = chain.invoke(market.question)
        return result
