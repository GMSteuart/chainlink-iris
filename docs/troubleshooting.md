# Troubleshooting

Testing Ganache Docker container is working properly

```sh
curl -X POST --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}' localhost:8545
```