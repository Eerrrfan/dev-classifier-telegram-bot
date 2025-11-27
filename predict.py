import joblib

def main():
    model = joblib.load("programmer_model.joblib")  
    print(" Model loaded successfully.")
    print("Type 'EXIT' to quit.\n")

    while True:
        text = input("Enter a message: ")

        if text.lower() == "exit":
            print("Exiting....")
            break

        pred = model.predict([text])[0]

        if pred == "dev":
            print("💻 This person is likely a PROGRAMMER.\n")
        else:
            print("🙂 This person is likely NOT a programmer.\n")

if __name__ == "__main__":
    main()
