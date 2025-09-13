from src.rag_chain import ask_question

if __name__ == "__main__":
    while True:
        q = input("Ask me something (or type 'exit'): ")
        if q.lower() == "exit":
            break
        print("Answer:", ask_question(q))