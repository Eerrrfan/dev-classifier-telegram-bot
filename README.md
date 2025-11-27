



# Dev or Not? 👨‍💻✨  
A lightweight machine learning project that predicts whether someone *is a programmer* based solely on their text.  
Includes a training pipeline, a CLI prediction tool, and a Telegram bot for real-time interaction. 🤖📩

---

## 📌 Overview
This project uses a labeled dataset of developer and non-developer sentences to train a text classifier.  
Once trained, the model can classify any message as:

- 🟢 **dev** — programmer  
- 🔵 **nondev** — not a programmer

Simple, practical, and perfect for learning ML text classification.

---

## ✨ Features
- 🔡 TF-IDF text processing  
- 🧠 Multiple ML models tested automatically  
- 💾 Best model saved using `joblib`  
- ⚡ Fast CLI prediction tool  
- 🤖 Telegram bot for interactive predictions  
- 🧱 Clean and beginner-friendly project structure  

---

## 📁 Project Structure
```

programmer_dataset_15k.csv   → dataset
train.py                     → training script
predict.py                   → CLI prediction tool
bot.py                       → Telegram bot
README.md                    → documentation

```

---

## ⚙️ Installation
Install requirements:

```

pip install pandas scikit-learn joblib python-telegram-bot

```

---

## 🧠 Train the Model
Run:

```

python train.py

```

The best model will be saved as:

```

programmer_model.joblib

```

---

## 🧪 CLI Predictor
```

python predict.py

```
Type a sentence → get a prediction.  
Type `EXIT` → exit the tool.

---

## 🤖 Telegram Bot Setup
1. Create a bot via **@BotFather**  
2. Set your bot token as an environment variable:

**Linux/macOS**
```

export TELEGRAM_BOT_TOKEN="YOUR_TOKEN"

```

**Windows**
```

setx TELEGRAM_BOT_TOKEN "YOUR_TOKEN"

```

3. Run the bot:
```

python bot.py

```

Send any message → the bot predicts whether the person is a programmer. 🚀

