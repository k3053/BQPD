import streamlit as st
from web3_config import web3, contract, account

# Streamlit page setup
st.set_page_config(page_title="Entity Registration - BQPD", layout="centered")
st.title("🔐 Entity Registration")
st.markdown("Register as a Paper Setter (PS) or Exam Conduction Center (ECC) to the blockchain.")
st.divider()

# --- Registration Form ---
st.subheader("📄 Register Entity")

uid = st.text_input("👤 Entity ID (UID)", placeholder="e.g., PS001 or ECC001")
entity_type = st.selectbox("🏷️ Entity Type", options=["PS", "ECC", "TA"])

if st.button("✅ Register Entity"):
    if not uid or not entity_type:
        st.warning("⚠️ Please fill in both UID and Entity Type.")
    else:
        try:
            tx_hash = contract.functions.registerEntity(uid, entity_type).transact({'from': account})
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            st.success("✅ Registered successfully!")
            st.code(f"Transaction Hash: {tx_hash.hex()}")
        except Exception as e:
            st.error(f"❌ Registration failed: {str(e)}")

st.divider()

# --- Check Entity Status ---
st.subheader("🔎 Check Entity Registration")

addr = st.text_input("🔐 Enter Ethereum Wallet Address", placeholder="e.g., 0xABC123...")
if st.button("🔍 Check Entity"):
    if not addr:
        st.warning("⚠️ Please enter a wallet address.")
    else:
        try:
            uid, entityType, isRegistered = contract.functions.getEntity(addr).call()
            if isRegistered:
                st.success("✅ Entity is registered.")
                st.markdown(f"**UID:** `{uid}`")
                st.markdown(f"**Type:** `{entityType}`")
                st.markdown(f"**Wallet Address:** `{addr}`")
            else:
                st.error("❌ This address is not registered.")
        except Exception as e:
            st.error(f"⚠️ Error occurred: {str(e)}")
