import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
load_dotenv()
os.environ['OPENAI_API_KEY'] = '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'

## langsmith tracking
os.environ['LANGCHAIN_API_KEY']= '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'
os.environ['LANGCHAIN_TRACING_V2']='True'
os.environ['LANGCHAIN_PROJECT']='GenAIAPPWithOPENAI'

promt = ChatPromptTemplate.from_messages(
[
    ('system','You are a helpful assistant. please respond to the question asked'),
    ('user',"Question:{question}")
]

)
## streamlit framework
st.title("Lanchain Demo with Gemma Model")
input_text = st.text_input("What question you have in mind?")

## Ollma Llama2
llm= ChatOpenAI(model='gpt-4o')
output_parser = StrOutputParser()
chain = promt|llm|output_parser
import streamlit as st
from requests.exceptions import ConnectionError

if chain.invoke({'question': input_text}):
    response = chain.invoke({'question': input_text})
    st.write(response)



