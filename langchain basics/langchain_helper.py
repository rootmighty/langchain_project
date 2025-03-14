from langchain.chains.summarize.map_reduce_prompt import prompt_template

from access import apiKey
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

os.environ["OPENAI_API_KEY"] = apiKey()
llm = OpenAI(temperature=0.7)




def generate_restaurant_name_and_items(cuisine):

    #Chain 1 Restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template= "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2 Food Recipes
    prompt_template_recipe = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some Menu Items for {restaurant_name} food. Return it only as csv comma separated value list."
    )
    food_chain = LLMChain(llm=llm, prompt=prompt_template_recipe, output_key="food_items")

    #Construct the Sequential Chain
    chain = SequentialChain(
        chains=[name_chain, food_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "food_items"]
    )

    #Running the chain
    response = chain({"cuisine":cuisine})
    return {
        "restaurant_name": response["restaurant_name"],
        "food_items": response["food_items"]
    }

if __name__ == "__main__":
    print(generate_restaurant_name_and_items(cuisine="Arabic"))
