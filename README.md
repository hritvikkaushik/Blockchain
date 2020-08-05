# Blockchain using Python

This personal project implements a functioning blockchain, to serve as a tool for me to grasp their working and build an understanding of the concept. 

## About Blockchain

Blockchain is the technology on which cryptocurrencies work. It's an immutable, sequential chain of records that contains the transactions. Data or files can be contained in it too. The tech makes use of hashes to chain the records together.

## Libraries and technologies used
* Python3 is the base programming language for this project.
* 'Requests' library and 'Flask' Framework of Python3 are used to create an API to access the blockchain over the network using HTTP requests.

## Features/functionality

The Blockchain runs as a Python server on a host machine. Other nodes on the network can send HTTP requests using cURL to register on the chain. They can all request to mine a block, and can initiate transactions. The Blockchain uses a simplified Proof Of Work algorithm as this is only a demo and does not need to be as computationally intensive as the real thing. A consensus algorithm has been implemented that ensures that all the nodes are working on the correct chain. The rule used to determine the real chain is that 'The Longest Chain is the de facto one'. A conflict resolution method has been defined that replaces the current chain with the longest one.

## Learning Outcomes

This has been a huge learning project for me. I learnt about the following
* __HTTP Requests:__ While implementing the Blockchain, this became the first time I implemented a RESTful API and used one over a network. I have had no prior experience with Web Development, so this was deeply interesting.
* __Blockchain__
* __UUID:__ I came across Universally Unique Identifiers for the first time and read about them.
* __Cryptographic Hash Algorithms:__ Blockchains usually use SHA-256 or similar cryptographic hashing algorithms to maintain the integrity of the chain. I read about these algorithms after coming across this concept.

## Tutorial Followed

The main guide behind this implementation was the excellent 'Learn Blockchains by Building One' from HackerNoon.com at https://hackernoon.com/learn-blockchains-by-building-one-117428612f46.

In addition to this, I watched several videos and read multiple articles and documentations for all the libraries and terminologies that were new to me, such as uuid, Flask, requests, cryptographic hash functions, etc.