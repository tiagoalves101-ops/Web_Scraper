# 📚 Web Scraping with GUI

This project is a **Python desktop application** that performs **web scraping** of products/books, stores the data in a **SQLite database**, and allows exporting the results to **CSV** or **Excel**, through a simple graphical interface built with **Tkinter**.

---

## 🚀 Features
- Enter any **URL** directly in the app.
- Extract **title, price, and availability** of products/books.
- Automatically store the data in a **SQLite** database.
- Export the data to **CSV or Excel** with one click.
- Simple and friendly GUI with Tkinter.

---

## 🛠️ Technologies
- **Python 3**
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [SQLite3](https://docs.python.org/3/library/sqlite3.html)
- [Pandas](https://pandas.pydata.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

---

## 📂 Project Structure
.
├── dados_web.db # SQLite database (auto-generated)
├── main.py # Main application code
├── README.md # Documentation
├── .gitignore # Ignored files
└── LICENSE # License (MIT)

yaml
Copiar código

---

📂 [Download Project File](https://github.com/tiagoalves101-ops/Web_Scraper/blob/main/creditcards.csv)

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/web-scraper-gui.git
   cd web-scraper-gui
Install dependencies:

bash
Copiar código
pip install requests beautifulsoup4 pandas openpyxl
Run the program:

bash
Copiar código
python main.py

⚠️ Disclaimer
This project is for educational purposes only.
Use it only on websites that allow scraping (e.g., Books to Scrape).
The author is not responsible for misuse on sites that prohibit automated data collection.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
