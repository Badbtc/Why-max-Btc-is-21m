<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Roboto&pause=1000&color=FF0000&width=435&lines=Bad+btc+is+Here++!" alt="Typing SVG" /></a>



<h1> Why maximum BTC is 21m blocks?</h1>

<bold>This code simulates the process of calculating the block subsidy for Bitcoin, which is the reward given to miners for adding new blocks to the blockchain. The block subsidy is halved approximately every 210,000 blocks, or about every four years, until it reaches zero, meaning no new bitcoins will be created.

The variable total keeps track of the total number of bitcoins that have been created so far, and C is the block height, which starts at 0 and increments by 1 each time through the loop. The loop runs indefinitely because of the while (True) statement, but it will eventually stop when sub becomes 0, meaning the block subsidy has reached 0.

The code calculates halving by dividing C by 210,000 and rounding down to the nearest integer. This tells us how many times the block subsidy has been halved. If halving is greater than or equal to 64, which corresponds to a block height of about 13.3 million, sub is set to 0, meaning no new bitcoins are created. Otherwise, sub is calculated by shifting the number 50,000,000 (which is the original block subsidy in satoshis) right by halving bits. This has the effect of dividing the original subsidy by 2^(halving), which is equivalent to halving the subsidy halving times.

The reason why the maximum number of bitcoins that can ever exist is 21 million is because of the design of the Bitcoin protocol. Satoshi Nakamoto, the creator of Bitcoin, chose this limit as a way to prevent inflation and ensure that the supply of bitcoins would be limited. The halving of the block subsidy every 210,000 blocks is a key feature of the protocol that gradually reduces the rate at which new bitcoins are created, eventually leading to a fixed supply.

The code in this repository is a simple way to illustrate how the block subsidy is calculated and how it gradually decreases over time. It can be used as a starting point for more complex simulations of the Bitcoin protocol, or as a way to understand how the supply of bitcoins is limited. </bold>


