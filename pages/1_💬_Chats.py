import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import time

# --- Helper Function for Placeholder Chart ---
def generate_placeholder_chart(data_type: str):
	"""Generates a sample Plotly chart for temperature or salinity."""
	depth = np.linspace(0, 2000, 100)
	if data_type == 'temperature':
		values = 25 * np.exp(-depth / 400) + np.random.randn(100) * 0.5
		df = pd.DataFrame({'Depth (m)': depth, 'Temperature (°C)': values})
		fig = px.line(
			df,
			x='Temperature (°C)',
			y='Depth (m)',
			title='Sample Temperature Profile',
			color_discrete_sequence=['#89B4FA']
		)
	else:  # Salinity
		values = 34.5 + np.tanh((depth - 1000) / 500) * 0.5 + np.random.randn(100) * 0.05
		df = pd.DataFrame({'Depth (m)': depth, 'Salinity (PSU)': values})
		fig = px.line(
			df,
			x='Salinity (PSU)',
			y='Depth (m)',
			title='Sample Salinity Profile',
			color_discrete_sequence=['#77dd77']
		)

	fig.update_layout(yaxis_autorange="reversed", template="plotly_dark")
	return fig

# --- Chat App ---
st.title("💬 FloatChat Interface")

# Initialize chat history
if "messages" not in st.session_state:
	st.session_state.messages = [{
		"role": "assistant",
		"content": "Hello! Ask me about ARGO data. Try 'show me temperature' or 'what is the salinity?'"
	}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])
		if "chart" in message:
			st.plotly_chart(message["chart"], use_container_width=True)

# React to user input
if prompt := st.chat_input("Ask about ocean data..."):
	# Display user message in chat message container
	st.chat_message("user").markdown(prompt)
	# Add user message to chat history
	st.session_state.messages.append({"role": "user", "content": prompt})

	# Assistant response logic
	with st.chat_message("assistant"):
		with st.spinner("Thinking..."):
			time.sleep(1.5)  # Simulate thinking

			response_text = "Sorry, I can only provide sample data for 'temperature' and 'salinity' in this demo."
			response_chart = None

			prompt_lower = prompt.lower()
			if "temperature" in prompt_lower:
				response_text = "Certainly! Here is a sample temperature profile you requested."
				response_chart = generate_placeholder_chart('temperature')
			elif "salinity" in prompt_lower:
				response_text = "Of course! Here is a sample salinity profile."
				response_chart = generate_placeholder_chart('salinity')

		st.markdown(response_text)
		if response_chart:
			st.plotly_chart(response_chart, use_container_width=True)

	# Add assistant response to chat history
	assistant_message = {"role": "assistant", "content": response_text}
	if response_chart:
		assistant_message["chart"] = response_chart
	st.session_state.messages.append(assistant_message)
