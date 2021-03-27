# chainlink-iris

## Use Cases

- Automated text, voice, and video messaging of blockchain transaction events.
  This technology can be useful in creating replayable audio communications for
  those who may be hard of hearing or those who are blind and find value in the
  alternative means of communication.
- Americans with Disabilities Act (ADA) compliance
- TTY integration
- 

## Installation

```sh
git clone https://github.com/GMSteuart/chainlink-iris.git
cd chainlink-iris
cp .env.example .env
# update .env file accordingly
# load in env variables
source .env

# launch local eth instance
ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie --fork https://mainnet.infura.io/v3/$WEB3_INFURA_PROJECT_ID --chainId 1

# spin up application services
docker-compose up -d
```