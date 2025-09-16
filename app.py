import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
	page_title="FloatChat",
	page_icon="🌊",
	layout="wide",
	initial_sidebar_state="expanded"
)

# --- SIDEBAR ---
with st.sidebar:
	st.title("🌊 FloatChat")
	st.write("---")
	# You can add more navigation or info here if needed in the future

	# Placeholder for user profile at the bottom
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("---")
	st.info("👤 User: Oceanographer")


# --- MAIN PAGE CONTENT ---
st.title("Welcome to FloatChat! 👋")
st.markdown("Your Conversational Gateway to ARGO Ocean Data.")
st.write("---")

st.header("About This Project")
st.info(
	"FloatChat is an AI-powered chatbot designed to make exploring complex ARGO oceanographic data "
	"as simple as asking a question. Select the 'Chats' page from the sidebar to start your conversation!"
)

st.header("How to Use")
st.markdown(
	"""
	1.  Navigate to the **💬 Chats** page from the sidebar on the left.
	2.  Type a question about ocean data into the chat input at the bottom.
	3.  For this demo, try asking about **'temperature'** or **'salinity'** to see a sample visualization.
	"""
)
