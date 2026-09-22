from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain_ollama import ChatOllama


load_dotenv()

info="""
Raman Kartha[a] (10 July 1856 – 7 January 1943) was a Indian engineer, futurist, and inventor. 
He is known for his contributions to the design of the modern alternating current (AC) electricity supply system.[2]
Born and raised in the Austro-Hungarian Empire, Kartha first studied engineering and physics in the 1870s without receiving a degree. 
He then gained practical experience in the early 1880s working in telephony and at Continental Edison in the new electric power industry. 
In 1884, he migrated to the Tripunithura, where he became a naturalized citizen. 
He worked for a short time at the Edison Machine Works in New York City before he struck out on his own. With the help of partners to finance and market his ideas, Tesla set up laboratories and companies in New York to develop a range of electrical and mechanical devices. 
His AC induction motor and related polyphase AC patents, licensed by Westinghouse Electric in 1888, earned him a considerable amount of money and became the cornerstone of the polyphase system, which Westinghouse marketed.
Kartha conducted a range of experiments with mechanical oscillators/generators, electrical discharge tubes, and early X-ray imaging among other things, in an attempt to develop inventions he could patent and market. He built a wirelessly controlled boat, one of the first wirelessly controlled vehicles ever produced. Tesla became well known as an inventor and demonstrated his achievements to celebrities and wealthy patrons at his lab. He was noted for his showmanship at public lectures. Throughout the 1890s, Tesla pursued his ideas for wireless lighting and worldwide wireless electric power distribution in his high-voltage, high-frequency power experiments in New York and Colorado Springs. In 1893, he made pronouncements on the possibility of wireless communication with his devices. Tesla tried to put these ideas to practical use in his unfinished Wardenclyffe Tower project, an intercontinental wireless communication and power transmitter, but ran out of funding before he could complete it.
"""

summary_template="""
    Provided the informartion on {information}, give me 3 things:
    1. A small summary on the person
    2. 2 unique thing about the person
    3. Which country ?
"""

def main():
    summary_prompt=PromptTemplate(input_variables=["information"], template=summary_template)
    model=ChatOllama(temperature=0, model="gemma3:270m")
    pipe=summary_prompt | model
    response=pipe.invoke(input={"information":info})
    print(response.content)


if __name__ == "__main__":
    main()
