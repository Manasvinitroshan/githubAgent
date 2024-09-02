import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchains.agents import create_tool_calling_agent
from langchains.agents import AgentExector
from langchains.tools.retriever import hub
from github import fetch_github_issues

load_dotenv()

def connect_to_vstore():
    embeddings = OpenAIEmbeddings()
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    desired_namespace = os.getenv("ASTRA_DB_KEYSPACE")

    if desired_namespace:
        ASTRA_DB_KEYSPACE = desired_namespace

    else:
        ASTRA_DB_KEYSPACE = None
    
    vstore = AstraDBVectorStore(

        embeddings=embeddings,
        collection_name = "github",
        api_endpoint = ASTRA_DB_API_ENDPOINT,
        token = ASTRA_DB_APPLICATION_TOKEN,
        namespace = ASTRA_DB_KEYSPACE,

    )
    return vstore

vstore = connect_to_vstore()
add_to_vectorstore = input("Do you want to update the issues (y/N): ").lower() in ["yes", "y"]

if add_to_vectorstore:
    owner = "Manasvinitroshan"
    repo = "tta-web"
    fetch_github_issues(owner,repo)





