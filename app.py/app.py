from flask import Flask, request, send_from_directory, render_template, redirect

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'logo.png')

@app.route("/")
def home():
    return render_template(
        "home.html",
        latest_jobs=latest_jobs[:20],
        results=results[:20],
        admit_cards=admit_cards[:20],
        answers_key=answers_key[:10],
        syllabuss=syllabuss[:10],
        admissions=admissions[:10],
    )

@app.route("/about")
def about():
    return """
    <h1>About Me</h1><p>Mera naam Aryan hai.</p>
    <br><br>
<a href="/">Home Page</a>
"""

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

results = [
    ("UPPSC Staff Nurse 2023 Final Result", "/result/uppsc-staff-nurse-2023"),
    ("UP Police Constable Answer Key 2026 – Out", "/result/up-police-constable-2024"),
    ("RRB ALP 01/2025 CBT-I Result 2026 – Out", "/result/rrb-alp-01-2025-cbt-i-result-2026"),
    ("UPSC CAPF AC 2024 Reserve List", "/result/upsc-capf-ac-2024"),
    ("RRB NTPC CEN 06/2025 Graduate Level Result 2026 - Out", "/result/rrb-ntpc-cen-06-2025-graduate-level"),
    ("BRABU UG 1st Merit List 2026-30", "/result/brabu-ug-1st-merit-list-2026-30"),
    ("BHU CHS SET Result 2026", "/result/bhu-chs-set-result-2026"),
    ("Bihar DCECE Polytechnic Result 2026", "/result/bihar-dcece-polytechnic-result-2026"),
    ("UP Polytechnic JEECUP Answer Key 2026", "/result/up-polytechnic-jeecup-answer-key-2026"),
    ("OFSS Bihar 11th 3rd Merit List 2026 – Soon", "/result/ofss-bihar-11th-2026"),
    ("UPPSC PCS 2024 Marksheet", "/result/uppsc-pcs-2024-marksheet"),
    ("BSF Constable Tradesman PET/PST Result 2026", "/result/bsf-constable-tradesman"),
    ("UPHESC Assistant Professor 2022 Result 2026", "/result/uphesc-assistant-professor-2022"),
    ("MPESB Group 5 Paramedical Post Result 2026", "/result/mpesb-group-5-paramedical-post"),
    ("NTA CUET UG Answer Key 2026 – Out", "/result/nta-cuet-ug"),
    ("UPSSSC BCG Technician 2024 Result", "/result/upsssc-bcg-technician"),
    ("UPSSSC Technical Assistant Group C 2024 Supplementary List", "/result/upsssc-technical-assistant-group-c-2024"),
    ("India Post GDS 4th Merit List 2026", "/result/india-post-gds"),
    ("DDA Group A, B & C Various Posts Marks 2026", "/result/dda-group"),
    ("DSSSB Advt 05/2024 Stenographer Grade-D Result 2026", "/result/dsssb-advt-05-2024"),
    ("SSC MTS / Havaldar Result 2026 – Soon", "/result/ssc-mts"),
    ("RSSB Livestock Assistant Final Result 2026 – Out", "/result/rssb-livestock-assistant"),
]

@app.route("/result")
def lates():
    return render_template(
        "result.html",
        results=results
    )

@app.route("/result/<slug>")
def result_page(slug):
    return render_template(f"result/{slug}.html")

admit_cards = [
    ("UPTET Exam City Details 2026", "/admit/uptet-exam-2026"),
    ("UPSC IES/ ISS Admit Card 2026", "/admit/upsc-ies-iss-2026"),
    ("UPSC Engineering Services Mains Admit Card 2026", "/admit/upsc-engineering-services-mains"),
    ("UPSC Geo Scientist Mains Admit Card 2026", "/admit/upsc-geo-scientist-mains"),
    ("DRDO CEPTAM-11 Tier-II Admit Card 2026", "/admit/drdo-ceptam-11-tier-ii"),
    ("UP Police SI DV/ PST Admit Card / Re-Print Form 2026", "/admit/up-police-si-dv-pst"),
    ("HSSC Police Constable PST Admit Card 2026", "/admit/hssc-police-constable-pst"),
    ("UPPSC Veterinary Officer Exam Date 2026", "/admit/uppsc-veterinary-officer"),
    ("Allahabad University PGAT Admit Card 2026", "/admit/allahabad-university-pgat"),
    ("Bihar Police CSBC Constable GD Exam City / Admit Card 2026", "/admit/bihar-police-csbc-constable-gd"),
    ("RRB NTPC 10+2 UG CBT-I Admit Card 2026", "/admit/rrb-ntpc-10-plus-2-ug-cbt-1"),
    ("NTA UGC NET June Exam City Details 2026", "/admit/nta-ugc-net-june"),
    ("NTA NEET UG Re-Exam City Details 2026", "/admit/nta-neet-ug-2026"),
    ("Indian Army Agniveer CEE Admit Card 2026", "/admit/indian-army-agniveer-cee"),
    ("UP GNM Entrance Exam UPGET Exam City Details 2026", "/admit/up-gnm-entrance-exam-upget"),
    ("SSB Head Constable Ministerial Written Exam Date 2026", "/admit/ssb-head-constable-ministerial"),
    ("UPSSSC Forest/WildLife Guard 2023 Medical Admit Card 2026", "/admit/upsssc-forest-wildlife-guard-2023-medical"),
    ("UP LT Grade Assistant Teacher Mains Admit Card 2026 (Update)", "/admit/up-lt-grade-assistant-teacher"),
    ("UKSSSC VDO, Patwari & Other Post Admit Card 2026", "/admit/uksssc-vdo-patwari"),
    ("Bihar Vidhan Parishad Security Guard Interview Admit Card 2026", "/admit/bihar-vidhan-paishad-security-guard"),
]

@app.route("/admit-card")
def admit_card():
    return render_template(
        "admit-card.html",
        admit_cards=admit_cards
    )

@app.route("/admit/<slug>")
def admit_page(slug):
    return render_template(f"admit-card/{slug}.html")

