from src.rag_chain import ask_question

if __name__ == "__main__":
    question = "What are the clubs that students can join at INPT Rabat? Give me two clubs with a brief explanation of each one's activities."
    answer = ask_question(question)
    print(answer)
