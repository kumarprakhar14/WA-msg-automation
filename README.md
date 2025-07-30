# 📲 WhatsApp Personalized Message Sender with Python

This project allows you to send **personalized WhatsApp messages** to a list of contacts stored in an Excel file — all in **one click** using **Python** and **WhatsApp Web automation**. Ideal for small business owners, event managers, or anyone looking to message many people without copy-pasting.

---

## 📁 Project Setup Instructions

### 🔃 Clone the Repository

```bash
git clone https://github.com/your-username/whatsapp-bulk-sender.git
cd whatsapp-bulk-sender
```

### 📦 Install Required Dependencies

Ensure you're using **Python 3.6+**. Then, install all the required Python packages:

Install the necessary packages, run the command :

```bash
pip install pandas openpyxl pywhatkit
```

---

## 📝 Excel File Format (`contacts.xlsx`)

The script uses an Excel file with the following **three columns**:

| Name  | Phone Number | Message Template                       |
| ----- | ------------ | -------------------------------------- |
| Rahul | 919812345678 | Hello {name}, your order is confirmed! |
| Priya | 917012345678 | Hi {name}, welcome to our newsletter!  |

> ✅ Make sure:
>
> * **Phone Number** includes country code (e.g., `91` for India).
> * `{name}` is a placeholder and will be replaced dynamically.

---

## 🚀 Running the Script

### Step-by-Step

1. Make sure your **contacts.xlsx** file is in the project folder.
2. Ensure you’re **logged into WhatsApp Web** in your browser.
3. Run the script:

```bash
python whatsapp_sender.py
```

The script will:

* Open WhatsApp Web
* Schedule and send each message one-by-one with a 15s delay
* Automatically personalize each message using `{name}`

---

## 🔧 Customization Guide

| 🔄 Feature             | How to Change                   | Notes                                   |
| ---------------------- | ------------------------------- | --------------------------------------- |
| Message Timing         | Modify `time_min + 1`           | Can be scheduled for future times       |
| Delay Between Messages | Change `time.sleep(15)`         | Useful for slow networks or large lists |
| Placeholder Support    | Use more like `{name}` in Excel | Add `{order_id}`, `{amount}`, etc.      |
| Tab Behavior           | Set `tab_close=True/False`      | Keep tab open if you want to monitor    |

---

## ⚠️ Important Notes

* Keep your internet stable and **don’t close the browser** during execution.
* Sending too many messages rapidly can **trigger WhatsApp spam filters**.
* This script is for **educational/personal use** only.

---

## 💼 Business/Enterprise Option

If you're looking to scale up or send files/media reliably:

👉 Use **[WhatsApp Business Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api)**

Benefits:

* High reliability
* Message templates, files, delivery tracking
* Scalable for thousands of users

---

## 📄 License

This project is licensed under the MIT License — you're free to use, modify, and distribute it.

---

## 👨‍💻 Author
**Kumar Prakhar**

Feel free to fork and improve. Suggestions are welcome!
Connect with me on [LinkedIn](www.linkedin.com/in/kumar-prakhar14) or GitHub.