latest_jobs = [
    ("Railway RRB Technician Online Form 2026 (6565 Posts) – Start", "/job/rrb-technician-2026"),
    ("UP Anganwadi Bharti Online Form 2026 (Updated)", "/job/up-anganwadi-bharti-2026"),
    ("RRB ALP CEN 01/2026 Online Form 2026 (11,127 Posts)", "/job/rrb-alp-2026"),
    ("SSC CGL 2026 Online Form (12,256 Posts)", "/job/ssc-cgl-2026"),
    ("Allahabad High Court RO, ARO & CA Online Form 2026", "/job/allahabad-high-court-ro"),
    ("Central Bank of India Apprentices Online Form 2026", "/job/central-bank-of-india-apprentices"),
    ("Rajasthan State Eligibility Test SET Online Form 2026", "/job/rajasthan-state-eligibility"),
    ("UPSSSC Lower PCS 2026 Online Form (2516 Posts)", "/job/upsssc-lower-pcs-2026"),
    ("UPSSSC Excise Constable Online Form 2026", "/job/upsssc-excise-constable"),
    ("SBI Apprentice Online Form 2026 (7150 Posts) – Extend", "/job/sbi-apprentice-2026"),
    ("Bank of Baroda Apprentices Online Form 2026 (5000 Posts) – Extend", "/job/bank-of-baroda-apprentices-2026"),
    ("UPSSSC Vidhan Bhawan Guard / Fire Guard Online Form 2026", "/job/upsssc-vidhan-bhawan-guard"),
    ("Coal India CIL Management Trainee Online Form 2026 – Extend", "/job/coal-india-cil-management-2026"),
    ("CISF ASI Paramedical Staff Online Form 2026", "/job/cisf-asi-paramedical-staff"),
    ("MPPSC Assistant Professor Online Form 2026", "/job/mppsc-assistant-professor"),
    ("NALCO Non Executive Various Posts Online Form 2026 – Extend", "/job/nalco-non-executive-various-2026"),
    ("SSC Junior Engineer JE Online Post Preference Form 2026", "/job/ssc-junior-engineer-je-2026"),
    ("CTET September Online Form 2026", "/job/ctet-september-2026"),
    ("Hindustan Copper Limited HCL Executive Online Form 2026", "/job/hindustan-copper-limited-hcl-2026"),
    ("UP Board Class 10th/12th Compartment Online Form 2026", "/job/up-board-class-10th-12th-compartment-2026"),
    ("Indian Navy Agniveer Apprentices INET Online Form 2026", "/job/indian-navy-agniveer"),
    ("RSSB CET 10+2 Inter Level Online Form 2026", "/job/rssb-cet-10+2-nter-level"),
]

@app.route("/latest-job")
def latest_job():
    return render_template(
        "latest-job.html",
        latest_jobs=latest_jobs
    )

@app.route("/job/<slug>")
def job_page(slug):
    return render_template(f"latest-job/{slug}.html")

answers_key= [
    ("BPSC AES Answer Key 2026 – Out", "/answer/bpsc-aes-2026"),
    ("SSC Delhi Police Constable (Executive) Final Answer Key 2026 – Out", "/answer/ssc-delhi-police-constable-2026"),
    ("Haryana HTET Answer Key 2026 – Out", "/answer/haryana-htet-2026"),
    ("Bihar DELED Answer Key 2026 – Out", "/answer/bihar-deled-2026"),
    ("UPSSSC Lekhpal Revised Answer Key 2026 – Out", "/answer/upsssc-lekhpal-revised-2026"),
    ("UPSSSC Pharmacist Answer Key 2026 – Out", "/answer/upsssc-pharmacist-2026"),
    ("UPSSSC UP Pollution Control Board Various Post Answer Key 2026 – Out", "/answer/upsssc-up-pollution-control-board-various-2026"),
    ("UPSSSC BCG Technician Answer Key 2026 – Out", "/answer/usssc-bcg-technician-2026"),
    ("NTA NEET UG 2026 Re-Exam Answer Key – Out", "/answer/nta-neet-ug-2026"),
    ("RSSB Agriculture Supervisor Final Answer Key 2026 – Out", "/answer/rssb-agriculture-supervisor"),
    ("UPSC ISS Answer Key 2026 – Out", "/answer/upsc-iss-2026"),
    ("MPESB Forest Guard & Jail Prahari Answer Key 2026", "/answer/mpesb-forest-gurd"),
    ("SSC Delhi Police Head Constable Ministerial Final Answer Key / Marks 2026", "/answer/ssc-delhi-plice-head-constable"),
    ("UP Police Constable Answer Key 2026 – Out", "/answer/up-police-constable"),
    ("SSC GD Constable Answer Key 2026 – Out", "/answer/ssc-gd-constable"),
    ("Bihar BSEB Sakshamta Pariksha Phase 5th Answer Key 2026", "/answer/bihar-bseb-sakshamta-pariksha"),
]

@app.route("/answer-key")
def answer_key():
    return render_template(
        "answer-key.html",
        answers_key=answers_key
    )

@app.route("/answer/<slug>")
def answer_page(slug):
    return render_template(f"answer-key/{slug}.html")

syllabuss = [
    ("UPTET Exam City Details 2026 – Out", "/syllabus/uptet-exam"),
    ("UPSSSC Cane Supervisor Online Form 2026", "/syllabus/upsssc-cane-supervisor"),
    ("UPSSSC Platoon Commander / Block Organizer Online Form 2026", "/syllabus/upsssc-platoon-commander"),
    ("UPSSSC Vidhan Bhawan Guard/ Fire Guard Online Form 2026", "/syllabus/upsssc-vidhan-bhawan-guard"),
    ("UPTET Exam City Details 2026 – Out", "/syllabus/uptet-exam"),
    ("UPSSSC Pharmacist Exam City Details 2026", "/syllabus/upsssc-pharmacist"),
]

@app.route("/syllabus")
def syllabul():
    return render_template(
        "syllabus.html",
        syllabuss=syllabuss
    )

@app.route("/syllabus/<slug>")
def syllabus_page(slug):
    return render_template(f"syllabus/{slug}.html")

admissions = [
    ("UP DGMHUP ANM Training Online Registration 2026", "/admission/up-dgmhup-anm-training-2026"),
    ("Allahabad University CUET UG Online Registration 2026", "/admission/allahabad-university-cute-ug"),
    ("NVS Class 6 Online Form 2027-28", "/admission/nvs-class-6"),
    ("RSSB CET Graduate Level Online Form 2026", "/admission/rssb-cet-graduate-level-2026"),
    ("NEET PG Online Form 2026", "/admission/neet-pg-2026"),
    ("RSSB CET 12th Level Online Form 2026", "/admission/rssb-cet-12th-level-2026"),
    ("Rajasthan State Eligibility Test SET Online Form 2026 – Start", "/admission/rajasthan-State-sligibility-test-set"),
    ("Jharkhand Teacher Eligibility Test Online Form 2026 – Date Extend", "/admission/jharkhand-teacher-eligibility-test"),
    ("Bihar DCECE Polytechnic PE Online Counselling/ Choice Filling 2026", "/admission/bihar-dcece-polytechnic-pe"),
    ("Bihar ITI CAT Counselling/ Choice Filling 2026", "/admission/bihar-iti-cat"),
]

@app.route("/admission")
def admission():
    return render_template(
        "admission.html",
        admissions=admissions
    )

@app.route("/admission/<slug>")
def admission_page(slug):
    return render_template(f"admission/{slug}.html")

