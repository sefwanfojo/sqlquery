import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType, initialize_agent, load_tools
import os

load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
st.title("SQL query generator")
sql_query= st.text_input("generate SQL query...")
button = st.button("search")

PREFIX = PREFIX = "Here to help with SQL queries! I can only answer questions related to building SQL queries. If your question isn't about SQL, please rephrase it as a query. I'll provide the answer directly, without extra explanations. Note: I currently cannot access external tools."

llm = ChatGoogleGenerativeAI(model="gemini-pro")
tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, agent_kwargs={'prefix':PREFIX})
if button:
    response=agent.invoke(sql_query)
    st.text(response['output'])