# 🌐 Google Search Scraper (Playwright + BeautifulSoup)
A **reusable Python template** for scraping structured content from websites using Playwright and BeautifulSoup. It extracts **clean, structured data** (sections and text) from public websites and saves the result into a JSON file.

---

## 📌 Features
- 🚀 Headless browser automation via Playwright  
- 🧾 HTML parsing using BeautifulSoup  
- 🎯 Smart filtering for meaningful content (headings, paragraphs, etc.)  
- 📂 Structured JSON output — section-wise content  
- 🔄 Easily customizable for different target websites  

---

## 🖼 Example Use Case
This scraper was used to extract structured content from **https://medium.com/**.  

Sample output in `structured_output.json` includes:
- Company Overview  
- AI-Powered Services  
- Job Roles (Niva)  
- FAQs and Integrations  
- Contact and Careers  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/NA7RAWY/Google_Search_Scraper.git
cd Google_Search_Scraper

### 2️⃣ Install dependencies
pip install -r requirements.txt
playwright install

> `playwright install` is required once to download browser binaries.

---

## 🚀 How to Use

### 1. Set your target URL
Edit the `url` variable in **scraper.py**:
url = "https://medium.com"  # Change this to your target page

### 2. Run the scraper
python scraper.py

### 3. View the results
- **structured_output.json** will contain extracted content in JSON format  
- Terminal will display clean, organized sections  

---

## 📁 Project Structure
.
├── scraper.py                # Main scraping logic
├── requirements.txt          # Required Python packages
├── structured_output.json    # Output file (auto-generated)
└── README.md                 # Project documentation

---

## 🛠 Tech Stack
- 🐍 Python 3.9+  
- 🌐 Playwright  
- 🥣 BeautifulSoup  
- 📄 lxml  

---

## 🔮 Roadmap
- [ ] Add CLI arguments (e.g., `--url`)  
- [ ] Handle pagination / infinite scroll  
- [ ] Export output to Markdown or HTML  
- [ ] Optional: Support login-protected pages  

---

## 👤 Author
**Mahmoud Elnahrawy**  
📧 mahmoudelnahrawywork@gmail.com  
📍 Cairo, Egypt  

---

## 🪪 License
Released under the MIT License — free to use and modify.