@app.route("/contact")
def contact():
    return """
        <html lang="en-IN"> 
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact - Bihar Result</title>

<meta name="description" content="Latest Government Jobs, Admit Cards, Results, 
Admissions, Answer Key and Syllabus updates on Bihar Result.">

<link rel="canonical" href="https://biharresult.com.Bm/contact">

<style>
.mobile-menu{
display:none;
}

@media screen and (max-width:768px){

.desktop-menu{
display:none;
}

.mobile-menu{
display:block;
background:#000080;
padding:15px;
color:white;
}

.mobile-links{
display:none;
background:#000080;
}

.mobile-links a{
display:block;
color:white;
padding:12px;
text-decoration:none;
border-top:1px solid #444;
}
}
</style>
<style>
#overlay{
backdrop-filter: blur(5px);
}
</style>
<style>
ul li{
color:black;
margin-bottom:10px;
}
</style>
<style>
a:link {
    color: blue;
}

a:visited {
    color: blue;
}

a:hover {
    color: darkblue;
}

a:active {
    color: darkblue;
}
</style>
<style>
body{
    margin:0;
    background:#f2f2f2;
    font-family:Arial, sans-serif;
}

.main-container{
    width:1100px;
    margin:0 auto;
    background:#fff;
}

@media (max-width:1100px){
    .main-container{
        width:100%;
    }
}
</style>
<style>
.logo-title{
    display:flex;
    justify-content:center;
    align-items:center;
    gap:8px;
    margin:0;
    color:#fff;
    font-family:'Times New Roman', Georgia, serif;
    font-weight:bold;
    text-transform:uppercase;
    letter-spacing:1px;
    font-size:clamp(28px,7vw,60px);
    white-space:nowrap;
}

.logo-title span{
    font-size:clamp(24px,6vw,50px);
}

.site-name{
    margin:10px 0 0;
    text-align:center;
    color:#fff;
    font-family:Arial,sans-serif;
    font-weight:bold;
    font-size:clamp(15px,3.5vw,26px);
}

@media (max-width:480px){
    .logo-title{
        gap:5px;
        letter-spacing:0;
    }

    .site-name{
        margin-top:6px;
    }
}
</style>
<style>
.social-links{
    text-align:center;
}

.social-links a{
    color:white;
    text-decoration:none;
    margin:10px;
    display:inline-block;
}

@media (max-width:768px){
.social-links{
display:flex;
justify-content:center;
gap:8px;
}

.social-links a{
margin:0 !important;
font-size:14px;
}
}
</style>
</head>

<body style="font-family:Arial;">

<div class="main-container">
    <div style="
background:red;
color:white;
text-align:center;
padding:20px;
width:100%;
box-sizing:border-box;
">
    <a href="/" style="text-decoration:none; color:white;">
    <div class="logo-title">
        <span>📚</span>
        BIHAR RESULT
    </div>
    </a>

    <p class="site-name">
        BiharResult.com.Bm
    </p>

</div>
    <div class="desktop-menu" style="background:blue; padding:12px; text-align:center; font-size:20px;">

<a href="/" style="color:white; text-decoration:none; margin:10px;">Home</a>

<a href="/latest-job" style="color:white; text-decoration:none; margin:10px;">Latest Job</a>

<a href="/admit-card" style="color:white; text-decoration:none; margin:10px;">Admit Card</a>

<a href="/result" style="color:white; text-decoration:none; margin:10px;">Result</a>

<a href="/admission" style="color:white; text-decoration:none; margin:10px;">Admission</a>

<a href="/syllabus" style="color:white; text-decoration:none; margin:10px;">Syllabus</a>

<a href="/answer-key" style="color:white; text-decoration:none; margin:10px;">Answer Key</a>

<div style="position:relative; display:inline-block;">

<a href="javascript:void(0);"
onclick="
var x=document.getElementById('moreMenu');
if(x.style.display=='block'){
x.style.display='none';
}else{
x.style.display='block';
}
"
style="color:white; text-decoration:none; margin:10px;">
More ▼
</a>

<div id="moreMenu" style="
display:none;
position:absolute;
top:35px;
right:0;
background:rgba(0,0,0,0.85);
padding:10px;
border-radius:10px;
min-width:180px;
z-index:999;
">

<a href="/contact" style="color:white; text-decoration:none; display:block; padding:8px;">
Contact Us
</a>

<a href="/privacy" style="color:white; text-decoration:none; display:block; padding:8px;">
Privacy Policy
</a>

<a href="/disclaimer" style="color:white; text-decoration:none; display:block; padding:8px;">
Disclaimer
</a>

</div>

</div>
<a href="javascript:void(0);"
onclick="
var x=document.getElementById('searchBox');
var o=document.getElementById('overlay');

if(x.style.display=='none' || x.style.display==''){
    x.style.display='block';
    o.style.display='block';
}else{
    x.style.display='none';
    o.style.display='none';
}
"
style="color:white; text-decoration:none; font-size:35px;">
🔍
</a>
</div>
<div class="mobile-menu">

<span onclick="
var x=document.getElementById('mobileLinks');
if(x.style.display=='block'){
x.style.display='none';
}else{
x.style.display='block';
}
"
style="font-size:30px;cursor:pointer;">
☰ Menu
</span>

<span
onclick="
var x=document.getElementById('searchBox');
var o=document.getElementById('overlay');

if(x.style.display=='none' || x.style.display==''){
    x.style.display='block';
    o.style.display='block';
}else{
    x.style.display='none';
    o.style.display='none';
}
"
style="float:right;font-size:30px;cursor:pointer;color:white;">
🔍
</span>

<div id="mobileLinks" class="mobile-links">

<a href="/">Home</a>
<a href="/latest-job">Latest Job</a>
<a href="/admit-card">Admit Card</a>
<a href="/result">Result</a>
<a href="/admission">Admission</a>
<a href="/syllabus">Syllabus</a>
<a href="/answer-key">Answer Key</a>
<a href="/contact">Contact Us</a>
<a href="/privacy">Privacy Policy</a>
<a href="/disclaimer">Disclaimer</a>

</div>

</div>
<div id="overlay"
onclick="
document.getElementById('overlay').style.display='none';
document.getElementById('searchBox').style.display='none';
"
style="
display:none;
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.6);
z-index:999;
">
</div>

<div id="searchBox"
style="
display:none;
position:fixed;
top:50%;
left:50%;
transform:translate(-50%,-50%);
width:90%;
max-width:500px;
background:transparent;
padding:15px;
border-radius:10px;
text-align:center;
z-index:1000;
">

<form action="/search" method="get"
style="
display:flex;
align-items:center;
justify-content:center;
gap:8px;
">

<input
type="text"
name="q"
placeholder="🔍 Search Jobs, Results, Admit Card..."
style="
width:320px;
max-width:70%;
padding:12px;
background:white;
color:black;
border:2px solid green;
border-radius:25px;
font-size:16px;
outline:none;
">

<button
type="submit"
style="
padding:12px 18px;
background:blue;
color:white;
border:none;
border-radius:25px;
font-size:16px;
cursor:pointer;
white-space:nowrap;
">
Search
</button>

</form>

</div>

<h1 style="text-align:center;">Contact Us</h1>
<hr>

<div style="
max-width:900px;
margin:25px auto;
background:#fff;
border:1px solid #ccc;
border-radius:8px;
padding:25px;
box-shadow:0 0 8px rgba(0,0,0,0.15);
line-height:1.8;
font-size:18px;
">

<h2 style="margin-top:0;">
<span style="color:red;">Contact with BiharResult.com.Bm</span>
</h2>

<p>
Welcome to <strong>BiharResult.com.Bm</strong>.
If you have any questions, suggestions, corrections or feedback regarding Government Jobs,
Admit Cards, Results, Admissions, Answer Keys or Syllabus updates, feel free to contact us.
Our team will try to respond as soon as possible.
</p>

<p>
<strong>हम BiharResult.com.Bm पर आपका स्वागत करते हैं।</strong>
यदि आपको हमारी वेबसाइट से संबंधित कोई प्रश्न, सुझाव, सुधार या सहायता चाहिए,
तो आप हमसे संपर्क कर सकते हैं। हमारी टीम आपकी सहायता करने का पूरा प्रयास करेगी।
</p>

<hr>

<h2 style="color:#B22222;text-align:center;">
Contact Information
</h2>

<p>
<b>Email:</b><br>
<a href="mailto:biharresult@gmail.com">
biharresult@gmail.com
</a>
</p>

<p>
<b>Website:</b><br>
<a href="https://biharresult.com.Bm">
https://biharresult.com.Bm
</a>
</p>

<hr>

<h2>Content Transparency</h2>

<p>
All information published on BiharResult.com.Bm is collected from official notifications,
government websites and trusted public sources.
Although we try our best to keep every update accurate and timely,
users are advised to verify important information from the official website before taking any action.
</p>

<p>
BiharResult.com.Bm पर प्रकाशित सभी जानकारी आधिकारिक नोटिफिकेशन,
सरकारी वेबसाइटों तथा विश्वसनीय स्रोतों से ली जाती है।
फिर भी किसी भी आवेदन या निर्णय से पहले आधिकारिक वेबसाइट पर जानकारी अवश्य जांच लें।
</p>

<hr>

<h2>Support</h2>

<p>
For any correction request, feedback or reporting an issue,
please email us with complete details.
We appreciate your valuable suggestions.
</p>

<p style="text-align:center;font-weight:bold;font-size:22px;">
Team BiharResult.com.Bm
</p>

</div>

<h2 style="
background:red;
color:white;
text-align:center;
padding:10px;
margin-top:20px;
">
Bihar Result 10+2 Latest Job
</h2>

<p style="
text-align:center;
padding:15px;
line-height:1.8;
font-size:18px;
">
Bihar Result par aapko Latest Government Jobs,
Admit Cards, Results, Admissions, Answer Keys,
Syllabus aur Exam Updates ki jankari milti hai.
Yahan Bihar aur India bhar ki Sarkari Naukri ki
latest updates uplabdh karayi jati hain.
</p>

<table style="
width:100%;
border-collapse:collapse;
text-align:center;
margin-bottom:20px;
">

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Result</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Police Result</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Jobs</a>
</td>
</tr>

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Admission</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Exam</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Results Hindi</a>
</td>
</tr>

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Result 2026</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Latest Bihar Jobs</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Vacancy</a>
</td>
</tr>

</table>
<h2 style="
background:#B22222;
color:white;
text-align:center;
padding:10px;
">
About Bihar Result
</h2>

<div style="
border:1px solid #ccc;
padding:15px;
line-height:1.8;
font-size:17px;
">

Bihar Result ek educational portal hai jahan aap
Latest Jobs, Admit Cards, Results, Answer Keys,
Admissions aur Syllabus ki jankari prapt kar sakte hain.

Hamari koshish hai ki students aur job seekers ko
sahi aur latest information ek hi jagah par mile.

</div>
<h2 style="
background:#006400;
color:white;
text-align:center;
padding:10px;
">
Frequently Asked Questions (FAQ)
</h2>

<div style="
border:1px solid #ccc;
padding:15px;
line-height:1.8;
font-size:17px;
">

<b>Q. Bihar Result kya hai?</b><br>
A. Bihar Result ek educational portal hai jahan latest jobs, admit cards aur results ki jankari milti hai.

<br><br>

<b>Q. Kya Bihar Result free hai?</b><br>
A. Haan, website ka upyog bilkul free hai.

<br><br>

<b>Q. Yahan kis type ki information milti hai?</b><br>
A. Government Jobs, Results, Admit Cards, Admissions, Answer Keys aur Syllabus.

<br><br>

<b>Q. Kya yeh official website hai?</b><br>
A. Nahi, yeh ek information portal hai. Official notification hamesha official website se verify karein.

</div>
<hr>

<div style="
background:#222;
color:white;
text-align:center;
padding:20px;
margin-top:20px;
">

<h3 style="margin-bottom:12px;">Connect With Us</h3>

<div class="social-links">

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📢 Telegram
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📺 YouTube
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📘 Facebook
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📷 Instagram
</a>

</div>

<p style="margin:20px 0;">
© 2026 Bihar Result | All Rights Reserved
</p>

<p>
<a href="/about" style="color:yellow;">About</a> |
<a href="/contact" style="color:yellow;">Contact</a> |
<a href="/privacy" style="color:yellow;">Privacy Policy</a> |
<a href="/disclaimer" style="color:yellow;">Disclaimer</a>
</p>
</div>

</body>
</html>
"""

