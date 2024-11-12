# Gnosis AI Scratch Pad

Welcome to the Gnosis AI Scratch Pad repo! 

Here you will find all you need to build a tool for AI Agents that can make predictions on outcomes of future events.

Follow the instructions below to get started.

## Support

Contact us at https://t.me/+Fb0trLKZdMw2MTQ8 or via the Gnosis Discord (channel gnosis-ai).

## Setup

Install the project dependencies with `poetry`, using Python 3.10 (you can use [pyenv](https://github.com/pyenv/pyenv) to manage multiple Python versions):

```bash
python3.10 -m pip install poetry
python3.10 -m poetry install
python3.10 -m poetry shell
```

Copy `.env.example` to `.env` and fill in the values:

### OpenAI API key

We will provide you with OpenAI key that's allowed to use gpt-3.5-turbo and embedding models, contact us on the TG group above.

However, everyone is welcome to use arbitrary LLM if wanted.

### Tavily API key

Create a free acount on https://tavily.com and get the key there.

Again, everyone is welcome to use arbitrary search engines, combine them, or even do a totally different approaches!

### Private key on Gnosis Chain

Use your existing or create a new wallet on Gnosis Chain. 

By default the script will do only very tiny bets (0.00001 xDai per market), but of course, you can contact us on the TG group above with your public key to get some free xDai.

## Task

Implement the agent in `main.py` using [the PMAT library](https://github.com/gnosis/prediction-market-agent-tooling) and feel free to take the inspiration from [the existing agents ](https://github.com/gnosis/prediction-market-agent).
