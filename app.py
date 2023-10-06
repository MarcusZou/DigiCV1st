from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Edward-Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "DIGITAL RESUME | EDWARD ZOU"
PAGE_ICON = ":wave:"
NAME = "Edward Zou"
DESCRIPTION = """
Hey there, this is Edward Zou. As a 4th year Computer Science student, ready to graduate this upcoming May from the University of British Columbia, I'm interested in full stack development, machine learning, APIs, and databases. In my free time, I like to watch movies and exercise to help me relax.
"""
EMAIL = "edwardzou10@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/edward-zou-0416a5188/",
    "Github": "https://github.com/edwzou",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 LAYERS: A virtual fitting room for everyone": "https://github.com/edwzou/Layers",
    "🏆 insightUBC: A query tool accessing UBC's metadata": "https://github.com/edwzou/",
    "🏆 ⚡️Flash: A marketplace for UBC tutors": "https://github.com/edwzou/flash",
    "🏆 ezSpringBoot: My Spring boot application": "https://github.com/edwzou/spring-boot-application",
    "🏆 NBA League Simulator: An NBA team tracker": "https://github.com/edwzou/NBA-League-Simulator",
}


st.set_page_config(page_title=PAGE_TITLE,
                   page_icon=PAGE_ICON, layout="centered")

# --- LOAD CSS, PDF & PROFILR PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([0.3, 0.7], gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- QUALIFICATIONS & CERTIFICATIONS ---
st.write("#")
st.subheader("QUALIFICATIONS & CERTIFICATIONS")
st.write(
    """
- ✔️ Frontend Development experience as Coop Intern with Dodge Construction Network
- ✔️ Full stack development / leadership as a Chief Innovation Officer with Popular Innovation Inc.
- ✔️ Microsoft Certified Azure Developer Associate (AZ-204) in 2023
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks and challenges
- ✔️ Top skills: Front-End Development • Databases • Back-End Web Development • Web Services API • Team Leadership
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("TECHNICAL SKILLS")
st.write(
    """
- 👩‍💻 Languages: Java, Python, C/C++, SQL (Postgres), JavaScript, TypeScript, HTML/CSS, R, Haskell
- 📊 Data Science and Blockchain techniques with hands on experience
- 📚 Frameworks: Angular, React, Node.js, Express, Spring, Docker, Azure Functions
- 🗄️ Developer Tools: Git, Docker, VS Code, Google Cloud Platform, Azure Portal, PyCharm, IntelliJ, Eclipse
"""
)


# --- WORK EXPERIENCE ---
st.write("#")
st.subheader("WORK EXPERIENCE")
st.write("---")


# --- Job 1 ---
st.write("#")
st.write("🚧", "**Software Engineering Co-op, Front-End | Dodge Construction Network**")
st.write("Jan. 2022 - Aug. 2022 || Vancouver, BC")
st.write(
    """
- ► Developed high quality software and features in accordance with team requirements and feedback
- ► Diagnosed and resolved a performance issue, resulting in a 30% increase in page rendering speed
- ► Implemented unit test code and provided assistance in additional relevant test automation
- ► Played a key role in advancing ongoing enhancements for both existing and future systems
- ► Worked closely with other functional groups including Quality Assurance, Operations and Client Services
- Skills: TypeScript · Quality Assurance · Scrum · Debugging · Front-End Development
"""
)

# --- Job 2 ---
st.write("#")
st.write("🚧", "**Co-Founder and Chief Innovation Officer | Popular Innovation Inc.**")
st.write("Jul. 2019 - Jun. 2021 || Calgary, AB")
st.write(
    """
- ► Influenced and directed IT infrastructure to drive key business strategies and processes
- ► Applied emerging technology knowledge to achieve key business objectives
- ► Built agile and responsive teams to maintain cloud-based and stand-alone systems
- ► Collaborated seamlessly with various teams throughout the duration of different projects and milestones
- ► Served as member on the board of directors
- Skills: Management · Startups · Cloud Applications · Artificial Intelligence (AI) · Team Leadership
"""
)

# --- Job 3 ---
st.write("#")
st.write("🚧", "**Data Analyst and Blockchain Engineer | HACCTECH Ltd.**")
st.write("May 2021 - Aug. 2021 || Calgary, AB")
st.write(
    """
- ► Utilized Python/SQL to conduct various Data Analytic tasks, including data wrangling, exploratory data analysis,
data trending, feature extraction, pattern interpretation, BI dashboard with Tableau
- ► Fully implemented blockchain ecosystem by integrating cryptography, Ethereum, coupling with designing,
multi-threaded coding, testing, troubleshooting, and evaluating blockchain projects
- Skills: Application Develepment · Artificial Intelligence (AI) · Blockchain ecosystem · Data Analysis
"""
)

# --- PROJECTS ---
st.write("#")
st.subheader("PROJECTS")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
