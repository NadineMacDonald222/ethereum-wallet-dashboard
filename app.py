import requests
import pandas as pd
import streamlit as st

# --- Your Etherscan API key ---
API_KEY = "B79HYUGHJTR5WC16PDNWR1WTUV5H99SRRY"

st.title("Ethereum Wallet Activity Dashboard")

wallet = st.text_input("Enter Ethereum wallet address")

if wallet:
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&sort=desc&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "1":
        transactions = data["result"]

        df = pd.DataFrame(transactions)

        df["value"] = df["value"].astype(float) / 1e18
        df["timeStamp"] = pd.to_datetime(df["timeStamp"], unit="s")

        total_received = df[df["to"] == wallet]["value"].sum()
        total_sent = df[df["from"] == wallet]["value"].sum()
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