@app.route("/privacy")
def privacy():
    return """
    <html lang="en-IN"> 

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Privacy Policy - Bihar Result</title>

<meta name="description" content="Latest Government Jobs, Admit Cards, Results, Admissions, Answer Key and Syllabus updates on Bihar Result.">

<link rel="canonical" href="https://biharresult.com.Bm/privacy">

<style>
.mobile-menu{
display:none;
}

@media screen and (max-width:768px){

.desktop-menu{
display:none;
}

.mobile-menu{
display:block;
background:#000080;
padding:15px;
color:white;
}

.mobile-links{
display:none;
background:#000080;
}

.mobile-links a{
display:block;
color:white;
padding:12px;
text-decoration:none;
border-top:1px solid #444;
}
}
</style>
<style>
#overlay{
backdrop-filter: blur(5px);
}
</style>
<style>
ul li{
color:black;
margin-bottom:10px;
}
</style>
<style>
a:link {
    color: blue;
}

a:visited {
    color: blue;
}

a:hover {
    color: darkblue;
}

a:active {
    color: darkblue;
}
</style>
<style>
body{
    margin:0;
    background:#f2f2f2;
    font-family:Arial, sans-serif;
}

.main-container{
    width:1100px;
    margin:0 auto;
    background:#fff;
}

@media (max-width:1100px){
    .main-container{
        width:100%;
    }
}
</style>
<style>
.logo-title{
    display:flex;
    justify-content:center;
    align-items:center;
    gap:8px;
    margin:0;
    color:#fff;
    font-family:'Times New Roman', Georgia, serif;
    font-weight:bold;
    text-transform:uppercase;
    letter-spacing:1px;
    font-size:clamp(28px,7vw,60px);
    white-space:nowrap;
}

.logo-title span{
    font-size:clamp(24px,6vw,50px);
}

.site-name{
    margin:10px 0 0;
    text-align:center;
    color:#fff;
    font-family:Arial,sans-serif;
    font-weight:bold;
    font-size:clamp(15px,3.5vw,26px);
}

@media (max-width:480px){
    .logo-title{
        gap:5px;
        letter-spacing:0;
    }

    .site-name{
        margin-top:6px;
    }
}
</style>
<style>
.social-links{
    text-align:center;
}

.social-links a{
    color:white;
    text-decoration:none;
    margin:10px;
    display:inline-block;
}

@media (max-width:768px){
.social-links{
display:flex;
justify-content:center;
gap:8px;
}

.social-links a{
margin:0 !important;
font-size:14px;
}
}
</style>
<style>
@media (max-width:768px){
.faq-heading{
font-size:20px;
padding:10px 5px !important;
}
}
</style>
</head>

<body style="font-family:Arial;">

<div class="main-container">
    <div style="
background:red;
color:white;
text-align:center;
padding:20px;
width:100%;
box-sizing:border-box;
">
    <a href="/" style="text-decoration:none; color:white;">
    <div class="logo-title">
        <span>📚</span>
        BIHAR RESULT
    </div>
    </a>

    <p class="site-name">
        BiharResult.com.Bm
    </p>

</div>
    <div class="desktop-menu" style="background:blue; padding:12px; text-align:center; font-size:20px;">

<a href="/" style="color:white; text-decoration:none; margin:10px;">Home</a>

<a href="/latest-job" style="color:white; text-decoration:none; margin:10px;">Latest Job</a>

<a href="/admit-card" style="color:white; text-decoration:none; margin:10px;">Admit Card</a>

<a href="/result" style="color:white; text-decoration:none; margin:10px;">Result</a>

<a href="/admission" style="color:white; text-decoration:none; margin:10px;">Admission</a>

<a href="/syllabus" style="color:white; text-decoration:none; margin:10px;">Syllabus</a>

<a href="/answer-key" style="color:white; text-decoration:none; margin:10px;">Answer Key</a>

<div style="position:relative; display:inline-block;">

<a href="javascript:void(0);"
onclick="
var x=document.getElementById('moreMenu');
if(x.style.display=='block'){
x.style.display='none';
}else{
x.style.display='block';
}
"
style="color:white; text-decoration:none; margin:10px;">
More ▼
</a>

<div id="moreMenu" style="
display:none;
position:absolute;
top:35px;
right:0;
background:rgba(0,0,0,0.85);
padding:10px;
border-radius:10px;
min-width:180px;
z-index:999;
">

<a href="/contact" style="color:white; text-decoration:none; display:block; padding:8px;">
Contact Us
</a>

<a href="/privacy" style="color:white; text-decoration:none; display:block; padding:8px;">
Privacy Policy
</a>

<a href="/disclaimer" style="color:white; text-decoration:none; display:block; padding:8px;">
Disclaimer
</a>

</div>

</div>
<a href="javascript:void(0);"
onclick="
var x=document.getElementById('searchBox');
var o=document.getElementById('overlay');

if(x.style.display=='none' || x.style.display==''){
    x.style.display='block';
    o.style.display='block';
}else{
    x.style.display='none';
    o.style.display='none';
}
"
style="color:white; text-decoration:none; font-size:35px;">
🔍
</a>
</div>
<div class="mobile-menu">

<span onclick="
var x=document.getElementById('mobileLinks');
if(x.style.display=='block'){
x.style.display='none';
}else{
x.style.display='block';
}
"
style="font-size:30px;cursor:pointer;">
☰ Menu
</span>

<span
onclick="
var x=document.getElementById('searchBox');
var o=document.getElementById('overlay');

if(x.style.display=='none' || x.style.display==''){
    x.style.display='block';
    o.style.display='block';
}else{
    x.style.display='none';
    o.style.display='none';
}
"
style="float:right;font-size:30px;cursor:pointer;color:white;">
🔍
</span>

<div id="mobileLinks" class="mobile-links">

<a href="/">Home</a>
<a href="/latest-job">Latest Job</a>
<a href="/admit-card">Admit Card</a>
<a href="/result">Result</a>
<a href="/admission">Admission</a>
<a href="/syllabus">Syllabus</a>
<a href="/answer-key">Answer Key</a>
<a href="/contact">Contact Us</a>
<a href="/privacy">Privacy Policy</a>
<a href="/disclaimer">Disclaimer</a>

</div>

</div>
<div id="overlay"
onclick="
document.getElementById('overlay').style.display='none';
document.getElementById('searchBox').style.display='none';
"
style="
display:none;
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.6);
z-index:999;
">
</div>

<div id="searchBox"
style="
display:none;
position:fixed;
top:50%;
left:50%;
transform:translate(-50%,-50%);
width:90%;
max-width:500px;
background:transparent;
padding:15px;
border-radius:10px;
text-align:center;
z-index:1000;
">

<form action="/search" method="get"
style="
display:flex;
align-items:center;
justify-content:center;
gap:8px;
">

<input
type="text"
name="q"
placeholder="🔍 Search Jobs, Results, Admit Card..."
style="
width:320px;
max-width:70%;
padding:12px;
background:white;
color:black;
border:2px solid green;
border-radius:25px;
font-size:16px;
outline:none;
">

<button
type="submit"
style="
padding:12px 18px;
background:blue;
color:white;
border:none;
border-radius:25px;
font-size:16px;
cursor:pointer;
white-space:nowrap;
">
Search
</button>

</form>

</div>
<h1 style="text-align:center;">Privacy Policy</h1>
<hr>

<div style="
max-width:900px;
margin:25px auto;
background:#fff;
border:1px solid #ccc;
border-radius:8px;
padding:25px;
box-shadow:0 0 8px rgba(0,0,0,0.15);
">

<h1 style="font-size:48px;margin-top:0;">
<span style="color:red;">Privacy Policy</span>
</h1>

<hr>

<p>
Welcome to <strong>BiharResult.com.Bm</strong>.
We are committed to protecting your privacy.
This Privacy Policy explains what information we collect
and how we use it.
</p>

<h2>Information We Collect</h2>

<p>
जब आप हमारी वेबसाइट का उपयोग करते हैं, तब कुछ सामान्य जानकारी
स्वचालित रूप से एकत्रित हो सकती है।
</p>

<ul>
<li>नाम (यदि आप स्वयं प्रदान करें)</li>
<li>Email Address</li>
<li>Browser Information</li>
<li>Device Information</li>
<li>IP Address</li>
<li>Visited Pages</li>
</ul>

<h2>How We Use Your Information</h2>

<ul>
<li>Website को बेहतर बनाने के लिए।</li>
<li>User Experience सुधारने के लिए।</li>
<li>नई Government Jobs एवं Updates देने के लिए।</li>
<li>Contact Request का उत्तर देने के लिए।</li>
</ul>

<h2>How We Protect Your Information</h2>

<p>
हम आपकी जानकारी की सुरक्षा के लिए उचित सुरक्षा उपाय अपनाते हैं।
हालांकि इंटरनेट पर 100% सुरक्षा की गारंटी नहीं दी जा सकती।
</p>

<h2>Cookies</h2>

<p>
हम वेबसाइट को बेहतर बनाने के लिए Cookies का उपयोग कर सकते हैं।
आप चाहें तो अपने Browser से Cookies Disable कर सकते हैं।
</p>

<h2>Third Party Links</h2>

<p>
हमारी वेबसाइट पर Official Websites के लिंक हो सकते हैं।
हम उन वेबसाइटों की Privacy Policy के लिए जिम्मेदार नहीं हैं।
</p>

<h2>Google Services</h2>

<p>
भविष्य में हमारी वेबसाइट Google Analytics, Google AdSense
या अन्य Google Services का उपयोग कर सकती है।
</p>

<h2>Changes to This Privacy Policy</h2>

<p>
यह Privacy Policy समय-समय पर अपडेट की जा सकती है।
नई Policy इसी पेज पर प्रकाशित की जाएगी।
</p>

<h2>Contact Us</h2>

<p>
यदि Privacy Policy से संबंधित कोई प्रश्न हो तो संपर्क करें:
</p>

<a href="mailto:biharresult@gmail.com">biharresult@gmail.com</a>

</div>

<h2 style="
background:red;
color:white;
text-align:center;
padding:10px;
margin-top:20px;
">
Bihar Result 10+2 Latest Job
</h2>

<p style="
text-align:center;
padding:15px;
line-height:1.8;
font-size:18px;
">
Bihar Result par aapko Latest Government Jobs,
Admit Cards, Results, Admissions, Answer Keys,
Syllabus aur Exam Updates ki jankari milti hai.
Yahan Bihar aur India bhar ki Sarkari Naukri ki
latest updates uplabdh karayi jati hain.
</p>

<table style="
width:100%;
border-collapse:collapse;
text-align:center;
margin-bottom:20px;
">

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Result</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Police Result</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Jobs</a>
</td>
</tr>

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Admission</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Exam</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Results Hindi</a>
</td>
</tr>

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Result 2026</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Latest Bihar Jobs</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Vacancy</a>
</td>
</tr>

</table>
<h2 style="
background:#B22222;
color:white;
text-align:center;
padding:10px;
">
About Bihar Result
</h2>

<div style="
border:1px solid #ccc;
padding:15px;
line-height:1.8;
font-size:17px;
">

Bihar Result ek educational portal hai jahan aap
Latest Jobs, Admit Cards, Results, Answer Keys,
Admissions aur Syllabus ki jankari prapt kar sakte hain.

Hamari koshish hai ki students aur job seekers ko
sahi aur latest information ek hi jagah par mile.

</div>
<h2 style="
background:#006400;
color:white;
text-align:center;
padding:10px;
">
Frequently Asked Questions (FAQ)
</h2>

<div style="
border:1px solid #ccc;
padding:15px;
line-height:1.8;
font-size:17px;
">

<b>Q. Bihar Result kya hai?</b><br>
A. Bihar Result ek educational portal hai jahan latest jobs, admit cards aur results ki jankari milti hai.

<br><br>

<b>Q. Kya Bihar Result free hai?</b><br>
A. Haan, website ka upyog bilkul free hai.

<br><br>

<b>Q. Yahan kis type ki information milti hai?</b><br>
A. Government Jobs, Results, Admit Cards, Admissions, Answer Keys aur Syllabus.

<br><br>

<b>Q. Kya yeh official website hai?</b><br>
A. Nahi, yeh ek information portal hai. Official notification hamesha official website se verify karein.

</div>
<hr>

<div style="
background:#222;
color:white;
text-align:center;
padding:20px;
margin-top:20px;
">

<h3 style="margin-bottom:12px;">Connect With Us</h3>

<div class="social-links">

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📢 Telegram
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📺 YouTube
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📘 Facebook
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📷 Instagram
</a>

</div>

<p style="margin:20px 0;">
© 2026 Bihar Result | All Rights Reserved
</p>

<p>
<a href="/about" style="color:yellow;">About</a> |
<a href="/contact" style="color:yellow;">Contact</a> |
<a href="/privacy" style="color:yellow;">Privacy Policy</a> |
<a href="/disclaimer" style="color:yellow;">Disclaimer</a>
</p>
</div>

</body>
</html>
"""

