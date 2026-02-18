import requests
import pandas as pd
import streamlit as st

API_KEY = "JPW3UAPVCW8TFT3T93F9D8NZ7R1QH7HNSN"

st.title("Ethereum Wallet Activity Dashboard")

wallet = st.text_input("Enter Ethereum wallet address")

if wallet:

    url = "https://api.etherscan.io/v2/api"

    params = {
        "chainid": 1,
        "module": "account",
        "action": "txlist",
        "address": wallet,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        st.write(data)  # debug

        if data.get("status") == "1" and data.get("result"):
            df = pd.DataFrame(data["result"])
            df["value"] = df["value"].astype(float) / 1e18
            df["timeStamp"] = pd.to_datetime(df["timeStamp"], unit="s")

            total_received = df[df["to"].str.lower() == wallet.lower()]["value"].sum()
            total_sent = df[df["from"].str.lower() == wallet.lower()]["value"].sum()

            st.metric("Total Transactions", len(df))
            st.metric("Total Received (ETH)", round(total_received, 4))
            st.metric("Total Sent (ETH)", round(total_sent, 4))

            st.dataframe(df[["timeStamp", "from", "to", "value"]])
            st.line_chart(df.set_index("timeStamp")["value"])
        else:
            st.error("No transactions found or invalid wallet.")

    except Exception as e:
        st.error(f"Error: {e}")
