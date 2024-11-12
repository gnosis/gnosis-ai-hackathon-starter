## Running the agent during the workshop

- Create a copy from `.env.example` and name it `.env`
- Fill the following variables

```commandline
OPENAI_API_KEY=<provided during workshop>
TAVILY_API_KEY=<provided during workshop>
BET_FROM_PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 # from Anvil
GRAPH_API_KEY=<provided during workshop>
GNOSIS_RPC_URL=http://localhost:8545 # requires Anvil
ENABLE_CACHE=0 # to avoid doing cache optimizations
```

- Start Anvil locally using
```commandline
anvil --fork-url https://gnosis-rpc.publicnode.com 
```

- (Optional) Use the [Rivet extension](https://github.com/paradigmxyz/rivet) to debug transactions sent to Anvil. Alternatively, scan the command line for the standard output logs.