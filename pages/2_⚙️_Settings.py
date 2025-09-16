import streamlit as st

st.title("⚙️ Account Center")
st.markdown("Let's get your account set up!")
st.write("---")

# Inject custom CSS for the card-like effect
st.markdown("""
<style>
	.card {
		background-color: #242526;
		border-radius: 10px;
		padding: 25px;
		box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
		transition: 0.3s;
	}
	.card:hover {
		box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
	}
	.metric-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
	}
</style>
""", unsafe_allow_html=True)


with st.container():
	st.markdown('<div class="card">', unsafe_allow_html=True)
	
	st.subheader("Usage Statistics")
	st.caption("See your current usage here. Resets on the 1st of the month.")

	col1, col2 = st.columns(2)
	with col1:
		st.metric(label="Chat Messages", value="35 / 50")
		st.metric(label="Training Characters", value="120K / 500K")
		st.metric(label="Ticket Forms", value="0 / 1")
	with col2:
		st.metric(label="Smart Suggestions", value="23 / 25")
		st.metric(label="Chatbots", value="1 / 2")
		st.metric(label="Team Member", value="0 / 1")
	
	st.write("---")
	
	st.subheader("Settings")
	
	# The toggle from the user request
	st.toggle("Enable Dark Mode", value=True, help="Theme is currently set globally in config.toml. This is a UI placeholder.")
	st.selectbox("Notification Preference", ["Email", "In-app", "None"])
	
	st.markdown('</div>', unsafe_allow_html=True)
