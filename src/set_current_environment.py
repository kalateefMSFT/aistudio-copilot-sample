import os
from azure.ai.generative import AIClient
from azure.identity import DefaultAzureCredential

def set_environment_variables():
    os.environ['AZURE_AI_SEARCH_ENDPOINT'] = os.environ['AZURE_COGNITIVE_SEARCH_TARGET']
    os.environ['AZURE_AI_SEARCH_KEY'] = os.environ['AZURE_COGNITIVE_SEARCH_KEY']
    os.environ['AZURE_AI_SEARCH_INDEX_NAME'] = 'product-info'
    os.environ['AZURE_OPENAI_CHAT_MODEL'] = 'gpt-35-turbo'
    os.environ['AZURE_OPENAI_CHAT_DEPLOYMENT'] = 'gpt-35-turbo-0301'
    os.environ['AZURE_OPENAI_EVALUATION_MODEL'] = 'gpt-35-turbo'
    os.environ['AZURE_OPENAI_EVALUATION_DEPLOYMENT'] = 'gpt-35-turbo-0301'
    os.environ['AZURE_OPENAI_EMBEDDING_MODEL'] = 'text-embedding-ada-002'
    os.environ['AZURE_OPENAI_EMBEDDING_DEPLOYMENT'] = 'text-embedding-ada-002-2'


def set_all():
    client = AIClient.from_config(DefaultAzureCredential())
    client.get_default_aoai_connection().set_current_environment()
    client.connections.get("Default_CognitiveSearch").set_current_environment()
    
    set_environment_variables()