@app.route("/disclaimer")
def disclaimer():
    return """
        <html lang="en-IN"> 

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Read the Disclaimer of Bihar Result. 
This website provides educational information about government jobs, results, admit cards, admissions, syllabus and answer keys.">
<title>Disclaimer - Bihar Result</title>

<meta name="description" content="Latest Government Jobs, Admit Cards, Results, Admissions, Answer Key and Syllabus updates on Bihar Result.">

<link rel="canonical" href="https://biharresult.com.Bm/disclaimer">

<style>
.mobile-menu{
display:none;
}

@media screen and (max-width:768px){

.desktop-menu{
display:none;
}

.mobile-menu{
display:block;
background:#000080;
padding:15px;
color:white;
}

.mobile-links{
display:none;
background:#000080;
}

.mobile-links a{
display:block;
color:white;
padding:12px;
text-decoration:none;
border-top:1px solid #444;
}
}
</style>
<style>
#overlay{
backdrop-filter: blur(5px);
}
</style>
<style>
ul li{
color:black;
margin-bottom:10px;
}
</style>
<style>
a:link {
    color: blue;
}

a:visited {
    color: blue;
}

a:hover {
    color: darkblue;
}

a:active {
    color: darkblue;
}
</style>
<style>
body{
    margin:0;
    background:#f2f2f2;
    font-family:Arial, sans-serif;
}

.main-container{
    width:1100px;
    margin:0 auto;
    background:#fff;
}

@media (max-width:1100px){
    .main-container{
        width:100%;
    }
}
</style>
<style>
.logo-title{
    display:flex;
    justify-content:center;
    align-items:center;
    gap:8px;
    margin:0;
    color:#fff;
    font-family:'Times New Roman', Georgia, serif;
    font-weight:bold;
    text-transform:uppercase;
    letter-spacing:1px;
    font-size:clamp(28px,7vw,60px);
    white-space:nowrap;
}

.logo-title span{
    font-size:clamp(24px,6vw,50px);
}

.site-name{
    margin:10px 0 0;
    text-align:center;
    color:#fff;
    font-family:Arial,sans-serif;
    font-weight:bold;
    font-size:clamp(15px,3.5vw,26px);
}

@media (max-width:480px){
    .logo-title{
        gap:5px;
        letter-spacing:0;
    }

    .site-name{
        margin-top:6px;
    }
}
</style>
<style>
.social-links{
    text-align:center;
}

.social-links a{
    color:white;
    text-decoration:none;
    margin:10px;
    display:inline-block;
}

@media (max-width:768px){
.social-links{
display:flex;
justify-content:center;
gap:8px;
}

.social-links a{
margin:0 !important;
font-size:14px;
}
}
</style>
<style>
@media (max-width:768px){
.faq-heading{
font-size:20px;
padding:10px 5px !important;
}
}
</style>
</head>

<body style="font-family:Arial;">

<div class="main-container">
    <div style="
background:red;
color:white;
text-align:center;
padding:20px;
width:100%;
box-sizing:border-box;
">
    <a href="/" style="text-decoration:none; color:white;">
    <div class="logo-title">
        <span>📚</span>
        BIHAR RESULT
    </div>
    </a>

    <p class="site-name">
        BiharResult.com.Bm
    </p>

</div>
    <div class="desktop-menu" style="background:blue; padding:12px; text-align:center; font-size:20px;">

<a href="/" style="color:white; text-decoration:none; margin:10px;">Home</a>

<a href="/latest-job" style="color:white; text-decoration:none; margin:10px;">Latest Job</a>

<a href="/admit-card" style="color:white; text-decoration:none; margin:10px;">Admit Card</a>

<a href="/result" style="color:white; text-decoration:none; margin:10px;">Result</a>

<a href="/admission" style="color:white; text-decoration:none; margin:10px;">Admission</a>

<a href="/syllabus" style="color:white; text-decoration:none; margin:10px;">Syllabus</a>

<a href="/answer-key" style="color:white; text-decoration:none; margin:10px;">Answer Key</a>

<div style="position:relative; display:inline-block;">

<a href="javascript:void(0);"
onclick="
var x=document.getElementById('moreMenu');
if(x.style.display=='block'){
x.style.display='none';
}else{
x.style.display='block';
}
"
style="color:white; text-decoration:none; margin:10px;">
More ▼
</a>

<div id="moreMenu" style="
display:none;
position:absolute;
top:35px;
right:0;
background:rgba(0,0,0,0.85);
padding:10px;
border-radius:10px;
min-width:180px;
z-index:999;
">

<a href="/contact" style="color:white; text-decoration:none; display:block; padding:8px;">
Contact Us
</a>

<a href="/privacy" style="color:white; text-decoration:none; display:block; padding:8px;">
Privacy Policy
</a>

<a href="/disclaimer" style="color:white; text-decoration:none; display:block; padding:8px;">
Disclaimer
</a>

</div>

</div>
<a href="javascript:void(0);"
onclick="
var x=document.getElementById('searchBox');
var o=document.getElementById('overlay');

if(x.style.display=='none' || x.style.display==''){
    x.style.display='block';
    o.style.display='block';
}else{
    x.style.display='none';
    o.style.display='none';
}
"
style="color:white; text-decoration:none; font-size:35px;">
🔍
</a>
</div>
<div class="mobile-menu">

<span onclick="
var x=document.getElementById('mobileLinks');
if(x.style.display=='block'){
x.style.display='none';
}else{
x.style.display='block';
}
"
style="font-size:30px;cursor:pointer;">
☰ Menu
</span>

<span
onclick="
var x=document.getElementById('searchBox');
var o=document.getElementById('overlay');

if(x.style.display=='none' || x.style.display==''){
    x.style.display='block';
    o.style.display='block';
}else{
    x.style.display='none';
    o.style.display='none';
}
"
style="float:right;font-size:30px;cursor:pointer;color:white;">
🔍
</span>

<div id="mobileLinks" class="mobile-links">

<a href="/">Home</a>
<a href="/latest-job">Latest Job</a>
<a href="/admit-card">Admit Card</a>
<a href="/result">Result</a>
<a href="/admission">Admission</a>
<a href="/syllabus">Syllabus</a>
<a href="/answer-key">Answer Key</a>
<a href="/contact">Contact Us</a>
<a href="/privacy">Privacy Policy</a>
<a href="/disclaimer">Disclaimer</a>

</div>

</div>
<div id="overlay"
onclick="
document.getElementById('overlay').style.display='none';
document.getElementById('searchBox').style.display='none';
"
style="
display:none;
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.6);
z-index:999;
">
</div>

<div id="searchBox"
style="
display:none;
position:fixed;
top:50%;
left:50%;
transform:translate(-50%,-50%);
width:90%;
max-width:500px;
background:transparent;
padding:15px;
border-radius:10px;
text-align:center;
z-index:1000;
">

<form action="/search" method="get"
style="
display:flex;
align-items:center;
justify-content:center;
gap:8px;
">

<input
type="text"
name="q"
placeholder="🔍 Search Jobs, Results, Admit Card..."
style="
width:320px;
max-width:70%;
padding:12px;
background:white;
color:black;
border:2px solid green;
border-radius:25px;
font-size:16px;
outline:none;
">

<button
type="submit"
style="
padding:12px 18px;
background:blue;
color:white;
border:none;
border-radius:25px;
font-size:16px;
cursor:pointer;
white-space:nowrap;
">
Search
</button>

</form>

</div>
<h1 style="text-align:center;">Disclaimer</h1>
<hr>

<div style="
max-width:900px;
margin:25px auto;
background:#fff;
border:1px solid #ccc;
border-radius:8px;
padding:25px;
box-shadow:0 0 8px rgba(0,0,0,0.15);
line-height:1.8;
font-size:18px;
text-align:center;
">

<p>
<strong style="color:#0047AB;">BiharResult.com.Bm</strong> is a private website that is not associated, endorsed or affiliated with any government institution, agency or department.
The content available on this website is published only for informational purposes and has been collected from various reliable sources.
Although we try our best to keep the information accurate and updated, we do not make any guarantee regarding the completeness, accuracy, reliability or availability of the information.
</p>

<hr>

<p>
<strong style="color:#0047AB;">BiharResult.com.Bm</strong> एक निजी वेबसाइट है जो किसी भी सरकारी संस्था, एजेंसी या विभाग से संबद्ध नहीं है।
इस वेबसाइट पर उपलब्ध सामग्री केवल सूचना के उद्देश्य से प्रकाशित की जाती है और विभिन्न विश्वसनीय स्रोतों से संकलित की गई है।
यद्यपि हम जानकारी को सही और अद्यतन रखने का प्रयास करते हैं, फिर भी हम इसकी पूर्णता, सटीकता, विश्वसनीयता या उपलब्धता की कोई गारंटी नहीं देते।
</p>

<p>
<b><i>Team BiharResult.com.Bm</i></b>
</p>

<hr>

<p>
Users are advised to independently verify all information before making any decision based on the content available on this website.
We shall not be responsible for any loss, error, omission or consequence arising from the use of this information.
Any reliance you place on the information is strictly at your own risk.
</p>

<hr>

<p>
उपयोगकर्ताओं को सलाह दी जाती है कि इस वेबसाइट की जानकारी के आधार पर कोई भी निर्णय लेने से पहले संबंधित आधिकारिक वेबसाइट से जानकारी की पुष्टि अवश्य करें।
इस वेबसाइट पर दी गई जानकारी के उपयोग से होने वाले किसी भी नुकसान, त्रुटि या परिणाम के लिए हम जिम्मेदार नहीं होंगे।
इस जानकारी पर आपकी निर्भरता पूरी तरह आपके अपने जोखिम पर होगी।
</p>

<p>
<b><i>Team BiharResult.com.Bm</i></b>
</p>

</div>

<h2 style="
background:red;
color:white;
text-align:center;
padding:10px;
margin-top:20px;
">
Bihar Result 10+2 Latest Job
</h2>

<p style="
text-align:center;
padding:15px;
line-height:1.8;
font-size:18px;
">
Bihar Result par aapko Latest Government Jobs,
Admit Cards, Results, Admissions, Answer Keys,
Syllabus aur Exam Updates ki jankari milti hai.
Yahan Bihar aur India bhar ki Sarkari Naukri ki
latest updates uplabdh karayi jati hain.
</p>

<table style="
width:100%;
border-collapse:collapse;
text-align:center;
margin-bottom:20px;
">

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Result</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Police Result</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Jobs</a>
</td>
</tr>

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Admission</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Exam</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Results Hindi</a>
</td>
</tr>

<tr>
<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Result 2026</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Latest Bihar Jobs</a>
</td>

<td style="border:1px solid black;padding:8px;">
<a href="#">Bihar Vacancy</a>
</td>
</tr>

</table>
<h2 style="
background:#B22222;
color:white;
text-align:center;
padding:10px;
">
About Bihar Result
</h2>

<div style="
border:1px solid #ccc;
padding:15px;
line-height:1.8;
font-size:17px;
">

Bihar Result ek educational portal hai jahan aap
Latest Jobs, Admit Cards, Results, Answer Keys,
Admissions aur Syllabus ki jankari prapt kar sakte hain.

Hamari koshish hai ki students aur job seekers ko
sahi aur latest information ek hi jagah par mile.

</div>
<h2 style="
background:#006400;
color:white;
text-align:center;
padding:10px;
">
Frequently Asked Questions (FAQ)
</h2>

<div style="
border:1px solid #ccc;
padding:15px;
line-height:1.8;
font-size:17px;
">

<b>Q. Bihar Result kya hai?</b><br>
A. Bihar Result ek educational portal hai jahan latest jobs, admit cards aur results ki jankari milti hai.

<br><br>

<b>Q. Kya Bihar Result free hai?</b><br>
A. Haan, website ka upyog bilkul free hai.

<br><br>

<b>Q. Yahan kis type ki information milti hai?</b><br>
A. Government Jobs, Results, Admit Cards, Admissions, Answer Keys aur Syllabus.

<br><br>

<b>Q. Kya yeh official website hai?</b><br>
A. Nahi, yeh ek information portal hai. Official notification hamesha official website se verify karein.

</div>
<hr>

<div style="
background:#222;
color:white;
text-align:center;
padding:20px;
margin-top:20px;
">

<h3 style="margin-bottom:12px;">Connect With Us</h3>

<div class="social-links">

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📢 Telegram
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📺 YouTube
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📘 Facebook
</a>

<a href="#" style="color:white;text-decoration:none;margin:10px;">
📷 Instagram
</a>

</div>

<p style="margin:20px 0;">
© 2026 Bihar Result | All Rights Reserved
</p>

<p>
<a href="/about" style="color:yellow;">About</a> |
<a href="/contact" style="color:yellow;">Contact</a> |
<a href="/privacy" style="color:yellow;">Privacy Policy</a> |
<a href="/disclaimer" style="color:yellow;">Disclaimer</a>
</p>
</div>

</body>
</html>
"""

