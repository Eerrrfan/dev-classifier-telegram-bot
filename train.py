import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline
import joblib

def main():
    
    df = pd.read_csv("programmer_dataset_15K.csv")

    assert "label" in df.columns and "text" in df.columns, "CSV file must contain 'label' and 'text' columns."

    X = df["text"]
    y = df["label"]
   
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Linear SVM": LinearSVC(),
        "Naive Bayes": MultinomialNB(),
    }

    best_model_name = None
    best_model = None
    best_accuracy = 0.0

    for name, clf in models.items():
        print(f"🔷 Training model: {name}\n")

        model = make_pipeline(
            TfidfVectorizer(),
            clf
        )

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        print(f" Accuracy for {name}: {acc:.4f}")
        print(" Classification report:")
        print(classification_report(y_test, y_pred))

        if best_model is None or acc > best_accuracy:
            best_accuracy = acc
            best_model_name = name
            best_model = model

    if best_model is None:
        raise RuntimeError("❌ No model was trained successfully. Check your dataset.")

    print(f"🏆 Best model: {best_model_name} with accuracy {best_accuracy:.4f}")

    joblib.dump(best_model, "programmer_model.joblib")
    print("\n Best model saved to 'programmer_model.joblib'.")

    test_samples = [
        "I use Python and Java for backend development.",
        "I love watching movies with my friends.",
        "I'm debugging a bug in my React project.",
        "I'm going to the gym later."
    ]
    preds = best_model.predict(test_samples)
    print("\n🔍 Test predictions on some sample texts:")
    for text, label in zip(test_samples, preds):
        print(f"Text: {text}  -->  Predicted: {label}")

if __name__ == "__main__":
    main()
