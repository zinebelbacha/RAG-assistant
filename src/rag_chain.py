from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables import RunnableMap
from .vectorstore import init_vectorstore
from .llm_wrapper import get_llm

def build_rag_chain():
    vectorstore = init_vectorstore()
    llm = get_llm()

    template = """
    You are an assistant specializing in the Institut National des Postes et Télécommunications (INPT).
    Your role is to provide information and answer questions related only to INPT, including its programs, research, and organizational details.
    If a question is outside your area of expertise, politely inform the user that you can only assist with questions related to INPT.

    Context: {context}
    Question: {question}
    Answer:
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )

    rag_chain = (
        RunnableMap({
            "context": vectorstore.as_retriever(), 
            "question": RunnablePassthrough()
        })
        | prompt
        | llm  
        | StrOutputParser()
    )
    return rag_chain

def ask_question(question):
    chain = build_rag_chain()
    return chain.invoke(question)
