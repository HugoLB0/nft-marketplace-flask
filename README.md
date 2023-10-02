# NFT Marketplace README

Welcome to the NFT Marketplace README! This NFT marketplace is a decentralized application (DApp) built using Flask, Web3, and smart contracts on the Ethereum blockchain. Below, we describe the functionalities of this NFT marketplace.


https://github.com/HugoLB0/nft-marketplace-flask/assets/66400773/34e5924d-ca86-4c60-b58c-f82b99b71c2c




## Table of Contents
- [Introduction](#introduction)
- [Functionalities](#functionalities)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This NFT marketplace is designed to allow users to buy, sell, and trade non-fungible tokens (NFTs) securely and efficiently. It leverages the power of blockchain technology to ensure transparency, ownership, and security of NFT transactions.

## Functionalities

1. **Browse NFTs**: Users can view a list of available NFTs on the main page. Each NFT is displayed with its relevant information, such as name, image, price, and owner.

2. **View NFT Details**: Users can click on an NFT to view its detailed information on a separate page. This page provides details about the NFT, including its transaction history, previous owners, and other relevant information.

3. **User Authentication**: Users can log in using their Ethereum wallet address. This authentication process is essential for interacting with the marketplace, such as buying and listing NFTs.

4. **Profile Page**: After logging in, users can access their profile page, which displays the NFTs they own. This helps users keep track of their NFT portfolio.

5. **Buy NFTs**: Users can initiate the purchase of an NFT. The application checks the buyer's Ethereum wallet balance to ensure they have sufficient funds to make the purchase.

6. **Metamask Integration**: The application integrates with Metamask for securely processing transactions. When a user decides to purchase an NFT, a transaction is sent to transfer funds from the buyer's wallet to the seller's wallet.

7. **Transaction History**: The application maintains a transaction history for each NFT, including the buyer, price, and date. This history is displayed on the NFT details page and helps users track the ownership and transaction history of an NFT.

8. **Off-Chain NFT Data**: NFT ownership and transaction history data are managed off-chain and are updated to reflect the latest changes after a successful transaction.

9. **Smart Contracts**: The application utilizes Ethereum smart contracts to facilitate secure and trustless NFT transfers.

Please refer to the code and comments in the provided code snippet for a more detailed understanding of how these functionalities are implemented.


We recommend watching the video demonstration to get a visual walkthrough of how the NFT marketplace works.

## Getting Started

To get started with this NFT marketplace, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies, including Flask and Web3.
3. Set up a suitable Ethereum provider URL in the code.
4. Run the application locally using `python app.py`.
5. Access the marketplace in your web browser at `http://localhost:5000`.

## Contributing 

Contributions to this project are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Thank you for using our NFT Marketplace! If you have any questions or need assistance, please don't hesitate to reach out.

Happy NFT trading! 🚀
