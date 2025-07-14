# Amity University FAQ Data
# This file contains all the FAQ questions and answers for the Zesta chatbot

# Department-wise Faculty Information
FACULTY_BY_DEPARTMENT = {
    "administration": {
        "name": "Administration",
        "faculty": [
            "Dr. Balvinder Shukla – Vice Chancellor, University Administration",
            "Prof. Kaiser Singh – Director, Student Affairs & Sports, ASET",
            "Dr. Sujata Khandai – Director, ACCF (Business)"
        ]
    },
    "engineering": {
        "name": "Engineering & Technology",
        "faculty": [
            "Prof. (Dr.) K. M. Soni – Deputy Dean, ASET (Mechanical/Electrical)",
            "Dr. Om Prakash Sinha – Director, AIT (Technology/Engineering)",
            "Dr. Shalini Singh Sharma – Director, ASE (School of Engineering)",
            "Dr. Bedatri Moulik – Assistant Professor (III), Technology (AIT)"
        ]
    },
    "law": {
        "name": "Law",
        "faculty": [
            "Prof. (Dr.) Tahir Mahmood – Honorary Chairman, AIALS (Law School)",
            "Atul Jain – Assistant Professor, Criminal Law"
        ]
    },
    "applied_sciences": {
        "name": "Applied Sciences",
        "faculty": [
            "Sunita Negi – Assistant Professor, Physics",
            "Prof. Ramesh Namdeo Pudake – Assistant Professor (III), Nanotechnology",
            "Dr. Ajit Varma – Distinguished Scientist & Professor of Eminence"
        ]
    },
    "social_sciences": {
        "name": "Social Sciences (AISS)",
        "faculty": [
            "Dr. Madhumita Saha – Associate Professor",
            "Dr. Shachee Agnihotri – Assistant Professor (II)",
            "Dr. Sucharita Sen – Assistant Professor (I)",
            "Dr. Smita – Assistant Professor (I)"
        ]
    },
    "medical_life_sciences": {
        "name": "Medical & Life Sciences",
        "faculty": [
            "Dr. Mallika Chatterjee – Associate Professor, Neuropsychology & Neurosciences (AINN)",
            "Dr. Rishikesh Kumar Gupta – Assistant Professor (II), AINN",
            "Dr. Sujeet Kumar Singh – Assistant Professor (II), Forestry & Wildlife (AIFW)",
            "Dr. Kajal Kanchan – Associate Professor, Molecular Medicine & Stem Cell Research",
            "Dr. Veerendra Kumar – Associate Professor & Ramalingaswami Fellow, AIMMSCR",
            "Dr. Adhiraj Roy – Associate Professor & Ramalingaswami Fellow, AIMMSCR",
            "Dr. Manoj Kumar – Professor, Genome Engineering (AIGE)"
        ]
    },
    "business_management": {
        "name": "Business & Management",
        "faculty": [
            "Dr. Chanderdeep Tandon – Director, AIB (Biotechnology)",
            "Dr. Nidhee Chaudhary – Professor, AIB",
            "Dr. Rachana Singh – Professor, AIB",
            "Pratima Chaudhuri – Professor, AIB",
            "Dr. Sabari Ghosal – Professor, AIB",
            "Dr. Shoma Paul Nandi – Professor, AIB",
            "Dr. Ajit Mittal – Professor, AIBS",
            "Dr. Mamta Mohan – Professor, AIBS",
            "Dr. Shikha Kapoor – Professor, AIBS",
            "V. P. Kakkar – Professor, AIBS",
            "C. Ranjan Bhandari – Professor, AICISM (Management)"
        ]
    },
    "other_departments": {
        "name": "Other Departments",
        "faculty": [
            "Dr. Raman Malik – Assistant Professor (I), Institute of English Studies & Research",
            "Dr. Bidisha Banerji – Associate Professor & Deputy Director, Public Policy (AIPP)",
            "Dr. Eshan Parikh – Assistant Professor (I), Film & Drama (ASFD)",
            "Dr. Ranjana Bhatia – Director, AIPAS (Psychology & Allied Sciences)",
            "Dr. Santosh Pal Singh – Director, ASNRSD (Nutrition, Sports & Disability Studies)",
            "Dr. Gurinder Singh – Director General, AIBS (International Business)"
        ]
    }
}

