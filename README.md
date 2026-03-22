# 🤖 ZestBot — Zesta AI Chatbot

### An intelligent FAQ chatbot for Amity University, Noida

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=6C63FF&center=true&vCenter=true&width=500&lines=Ask+me+anything+about+Amity+University!;80%2B+FAQs+at+your+fingertips;Admin+Panel+for+easy+management;Built+with+Flask+%26+SQLite" alt="Typing SVG" />

---

[Features](#-features) •
[Tech Stack](#-tech-stack) •
[Installation](#-installation) •
[Usage](#-usage) •
[API Reference](#-api-reference) •
[Contributing](#-contributing)

</div>

---

## 📖 About The Project

**ZestBot (Zesta AI)** is a web-based FAQ chatbot application designed specifically for **Amity University, Noida**. It helps students, parents, and visitors get instant answers to common university-related questions — from admissions and placements to hostel life and faculty information.

The project also includes a fully functional **Admin Panel** that allows administrators to add, edit, and delete FAQ entries in real-time without touching the code.

### 🎯 Why ZestBot?

- 🕐 Students often struggle to find quick answers about university services
- 📞 Phone lines and help desks have limited hours
- 🔁 Most queries are repetitive and can be automated
- ⚡ ZestBot provides instant 24/7 responses to 80+ common questions

---

## ✨ Features

### 💬 Chat Interface
- Clean, modern chat UI for student interaction
- Real-time question-answer system
- Keyword-based intelligent matching algorithm
- Department-specific faculty query detection
- Fallback response for unrecognized questions

### 🔐 Admin Panel
- Secure login system with session management
- **Add** new FAQ entries
- **Edit** existing questions and answers
- **Delete** outdated FAQs
- View all FAQs in an organized dashboard
- Flash message notifications for all actions

### 📚 Comprehensive FAQ Database
- **80+ pre-loaded FAQs** covering:
  - 🎓 Admissions & Eligibility
  - 📖 Academics & Curriculum
  - 💼 Placements & Internships
  - 💰 Fees & Scholarships
  - 🏠 Hostel & Accommodation
  - 🎉 Campus Life & Clubs
  - 👨‍🏫 Faculty & Departments
  - 🌍 International Programs
  - 📋 General & Miscellaneous

### 👨‍🏫 Faculty Directory
- Department-wise faculty listings for **8 departments**:
  - Administration
  - Engineering & Technology
  - Law
  - Applied Sciences
  - Social Sciences
  - Medical & Life Sciences
  - Business & Management
  - Other Departments

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technology |
|:--------:|:----------:|
| **Language** | ![Python](https://img.shields.io/badge/Python_3-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Framework** | ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite3-003B57?style=flat-square&logo=sqlite&logoColor=white) |
| **Templating** | ![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |
| **Auth** | ![Session](https://img.shields.io/badge/Flask_Sessions-Cookie_Based-orange?style=flat-square) |

</div>

### 📦 Dependencies
Flask>=2.0.0

text


> **Note:** `os`, `sqlite3`, and `datetime` are part of the Python standard library — no additional installation required.

---

## 🏗️ Architecture
┌─────────────────────────────────────────────────────────┐
│ ZestBot Architecture │
├─────────────────────────────────────────────────────────┤
│ │
│ ┌────────────┐ HTTP/JSON ┌────────────────────┐ │
│ │ Frontend │ ◄────────────► │ Flask Server │ │
│ │ (HTML/ │ │ (app.py) │ │
│ │ Jinja2) │ │ │ │
│ └────────────┘ │ ┌──────────────┐ │ │
│ │ │ Keyword │ │ │
│ ┌────────────┐ │ │ Matcher │ │ │
│ │ Admin │ ◄── Session ──►│ │ Engine │ │ │
│ │ Panel │ Auth │ └──────────────┘ │ │
│ └────────────┘ └────────┬───────────┘ │
│ │ │
│ ┌────────▼───────────┐ │
│ ┌────────────────┐ │ SQLite3 │ │
│ │ faq_data.py │──seed───► │ (zesta.db) │ │
│ │ (80+ FAQs) │ │ │ │
│ └────────────────┘ └────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────┘

text


### 🔄 How the Matching Algorithm Works
User Input ──► Lowercase & Split into Words
│
▼
Compare with each FAQ
in the database
│
▼
Count matching words
(word overlap score)
│
▼
┌──────────────┴──────────────┐
│ │
Score > 0 Score = 0
│ │
▼ ▼
Return best match Return fallback message
(highest score) "I don't have information..."

text


Additionally, a **department-specific handler** checks for faculty-related keywords combined with department identifiers for targeted responses.

---

## 📁 Project Structure
zestBot/
│
├── 📄 app.py # Main Flask application
├── 📄 faq_data.py # FAQ data & faculty directory
├── 📄 requirements.txt # Python dependencies
├── 📄 README.md # Project documentation
│
├── 📂 templates/ # Jinja2 HTML templates
│ ├── 📄 chat.html # Main chatbot interface
│ ├── 📄 admin_login.html # Admin login page
│ ├── 📄 admin_panel.html # Admin dashboard
│ └── 📄 edit_faq.html # FAQ edit form
│
├── 📂 static/ # Static assets (CSS, JS, images)
│ ├── 📂 css/
│ ├── 📂 js/
│ └── 📂 images/
│
└── 📄 zesta.db # SQLite database (auto-generated)

text


---

## ⚡ Installation

### Prerequisites

- **Python 3.8+** installed on your system
- **pip** (Python package manager)
- **Git** (to clone the repository)

### Step-by-Step Setup

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Overallscam/zestBot.git
cd zestBot
2️⃣ Create a Virtual Environment (Recommended)
Bash

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
Bash

pip install -r requirements.txt
Or install Flask manually:

Bash

pip install Flask
4️⃣ Set Environment Variables (Optional)
Bash

# On Windows (PowerShell)
$env:SECRET_KEY = "your-super-secret-key-here"
$env:FLASK_ENV = "development"

# On macOS/Linux
export SECRET_KEY="your-super-secret-key-here"
export FLASK_ENV="development"
5️⃣ Run the Application
Bash

python app.py
6️⃣ Open in Browser
text

🤖 Chatbot:    http://localhost:5000
🔐 Admin:      http://localhost:5000/admin
🚀 Usage
💬 Using the Chatbot
Navigate to http://localhost:5000
Type your question in the chat input box
Press Enter or click Send
ZestBot will find the most relevant answer from its database
Example queries:

text

"What is the fee structure for B.Tech?"
"How can I apply to Amity University?"
"Who are the engineering faculty?"
"Are hostels available?"
"What is the placement rate?"
🔐 Using the Admin Panel
Navigate to http://localhost:5000/admin
Login with default credentials:
text

Username: admin
Password: zesta123
From the dashboard, you can:
➕ Add new FAQ entries
✏️ Edit existing FAQs
🗑️ Delete outdated FAQs
📋 View all FAQ entries
📡 API Reference
Public Endpoints
GET /
Returns the main chatbot interface.

POST /ask
Processes a user question and returns the best matching answer.

Request:

JSON

{
  "message": "What is the fee for B.Tech?"
}
Response:

JSON

{
  "answer": "Around ₹2–3 LPA (varies by specialization)."
}
Admin Endpoints
Method	Endpoint	Description	Auth Required
GET	/admin	Admin login page	❌
POST	/admin/login	Authenticate admin	❌
GET	/admin/panel	View all FAQs	✅
GET	/admin/logout	Logout admin	✅
GET	/admin/status	Check login status	❌
POST	/admin/add	Add new FAQ	✅
GET	/admin/edit/<id>	Edit FAQ form	✅
POST	/admin/update/<id>	Save FAQ changes	✅
GET	/admin/delete/<id>	Delete a FAQ	✅
🗃️ Database Schema
faqs Table
Column	Type	Constraints	Description
id	INTEGER	PRIMARY KEY, AUTOINCREMENT	Unique identifier
question	TEXT	NOT NULL	The FAQ question
answer	TEXT	NOT NULL	The FAQ answer
Auto-Seeding
On first run, the database is automatically populated with 80+ FAQs from faq_data.py. This includes questions about:

Category	Count
General Bot Info	5
Faculty Information	7+
Admissions	10
Academics	10
Placements	10
Fees & Scholarships	10
Campus Life & Clubs	10
Hostel & Accommodation	10
Faculty & Departments	10
International Programs	10
General & Miscellaneous	20
👨‍🏫 Faculty Directory
ZestBot includes a comprehensive faculty directory organized by department:

<details> <summary><b>🏛️ Administration (3 members)</b></summary>
Dr. Balvinder Shukla – Vice Chancellor
Prof. Kaiser Singh – Director, Student Affairs & Sports
Dr. Sujata Khandai – Director, ACCF
</details><details> <summary><b>⚙️ Engineering & Technology (4 members)</b></summary>
Prof. (Dr.) K. M. Soni – Deputy Dean, ASET
Dr. Om Prakash Sinha – Director, AIT
Dr. Shalini Singh Sharma – Director, ASE
Dr. Bedatri Moulik – Assistant Professor, AIT
</details><details> <summary><b>⚖️ Law (2 members)</b></summary>
Prof. (Dr.) Tahir Mahmood – Honorary Chairman, AIALS
Atul Jain – Assistant Professor, Criminal Law
</details><details> <summary><b>🔬 Applied Sciences (3 members)</b></summary>
Sunita Negi – Assistant Professor, Physics
Prof. Ramesh Namdeo Pudake – Nanotechnology
Dr. Ajit Varma – Distinguished Scientist
</details><details> <summary><b>📊 Social Sciences (4 members)</b></summary>
Dr. Madhumita Saha – Associate Professor
Dr. Shachee Agnihotri – Assistant Professor (II)
Dr. Sucharita Sen – Assistant Professor (I)
Dr. Smita – Assistant Professor (I)
</details><details> <summary><b>🏥 Medical & Life Sciences (7 members)</b></summary>
Dr. Mallika Chatterjee – Neuropsychology & Neurosciences
Dr. Rishikesh Kumar Gupta – AINN
Dr. Sujeet Kumar Singh – Forestry & Wildlife
Dr. Kajal Kanchan – Molecular Medicine
Dr. Veerendra Kumar – AIMMSCR
Dr. Adhiraj Roy – AIMMSCR
Dr. Manoj Kumar – Genome Engineering
</details><details> <summary><b>💼 Business & Management (11 members)</b></summary>
Dr. Chanderdeep Tandon – Director, AIB
Dr. Nidhee Chaudhary – Professor, AIB
Dr. Rachana Singh – Professor, AIB
Pratima Chaudhuri – Professor, AIB
Dr. Sabari Ghosal – Professor, AIB
Dr. Shoma Paul Nandi – Professor, AIB
Dr. Ajit Mittal – Professor, AIBS
Dr. Mamta Mohan – Professor, AIBS
Dr. Shikha Kapoor – Professor, AIBS
V. P. Kakkar – Professor, AIBS
C. Ranjan Bhandari – Professor, AICISM
</details><details> <summary><b>📚 Other Departments (6 members)</b></summary>
Dr. Raman Malik – English Studies & Research
Dr. Bidisha Banerji – Public Policy
Dr. Eshan Parikh – Film & Drama
Dr. Ranjana Bhatia – Psychology & Allied Sciences
Dr. Santosh Pal Singh – Nutrition, Sports & Disability Studies
Dr. Gurinder Singh – International Business
</details>
⚙️ Configuration
Environment Variables
Variable	Default	Description
SECRET_KEY	zesta-super-secret-key-12345	Flask session encryption key
PORT	5000	Server port
FLASK_ENV	development	Set to production for deployment
Default Admin Credentials
text

Username: admin
Password: zesta123
⚠️ Important: Change these before deploying to production!

🌐 Deployment
ZestBot is deployment-ready for platforms like Heroku, Render, Railway, or any cloud provider.

Deploy on Render
Push code to GitHub
Connect repo on Render
Set build command: pip install -r requirements.txt
Set start command: python app.py
Add environment variables:
text

SECRET_KEY=your-production-secret-key
FLASK_ENV=production
PORT=10000
Deploy on Heroku
Create a Procfile:
text

web: python app.py
Deploy via Heroku CLI:
Bash

heroku create zestbot-app
heroku config:set SECRET_KEY=your-production-secret-key
heroku config:set FLASK_ENV=production
git push heroku main
Deploy with Docker
Create a Dockerfile:

Dockerfile

FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=production
CMD ["python", "app.py"]
Bash

docker build -t zestbot .
docker run -p 5000:5000 zestbot
🔒 Security Notes
Issue	Severity	Recommendation
Hardcoded credentials	🔴 High	Use environment variables & hashed passwords
Hardcoded secret key fallback	🔴 High	Always set SECRET_KEY env variable
No password hashing	🔴 High	Use werkzeug.security for hashing
No CSRF protection	🟡 Medium	Add Flask-WTF for CSRF tokens
GET for delete operations	🟡 Medium	Use POST/DELETE HTTP methods
No rate limiting	🟡 Medium	Add Flask-Limiter
SQLite in production	🟡 Medium	Migrate to PostgreSQL for scale
No input sanitization	🟡 Medium	Sanitize user input to prevent XSS
🗺️ Roadmap
 Basic chatbot functionality
 Admin panel with CRUD operations
 Department-wise faculty search
 80+ pre-loaded FAQs
 Session-based authentication
 🔜 Natural Language Processing (NLP) integration
 🔜 Password hashing & secure auth
 🔜 CSRF protection
 🔜 Rate limiting
 🔜 Chat history & analytics
 🔜 Multi-language support
 🔜 Dark mode UI
 🔜 Voice input support
 🔜 Migration to PostgreSQL
 🔜 REST API with token authentication
🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository
Create your feature branch
Bash

git checkout -b feature/amazing-feature
Commit your changes
Bash

git commit -m "Add amazing feature"
Push to the branch
Bash

git push origin feature/amazing-feature
Open a Pull Request
Contribution Ideas
🐛 Bug fixes
🎨 UI/UX improvements
📝 More FAQ entries
🔒 Security enhancements
🧪 Unit tests
📱 Mobile responsive design
🤖 NLP/ML integration
📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

👤 Author
<div align="center">
Overallscam

GitHub

</div>
🙏 Acknowledgments
Flask — Micro web framework for Python
SQLite — Lightweight embedded database
Jinja2 — Templating engine
Amity University, Noida — FAQ content source
<div align="center">
⭐ Star this repository if you found it helpful!
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=6C63FF&center=true&vCenter=true&width=400&lines=Made+with+%E2%9D%A4%EF%B8%8F+using+Python+%26+Flask" alt="Footer" /></div> ```
