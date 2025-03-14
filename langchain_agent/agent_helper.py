#to initialize and use agents
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chains.llm import LLMChain
from langchain.llms import OpenAI
from access import apiKey, serpapikey
import os
#To keep conversation on memory
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
#To have only a part of the oldest conversation as history
from langchain.memory import ConversationBufferWindowMemory

os.environ["OPENAI_API_KEY"] = apiKey()

llm = OpenAI(temperature=0.7)
#Using Wikipedia
"""tools = load_tools(["wikipedia","llm-math"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, #Thought then answer
    verbose=True
)
response = agent.run("When was Elon Musk born ? What is his age right now in 2025 ?")
print(response)"""

"""#Using SerpAPI
os.environ["SERPAPI_API_KEY"] = serpapikey()
tools = load_tools(["serpapi","llm-math"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, #Thought then answer
    verbose=True
)
response2 = agent.run("What was the GDP of US in 2022? add 5 to that GDP. What is the answer?")
print(response2)"""

"""prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template= "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
    )

memory = ConversationBufferMemory()

chain = LLMChain(llm=llm, prompt=prompt_template_name, memory=memory)
name = chain.run("Italian")
print(name)
name = chain.run("EWE TraditionalTogolese")
print(name)
print(chain.memory.buffer)"""

memory = ConversationBufferWindowMemory(k=2)
convo = ConversationChain(llm=llm)
print(convo.prompt.template)
print(convo.run("What is the capital of France ?"))
print(convo.run("What is the one of Togo ?"))
print(convo.run("What is 8 + 3 ?"))
print(convo.run("What is the one of Togo ?"))
print(convo.run("What is 8 + 3 ?"))
print(convo.run("What is 8 + 5 ?"))
print(convo.run("What about Italy talking about that previous question ?"))
print(convo.memory.buffer)