@app.route("/search")
def search():
    q = request.args.get("q", "").lower()

    if "result" in q:
        return redirect("/result")

    elif "admit" in q:
        return redirect("/admit-card")

    elif "job" in q:
        return redirect("/latest-job")
    
    elif "answer" in q:
        return redirect("/answer-key")
    
    elif "syllabus" in q:
        return redirect("/syllabus")
    
    elif "admission" in q:
        return redirect("/admission")
    
    elif "contact" in q:
        return redirect("/contact")
    
    elif "privacy" in q:
        return redirect("/privacy")
    
    elif "disclaimer" in q:
        return redirect("/disclaimer")

    else:
        return redirect("/")


@app.route("/upsssc-lower-pcs")
def upsssc_lower_pcs():
    return """
    <div style="background:red; color:white; text-align:center; padding:20px;">
        <h1>UPSSsC Lower PCS Form</h1>
    </div>

    <h2>Railway UPSSsC Lower PCS Recruitment 2026</h2>

    <p>Total Posts: 2516</p>

    <table border="1" width="100%" cellpadding="10">
        <tr>
            <th>Important Dates</th>
            <th>Application Fee</th>
        </tr>

        <tr>
            <td>
                Apply Start : 10 July 2026<br>
                Last Date : 15 August 2026
            
            Last Date For Fee Paymet :
                Correction Last Date :
             </td>

        
                Exam Date :
                Admit Card :
                Result Date :
                Candidates Are Advised To Connfirm From The
                 UPSSSC Official Website
            </td>

            <td>
                General/OBC: ₹25<br>
                SC/ST: ₹25
                PH Candidates: ₹25
            Payment Mode (Online):You Can Make The
            Payment Using The Following Methods:
                Debit Card
                Creadit Card
                Internet Banking
                IMPS
                Cash Card/Mobile Wallet
            </td>
        </tr>
    </table>

    <br>
    <a href="/">Home Page</a>
    """

