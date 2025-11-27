<h1 align="center">Dev or Not? 👨‍💻🤖</h1>

<p align="center">
A lightweight and fun machine learning project that predicts whether someone <b>is a programmer</b> — based only on their text.
<br>
Includes model training, a CLI predictor, and a Telegram bot.
</p>

---

## ✨ What This Project Does
- Learns from a text dataset (`dev` vs `nondev`)
- Trains multiple ML models and picks the best one automatically
- Saves the final model for later usage
- Offers:
  - ⚡ A simple **CLI prediction tool**
  - 🤖 A fully working **Telegram bot**

---

## 📁 Project Layout


programmer_dataset_15k.csv → dataset
train.py → train the ML model
predict.py → quick CLI predictor
bot.py → Telegram bot



---

## ⚙️ Installation
```bash
pip install pandas scikit-learn joblib python-telegram-bot




🧠 Train the Model

python train.py


The trained model will be saved as:
programmer_model.joblib