SAMPLE_FAQS = [
    ("What is Zesta?", "Zesta is your friendly AI assistant that can answer questions and help you with information."),
    ("How do I use Zesta?", "Simply type your question in the chat box and I'll do my best to help you!"),
    ("What can you help me with?", "I can answer questions about various topics, provide information, and have conversations with you."),
    ("Are you available 24/7?", "Yes! I'm always here and ready to help you anytime you need assistance."),
    ("How accurate are your answers?", "I try my best to provide accurate information based on my knowledge. For important matters, please verify with reliable sources."),
    
    # COMPREHENSIVE FACULTY INFORMATION
    ("Who are the faculty members at Amity University?", """Here are key faculty members at Amity University, Noida organized by departments:

**ADMINISTRATION:**
• Dr. Balvinder Shukla – Vice Chancellor, University Administration
• Prof. Kaiser Singh – Director, Student Affairs & Sports, ASET
• Dr. Sujata Khandai – Director, ACCF (Business)

**ENGINEERING & TECHNOLOGY:**
• Prof. (Dr.) K. M. Soni – Deputy Dean, ASET (Mechanical/Electrical)
• Dr. Om Prakash Sinha – Director, AIT (Technology/Engineering)
• Dr. Shalini Singh Sharma – Director, ASE (School of Engineering)
• Dr. Bedatri Moulik – Assistant Professor (III), Technology (AIT)

**LAW:**
• Prof. (Dr.) Tahir Mahmood – Honorary Chairman, AIALS (Law School)
• Atul Jain – Assistant Professor, Criminal Law

**APPLIED SCIENCES:**
• Sunita Negi – Assistant Professor, Physics
• Prof. Ramesh Namdeo Pudake – Assistant Professor (III), Nanotechnology
• Dr. Ajit Varma – Distinguished Scientist & Professor of Eminence

**SOCIAL SCIENCES (AISS):**
• Dr. Madhumita Saha – Associate Professor
• Dr. Shachee Agnihotri – Assistant Professor (II)
• Dr. Sucharita Sen – Assistant Professor (I)
• Dr. Smita – Assistant Professor (I)

**MEDICAL & LIFE SCIENCES:**
• Dr. Mallika Chatterjee – Associate Professor, Neuropsychology & Neurosciences (AINN)
• Dr. Rishikesh Kumar Gupta – Assistant Professor (II), AINN
• Dr. Sujeet Kumar Singh – Assistant Professor (II), Forestry & Wildlife (AIFW)
• Dr. Kajal Kanchan – Associate Professor, Molecular Medicine & Stem Cell Research
• Dr. Veerendra Kumar – Associate Professor & Ramalingaswami Fellow, AIMMSCR
• Dr. Adhiraj Roy – Associate Professor & Ramalingaswami Fellow, AIMMSCR
• Dr. Manoj Kumar – Professor, Genome Engineering (AIGE)

**BUSINESS & MANAGEMENT:**
• Dr. Chanderdeep Tandon – Director, AIB (Biotechnology)
• Dr. Nidhee Chaudhary – Professor, AIB
• Dr. Rachana Singh – Professor, AIB
• Pratima Chaudhuri – Professor, AIB
• Dr. Sabari Ghosal – Professor, AIB
• Dr. Shoma Paul Nandi – Professor, AIB
• Dr. Ajit Mittal – Professor, AIBS
• Dr. Mamta Mohan – Professor, AIBS
• Dr. Shikha Kapoor – Professor, AIBS
• V. P. Kakkar – Professor, AIBS
• C. Ranjan Bhandari – Professor, AICISM (Management)

**OTHER DEPARTMENTS:**
• Dr. Raman Malik – Assistant Professor (I), Institute of English Studies & Research
• Dr. Bidisha Banerji – Associate Professor & Deputy Director, Public Policy (AIPP)
• Dr. Eshan Parikh – Assistant Professor (I), Film & Drama (ASFD)
• Dr. Ranjana Bhatia – Director, AIPAS (Psychology & Allied Sciences)
• Dr. Santosh Pal Singh – Director, ASNRSD (Nutrition, Sports & Disability Studies)
• Dr. Gurinder Singh – Director General, AIBS (International Business)

This is a comprehensive list of faculty across various departments and institutes at Amity University, Noida."""),
    
    # DEPARTMENT-SPECIFIC FACULTY QUESTIONS
    ("Who are the engineering faculty at Amity?", f"""**ENGINEERING & TECHNOLOGY FACULTY:**
• {chr(10).join(FACULTY_BY_DEPARTMENT['engineering']['faculty'])}

The engineering department includes ASET (Amity School of Engineering & Technology), AIT (Amity Institute of Technology), and ASE (Amity School of Engineering)."""),
    
    ("Who teaches in the law department?", f"""**LAW FACULTY:**
• {chr(10).join(FACULTY_BY_DEPARTMENT['law']['faculty'])}

The law department operates under AIALS (Amity Institute of Advanced Legal Studies)."""),
    
    ("Who are the business faculty at Amity?", f"""**BUSINESS & MANAGEMENT FACULTY:**
• {chr(10).join(FACULTY_BY_DEPARTMENT['business_management']['faculty'])}

This includes faculty from AIB (Amity International Business School), AIBS (Amity Institute of Business Studies), and AICISM (Amity Institute of Supply Chain & Integrated Studies in Commerce Management)."""),
    
    ("Who teaches in applied sciences?", f"""**APPLIED SCIENCES FACULTY:**
• {chr(10).join(FACULTY_BY_DEPARTMENT['applied_sciences']['faculty'])}

This includes Physics, Nanotechnology, and other applied science disciplines."""),
    
    ("Who are the medical faculty at Amity?", f"""**MEDICAL & LIFE SCIENCES FACULTY:**
• {chr(10).join(FACULTY_BY_DEPARTMENT['medical_life_sciences']['faculty'])}

This includes faculty from AINN (Amity Institute of Neuropsychology & Neurosciences), AIFW (Amity Institute of Forestry & Wildlife), AIMMSCR (Amity Institute of Molecular Medicine & Stem Cell Research), and AIGE (Amity Institute of Genome Engineering)."""),
    
    ("Who are the social sciences faculty?", f"""**SOCIAL SCIENCES FACULTY (AISS):**
• {chr(10).join(FACULTY_BY_DEPARTMENT['social_sciences']['faculty'])}

AISS stands for Amity Institute of Social Sciences."""),
    
    # GENERAL LEADERSHIP QUESTIONS
    ("Who is the Vice Chancellor of Amity University?", "Dr. Balvinder Shukla is the Vice Chancellor of Amity University, Noida. He oversees the University Administration."),
    
    ("Who are the directors at Amity University?", """Key Directors at Amity University include:
• Dr. Sujata Khandai – Director, ACCF (Business)
• Dr. Chanderdeep Tandon – Director, AIB (Biotechnology)  
• Dr. Ranjana Bhatia – Director, AIPAS (Psychology & Allied Sciences)
• M. S. Prasad – Director, AISST (Science & Technology)
• Dr. Om Prakash Sinha – Director, AIT (Technology/Engineering)
• Dr. M. Sajnani – Director, AITT (Teacher Training)
• Dr. Shalini Singh Sharma – Director, ASE (School of Engineering)
• A. P. Singh – Director, ASIBAS (Biological & Agricultural Sciences)
• Dr. Santosh Pal Singh – Director, ASNRSD (Nutrition, Sports & Disability Studies)
• Dr. Gurinder Singh – Director General, AIBS (International Business)"""),
    
    # ADMISSIONS FAQs
    ("How can I apply to Amity University Noida?", "You can apply online via www.amity.edu or visit the campus for offline forms."),
    ("Is there any entrance exam for B.Tech at Amity Noida?", "Yes, Amity JEE or valid JEE Main scores are accepted."),
    ("What is the application fee for Amity Noida?", "₹1,500 (subject to change)."),
    ("Can I apply for multiple courses at once?", "Yes, but you must pay separate fees for each."),
    ("What are the eligibility criteria for BBA?", "Minimum 60% in 10+2 from a recognized board."),
    ("Is direct admission possible at Amity?", "Merit-based admission is available for some programs without entrance."),
    ("Is the admission process completely online?", "Yes, including form submission and interviews."),
    ("What documents are needed during admission?", "10th & 12th mark sheets, ID proof, passport-size photo, migration certificate."),
    ("When does the admission cycle start?", "Usually in January each year."),
    ("Is there any age limit for admission?", "No strict limit, but typical UG age is 17+."),
    
    # ACADEMICS FAQs
    ("Does Amity Noida follow a semester system?", "Yes, there are two semesters: July–Dec and Jan–May."),
    ("What grading system is followed?", "10-point GPA system."),
    ("Are classes conducted in English?", "Yes, English is the medium of instruction."),
    ("Are elective subjects offered?", "Yes, a wide range of interdisciplinary electives are available."),
    ("Is attendance compulsory?", "Yes, minimum 75% attendance is required."),
    ("Are there minors and specialization options?", "Yes, most programs offer minors and major electives."),
    ("Can students opt for dual degree programs?", "Integrated courses like B.Tech + MBA are offered."),
    ("Are final year projects mandatory?", "Yes, across most UG and PG programs."),
    ("Are international exchange programs available?", "Yes, via Amity's Global Study Programs."),
    ("Is research encouraged at the UG level?", "Yes, especially in engineering, biotech, and science streams."),
    
    # PLACEMENTS FAQs
    ("What is the placement rate at Amity Noida?", "Over 90% in some schools."),
    ("What is the highest placement package?", "₹45 LPA (international offer)."),
    ("Which companies recruit from Amity?", "Accenture, Infosys, Amazon, TCS, Deloitte, Wipro, etc."),
    ("Is there a placement cell?", "Yes, the Corporate Resource Center (CRC)."),
    ("Are internships compulsory?", "Yes, summer internships are part of the curriculum."),
    ("Does Amity offer soft skills training?", "Yes, including communication, aptitude, and personality development."),
    ("Do startups visit for placements?", "Yes, especially in tech and management fields."),
    ("Can students get PPOs?", "Yes, from companies post-internship."),
    ("Is campus placement guaranteed?", "Not guaranteed, but ample support is provided."),
    ("Can I pursue government jobs from Amity?", "Yes, students are eligible for PSU and government recruitment."),
    
    # FEES & SCHOLARSHIPS FAQs
    ("What is the fee structure for B.Tech?", "Around ₹2–3 LPA (varies by specialization)."),
    ("Is the fee different for international students?", "Yes, NRI/foreign category has separate fees."),
    ("Are scholarships available?", "Yes, based on merit, sports, and financial need."),
    ("What is the refund policy?", "Refunds follow UGC norms and vary by date of withdrawal."),
    ("Is there a payment installment option?", "Yes, in select cases with prior approval."),
    ("Can I pay fees online?", "Yes, through the Amity Microsite or official website."),
    ("What scholarships are offered for MBA?", "Based on CAT/MAT/GMAT scores and academic merit."),
    ("Are education loans accepted?", "Yes, from major banks (Amity provides loan assistance letters)."),
    ("Is the hostel fee included in tuition?", "No, it's charged separately."),
    ("Are scholarships renewed every year?", "Yes, if the student maintains minimum CGPA."),
    
    # CAMPUS LIFE & CLUBS FAQs
    ("What extracurricular activities are offered?", "Dance, music, dramatics, tech clubs, sports, MUNs, etc."),
    ("Does Amity have student clubs?", "Yes, over 100 clubs across departments."),
    ("Are there fests and cultural events?", "Yes, events like Amiphoria and Sangathan are annual highlights."),
    ("Is there a gym on campus?", "Yes, a fully equipped gym."),
    ("Are there student councils or leadership bodies?", "Yes, each department has class representatives and councils."),
    ("Is ragging allowed?", "No, Amity has a zero-tolerance ragging policy."),
    ("Is there a dress code?", "No formal code, though professional attire is expected in certain programs."),
    ("What sports facilities are available?", "Cricket, football, basketball, tennis, gym, and more."),
    ("Can students organize events?", "Yes, with faculty approval."),
    ("Are there mentorship programs?", "Yes, students are assigned faculty mentors."),
    
    # HOSTEL & ACCOMMODATION FAQs
    ("Are hostels available at Amity Noida?", "Yes, both AC and non-AC hostels."),
    ("What are hostel fees?", "₹85,000 to ₹1.6 lakh per year, depending on room type."),
    ("Is hostel allocation first-come-first-serve?", "Yes, early application is recommended."),
    ("Do hostels have Wi-Fi?", "Yes, 24x7 Wi-Fi is provided."),
    ("Is there a curfew for hostel students?", "Yes, usually 7:30 PM for UG girls, later for others."),
    ("Are day scholars allowed?", "Yes, local students can commute."),
    ("Are visitors allowed in hostels?", "Only during designated hours with ID proof."),
    ("Are meals included in hostel fees?", "Yes, with 3 meals + snacks per day."),
    ("Are laundry facilities available?", "Yes, paid and free options exist."),
    ("Is hostel life safe?", "Yes, with 24/7 security and CCTV surveillance."),
    
    # FACULTY & DEPARTMENTS FAQs
    ("Who is the Vice-Chancellor of Amity Noida?", "Prof. (Dr.) Balvinder Shukla."),
    ("Who is the Dean of Engineering?", "Prof. (Dr.) K.M. Soni (ASET)."),
    ("Is the faculty qualified?", "Yes, most have PhDs and industry experience."),
    ("How many departments does Amity Noida have?", "Over 60+ academic departments."),
    ("Do faculty conduct research?", "Yes, many are active researchers with publications."),
    ("Can students interact freely with faculty?", "Yes, faculty mentoring is part of the system."),
    ("Does Amity have guest lectures?", "Yes, from global academicians and CEOs."),
    ("Are there industry-experienced faculty?", "Yes, in management, media, law, and tech."),
    ("Can students work under professors?", "Yes, as research interns or assistants."),
    ("Is faculty feedback collected?", "Yes, anonymously via student portals."),
    
    # INTERNATIONAL PROGRAMS FAQs
    ("Does Amity offer semester abroad programs?", "Yes, through Amity Global Study."),
    ("Which universities does Amity partner with?", "Harvard Business Online, Purdue, NYU, and others."),
    ("Is the degree valid abroad?", "Yes, UGC-recognized degrees are accepted globally."),
    ("Are dual degree programs available internationally?", "Yes, 1+1 or 2+2 collaborations exist."),
    ("Is IELTS/TOEFL required for exchanges?", "Depends on the destination university."),
    ("Do foreign professors teach at Amity?", "Yes, via guest lectures and exchange programs."),
    ("Are there international conferences?", "Yes, hosted regularly in multiple disciplines."),
    ("Can students intern abroad?", "Yes, via exchange or personal arrangements."),
    ("Are there cultural exchange programs?", "Yes, especially in humanities and business."),
    ("Are international students allowed?", "Yes, via Amity International office."),
    
    # GENERAL & MISCELLANEOUS FAQs
    ("Is Amity Noida UGC recognized?", "Yes, and NAAC A+ accredited."),
    ("Where is Amity University Noida located?", "Sector 125, Noida, Uttar Pradesh, India."),
    ("Is Amity a private or public university?", "It is a private university."),
    ("What are the contact details for admissions?", "Email: admissions@amity.edu; Phone: 0120-2445252."),
    ("Does Amity have an alumni network?", "Yes, through Amity Alumni Association."),
    ("Can alumni access campus services?", "Yes, including networking and career portals."),
    ("Is there a grievance redressal cell?", "Yes, for students and parents."),
    ("Is there medical support on campus?", "Yes, a full-time medical unit and ambulance service."),
    ("Are there transport/bus facilities?", "Yes, across NCR regions."),
    ("What are the campus timings?", "Usually 9 AM to 5 PM, depending on program."),
    ("Is the campus Wi-Fi enabled?", "Yes, for both students and faculty."),
    ("Are pets allowed in hostels?", "No, pets are not allowed."),
    ("Can I defer my admission?", "In special cases, yes, with valid reason."),
    ("Is there a lost & found office?", "Yes, managed by admin."),
    ("Is mobile usage allowed in class?", "No, unless faculty permits for academic use."),
    ("Are there gender-neutral restrooms?", "Some buildings may have accessible facilities."),
    ("What is Amity's policy on plagiarism?", "Strictly prohibited; Turnitin and similar tools are used."),
    ("Can I pursue part-time jobs?", "Only off-campus, and not during class hours."),
    ("Is there Wi-Fi in academic blocks?", "Yes, for registered devices."),
    ("Is Amity a good university?", "Yes, it's ranked among the top private universities in India for academics and placements.")
]
