import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("ETHERSCAN_API_KEY")

st.title("Ethereum Wallet Activity Dashboard")

wallet = st.text_input("Enter Ethereum wallet address")

if wallet:
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&sort=desc&apikey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()  # Parse JSON response

        # Debug output
        st.write(data)

        if data["status"] == "1" and data["result"]:
            df = pd.DataFrame(data["result"])
            df["value"] = df["value"].astype(float) / 1e18
            df["timeStamp"] = pd.to_datetime(df["timeStamp"], unit="s")

            total_received = df[df["to"].str.lower() == wallet.lower()]["value"].sum()
            total_sent = df[df["from"].str.lower() == wallet.lower()]["value"].sum()
            tx_count = len(df)

            st.metric("Total Transactions", tx_count)
            st.metric("Total Received (ETH)", round(total_received, 4))
            st.metric("Total Sent (ETH)", round(total_sent, 4))

            st.subheader("Recent Transactions")
            st.dataframe(df[["timeStamp", "from", "to", "value"]])

            st.subheader("Transaction Value Over Time")
            st.line_chart(df.set_index("timeStamp")["value"])
        else:
            st.error("No transactions found or invalid wallet.")
    except Exception as e:
        st.error(f"Error: {e}")