@app.route("/daiy-5-minutes-meditation")
def daiy_5_minutes_meditation():
    return """
    <div style="background:red; color:white; text-align:center; padding:20px;">
        <h1>Daiy 5 Minutes Meditation</h1>
    </div>

    <h2>Daiy 5 Minutes Meditation</h2>

    <p>Total Posts: 10000</p>

    <table border="1" width="100%" cellpadding="10">
        <tr>
            <th>Important Dates</th>
            <th>Application Fee</th>
        </tr>

        <tr>
            <td>
                Apply Start: 10 July 2026<br>
                Last Date: 15 August 2026
            </td>

            <td>
                General/OBC: ₹500<br>
                SC/ST: ₹250
            </td>
        </tr>
    </table>

    <br>
    <a href="/">Home Page</a>
    """



@app.route("/ssc-2026")
def ssc_2026():
    return """
    <div style="background:red; color:white; text-align:center; padding:20px;">
        <h1>BIHAR RESULT</h1>
    </div>

    <h2>SSC GD Result</h2>
    <h2>SSC GD Online forme 2026</h2>

    <p>Total Posts: 9,970</p>

    <table border="1" width="100%" cellpadding="10">
        <tr>
            <th>Important Dates</th>
            <th>Application Fee</th>
        </tr>

        <tr>
            <td>
                Apply Start: 10 July 2026<br>
                Last Date: 15 August 2026
            </td>

            <td>
                General/OBC: ₹500<br>
                SC/ST: ₹250
            </td>
        </tr>
    </table>

    <br>
    <a href="/">Home Page</a>
    """

