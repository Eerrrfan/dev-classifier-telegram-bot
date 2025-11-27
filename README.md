

```markdown
# Dev or Not? 👨‍💻🤖
A simple machine learning project that predicts whether a person *is a programmer or not* based on their text.  
Includes a training script, CLI prediction tool, and a Telegram bot.

---

## 📌 Features
- Text classification using TF-IDF  
- Trains multiple ML models and saves the best one  
- CLI tool for quick predictions  
- Telegram bot connected to the trained model  
- Easy-to-understand project structure

---

## 🗂 Project Structure
```

programmer_dataset_15k.csv   # Dataset
train.py                     # Train the model
predict.py                   # CLI prediction tool
bot.py                       # Telegram bot
README.md

```

---

## ⚙️ Installation
```

pip install pandas scikit-learn joblib python-telegram-bot

```

---

## 🧠 Train the Model
```

python train.py

```
The best model will be saved as:
```

programmer_model.joblib

```

---

## 🧪 CLI Prediction
```

python predict.py

```
Type any text → get prediction  
Type `EXIT` → quit

---

## 🤖 Telegram Bot
1. Create a bot using **@BotFather**
2. Set your token:
   - Linux/Mac:  
     `export TELEGRAM_BOT_TOKEN="YOUR_TOKEN"`
   - Windows (PowerShell):  
     `setx TELEGRAM_BOT_TOKEN "YOUR_TOKEN"`
3. Run the bot:
```

python bot.py

```

---

## 📜 License
MIT License
```
