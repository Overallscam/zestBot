import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import sqlite3
from datetime import timedelta
from faq_data import SAMPLE_FAQS, FACULTY_BY_DEPARTMENT

app = Flask(__name__)
# Use environment variable for secret key in production
app.secret_key = os.environ.get('SECRET_KEY', 'zesta-super-secret-key-12345')
app.permanent_session_lifetime = timedelta(hours=24)

# Create database and sample data
def setup_database():
    conn = sqlite3.connect('zesta.db')
    cursor = conn.cursor()
    
    # Create FAQs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    
    # Add sample FAQs if table is empty
    cursor.execute('SELECT COUNT(*) FROM faqs')
    if cursor.fetchone()[0] == 0:
        # Import FAQs from separate file to keep code clean
        for question, answer in SAMPLE_FAQS:
            cursor.execute('INSERT INTO faqs (question, answer) VALUES (?, ?)', (question, answer))
    
    conn.commit()
    conn.close()

# Find matching answer for user question
def get_answer(user_question):
    user_question_lower = user_question.lower()
    
    # Check for department-specific faculty queries first
    department_answer = check_department_query(user_question_lower)
    if department_answer:
        return department_answer
    
    # Regular FAQ search
    conn = sqlite3.connect('zesta.db')
    cursor = conn.cursor()
    cursor.execute('SELECT question, answer FROM faqs')
    faqs = cursor.fetchall()
    conn.close()
    
    best_answer = "I'm sorry, I don't have information about that. Try asking something else!"
    best_score = 0
    
    for db_question, db_answer in faqs:
        db_question_lower = db_question.lower()
        
        # Simple word matching
        user_words = user_question_lower.split()
        score = 0
        for word in user_words:
            if word in db_question_lower:
                score += 1
        
        if score > best_score:
            best_score = score
            best_answer = db_answer
    
    return best_answer

def check_department_query(user_question):
    """Check if user is asking about a specific department's faculty"""
    
    # Department keyword mappings
    department_keywords = {
        'engineering': ['engineering', 'engineer', 'technology', 'tech', 'aset', 'ait', 'ase', 'mechanical', 'electrical'],
        'law': ['law', 'legal', 'aials', 'criminal'],
        'business_management': ['business', 'management', 'mba', 'aibs', 'aib', 'commerce', 'aicism'],
        'applied_sciences': ['science', 'physics', 'nanotechnology', 'applied science'],
        'medical_life_sciences': ['medical', 'medicine', 'life science', 'neuroscience', 'biotechnology', 'genome', 'ainn', 'aifw', 'aimmscr', 'aige'],
        'social_sciences': ['social science', 'sociology', 'aiss', 'psychology'],
        'administration': ['administration', 'admin', 'vice chancellor', 'director']
    }
    
    # Check if question contains faculty-related keywords
    faculty_keywords = ['faculty', 'teacher', 'professor', 'staff', 'who teaches', 'who are the']
    has_faculty_keyword = any(keyword in user_question for keyword in faculty_keywords)
    
    if has_faculty_keyword:
        # Find which department is being asked about
        for dept_key, keywords in department_keywords.items():
            if any(keyword in user_question for keyword in keywords):
                dept_info = FACULTY_BY_DEPARTMENT[dept_key]
                faculty_list = '\n• '.join(dept_info['faculty'])
                
                return f"""**{dept_info['name'].upper()} FACULTY:**
• {faculty_list}

These are the faculty members in the {dept_info['name']} department at Amity University, Noida."""
    
    return None

# Routes
@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message', '').strip()
    if not user_message:
        return jsonify({'answer': 'Please ask me something!'})
    
    answer = get_answer(user_message)
    return jsonify({'answer': answer})

@app.route('/admin')
@app.route('/admin/login')
def admin_login():
    # If already logged in, go to panel
    if session.get('logged_in') == True:
        return redirect(url_for('admin_panel'))
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    
    # Simple hardcoded check
    if username == 'admin' and password == 'zesta123':
        session.permanent = True
        session['logged_in'] = True
        session['username'] = 'admin'
        flash('Welcome to Zesta Admin Panel!', 'success')
        return redirect(url_for('admin_panel'))
    else:
        flash('Invalid username or password. Try admin/zesta123', 'error')
        return redirect(url_for('admin_login'))

@app.route('/admin/panel')
def admin_panel():
    # Check if logged in
    if not session.get('logged_in'):
        flash('Please login to access admin panel', 'error')
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('zesta.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM faqs ORDER BY id')
    faqs = cursor.fetchall()
    conn.close()
    
    return render_template('admin_panel.html', faqs=faqs)

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/admin/status')
def admin_status():
    """Simple route to check login status"""
    if session.get('logged_in'):
        return f"✅ Logged in as: {session.get('username')}<br><a href='/admin/panel'>Go to Admin Panel</a><br><a href='/admin/logout'>Logout</a>"
    else:
        return f"❌ Not logged in<br><a href='/admin'>Login</a>"

@app.route('/admin/add', methods=['POST'])
def add_faq():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    question = request.form.get('question', '').strip()
    answer = request.form.get('answer', '').strip()
    
    if question and answer:
        conn = sqlite3.connect('zesta.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO faqs (question, answer) VALUES (?, ?)', (question, answer))
        conn.commit()
        conn.close()
        flash('FAQ added successfully!', 'success')
    else:
        flash('Please fill in both question and answer.', 'error')
    
    return redirect(url_for('admin_panel'))

@app.route('/admin/edit/<int:faq_id>')
def edit_faq(faq_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('zesta.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM faqs WHERE id = ?', (faq_id,))
    faq = cursor.fetchone()
    conn.close()
    
    if not faq:
        flash('FAQ not found!', 'error')
        return redirect(url_for('admin_panel'))
    
    return render_template('edit_faq.html', faq=faq)

@app.route('/admin/update/<int:faq_id>', methods=['POST'])
def update_faq(faq_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    question = request.form.get('question', '').strip()
    answer = request.form.get('answer', '').strip()
    
    if question and answer:
        conn = sqlite3.connect('zesta.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE faqs SET question = ?, answer = ? WHERE id = ?', (question, answer, faq_id))
        conn.commit()
        conn.close()
        flash('FAQ updated successfully!', 'success')
    else:
        flash('Please fill in both question and answer.', 'error')
    
    return redirect(url_for('admin_panel'))

@app.route('/admin/delete/<int:faq_id>')
def delete_faq(faq_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('zesta.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM faqs WHERE id = ?', (faq_id,))
    conn.commit()
    conn.close()
    flash('FAQ deleted!', 'success')
    
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    setup_database()
    print("🤖 Starting Zesta AI...")
    print("💻 Visit: http://localhost:5000")
    print("🔐 Admin: http://localhost:5000/admin (admin/zesta123)")
    # Use environment port for deployment, fallback to 5000 for local
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)
