# Ethereum Wallet Activity Dashboard

A **Streamlit app** to visualize Ethereum wallet transactions using the **Etherscan API**. Quickly view total transactions, ETH sent/received, recent transactions, and trends over time.

---

## Features

- Real-time wallet activity from Etherscan  
- Total ETH sent and received  
- Recent transactions table  
- Transaction value chart over time  
- Secure API key handling with `.env`

---

## Setup

1. **Clone the repo**  
git clone https://github.com/NadineMacDonald222/ethereum-wallet-dashboard.git
cd ethereum-wallet-dashboard

2. **Create and activate a virtual environment**
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Create a .env file in the project folder with your Etherscan API key:**
ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY_HERE
-------

## Run the Streamlit app:
streamlit run app.py
2. Enter an Ethereum wallet address in the input box.

3. Explore:
- Total transactions
- Total ETH sent/received
- Recent transactions table
- Transaction value over time chart
------

## Notes:
-Works best with small to medium wallets. Large wallets may load slower.
-API key is private via .env.
-Dependencies are listed in requirements.txt.