@app.route("/railway-2026")
def railway_2026():
    return """
    <div style="background:red; color:white; text-align:center; padding:20px;">
        <h1>BIHAR RESULT</h1>
    </div>

    <h2>Railway Result</h2>

    <p>Total Posts: 9,970</p>

    <table border="1" width="100%" cellpadding="10">
        <tr>
            <th>Important Dates</th>
            <th>Application Fee</th>
        </tr>

        <tr>
            <td>
                Apply Start: 10 July 2026<br>
                Last Date: 15 August 2026
            </td>

            <td>
                General/OBC: ₹500<br>
                SC/ST: ₹250
            </td>
        </tr>
    </table>

    <br>
    <a href="/">Home Page</a>
    """

@app.route("/up-police-2026")
def up_2026():
    return """
    <div style="background:red; color:white; text-align:center; padding:20px;">
        <h1>BIHAR RESULT</h1>
    </div>

    <h2>UP Police Result</h2>

    <p>Total Posts: 9,970</p>

    <table border="1" width="100%" cellpadding="10">
        <tr>
            <th>Important Dates</th>
            <th>Application Fee</th>
        </tr>

        <tr>
            <td>
                Apply Start: 10 July 2026<br>
                Last Date: 15 August 2026
            </td>

            <td>
                General/OBC: ₹500<br>
                SC/ST: ₹250
            </td>
        </tr>
    </table>

    <br>
    <a href="/">Home Page</a>
    """


@app.route("/nta-neet-ug-re-exam-city")
def nta_neet_ug_re_exam_city():
    return """
    <div style="background:red; color:white; text-align:center; padding:20px;">
        <h1>BIHAR RESULT</h1>
    </div>

    <h2>NEET UG Re-Exam City Details</h2>

    <p>Total Posts: 9,970</p>

    <table border="1" width="100%" cellpadding="10">
        <tr>
            <th>Important Dates</th>
            <th>Application Fee</th>
        </tr>

        <tr>
            <td>
                Apply Start: 10 July 2026<br>
                Last Date: 15 August 2026
            </td>

            <td>
                General/OBC: ₹500<br>
                SC/ST: ₹250
            </td>
        </tr>
    </table>

    <br>
    <a href="/">Home Page</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
