from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
Claudio Fayad 
Vice President of Technology, Process Systems & Solutions, 
Emerson Automation Solutions 
Claudio Fayad is currently vice president of technology of Emersons process 
systems and solutions business. In this role since August 2016, Claudio is responsible 
for product strategy and development of mission-critical platforms. He actively works 
with customers and stakeholders across the organization to develop innovative digital 
initiatives and extend DeltaV into a broader digital ecosystem.  
Claudio has 27 years in the Automations Solutions business include previous roles 
in engineering, sales, project execution, project management, business management, 
product marketing and technology, participating in many projects around the world. 
Claudio has a passion for bringing people together to drive results through 
change, engagement and diversity.  
Originally from Brazil, Claudio attained his electrical engineering degree from 
UNICAMP (Campinas University) University with a major in process control. He earned 
his executive MBA degree from Fundação Dom Cabral and is also a graduate of the 
post-MBA executive program from Kellogg. 
"""

if __name__ == '__main__':
    print('Hello Langchain!')

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)