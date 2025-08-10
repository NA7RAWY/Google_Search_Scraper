# 🌐 Google Search Scraper (Playwright + BeautifulSoup)

This project is a reusable Python template for scraping structured content from websites using [Playwright](https://playwright.dev/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). It extracts clean, structured data (sections and text) from public websites and saves the result into a JSON file.

---

## 📦 Features

- Headless browser scraping via **Playwright**
- HTML parsing via **BeautifulSoup**
- Smart filtering for meaningful content (headings, paragraphs, etc.)
- Structured section-wise JSON output
- Easy to modify and reuse on different sites

---

## 🖼 Example Use Case

This scraper was used to extract structured content from **[https://medium.com]**. The output (see `structured_output.json`) includes sections such as:

- Company Overview
- AI-Powered Services
- Job Roles (Niva)
- FAQs and Integrations
- Contact and Careers

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/google-search-scraper.git
cd google-search-scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

> Note: `playwright install` is required once to download browser binaries.

---

## 🚀 How to Use

### 1. Change the target URL

Edit the `url` in `scraper.py`:

```python
url = "https://medium.com"  # or any other page you want
```

### 2. Run the scraper

```bash
python scraper.py
```

### 3. Output

- A structured JSON will be saved as `structured_output.json`
- Terminal will display organized sections with clean text

---

## 📁 File Structure

```
.
├── scraper.py                # Main scraping logic
├── requirements.txt          # Required Python packages
├── structured_output.json    # Output (auto-generated)
└── README.md                 # This file
```

---

## 🧠 Technologies Used

- [Python 3.9+](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [lxml](https://lxml.de/)

---

## 🛡 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to reuse and modify.

---

## 🧪 TODO / Improvements

- Add command-line arguments (e.g., `--url`)
- Handle pagination or infinite scroll
- Export to Markdown or HTML
- Optional: Support for login-protected pages

---

## 👤 Author
**Mahmoud Elnahrawy**  
Contact: info@nanovate.io  
Cairo, Egypt
