from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "picture-cv.jpg"


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mitzio Ercambrack"
PAGE_ICON = ":smiley_cat:"
NAME = " Mitzio Ercambrack"
DESCRIPTION = """
Data Analyst & Engenier.
"""
EMAIL = "machetearte58@gmail.com"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    #"Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#---background---
page_bd = f''' 
    <style>
        [data-testid = "stMain"]{{
                background: #020024;
                background: linear-gradient(90deg,rgba(2, 0, 36, 1) 0%, rgba(9, 9, 121, 1) 35%, rgba(0, 212, 255, 1) 100%);
        }}
    </style>
'''
st.markdown(page_bd, unsafe_allow_html=True)

# --- LOAD CSS, PDF & PROFIL PIC ---
#with open(css_file) as f:
    #st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
load_css(css_file)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "⬇️ Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        key="download"
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ +10 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, NumPy, DLT, DBT, Airflow, Etc..), Airbyte, SQL, VBA, Docker
- 📊 Data Visulization: PowerBI, MS Excel, Plotly, Streamlit
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL, MS SQL Server
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Desarrollador Jr | Neoris de México SA de CV**")
st.write("Junio 2019 - Present")
st.write(
    """
    - ► Diseño e implementación de bases de datos, procesos ETL/ELT y 
        pipelines en Python. Desarrollo de Dashboards en Power BI con DAX, 
        conectados a múltiples fuentes (SQL, Data Lake, Excel, API), orientados 
        a alta dirección, gerencia y supervisión. Creación y consumo de 
        datawarehouse y datalake, análisis de producto, generación de insights, 
        diseño de KPI/SLA/OLA al igual que otros indicadores de valor, 
        presentaciones estratégicas para la toma de decisiones, así como su 
        conducción en la mismas. 
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Developer | Grupo Scanda**")
st.write("Feb 2018 - May 2019")
st.write(
    """
- ► Experiencia en diseño e implementación de bases de datos, procesos 
    ETL/ELT y pipelines en Python. Desarrollo de Dashboards en Power BI 
    con DAX, conectados a múltiples fuentes (SQL, Data Lake, Excel, API), 
    enfocados en la toma de decisiones para alta dirección, gerencia y 
    supervisión, atención de requerimientos. Generación de insights, 
    reportes automatizados, y creación/consumo de datawarehouse. 
    Administración de servidores Linux y participación en proyectos para 
    clientes nacionales e internacionales como OXXO, Liverpool y Banorte. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Administrativo | Interim Adecco SA de CV **")
st.write("Ene 2017 - Feb 2018")
st.write(
    """
- ► Experiencia en diseño e implementación de bases de datos, procesos 
    ETL/ELT y pipelines en Python. Desarrollo de Dashboards en Power BI 
    con DAX, conectados a múltiples fuentes (SQL, Data Lake, Excel, API), 
    enfocados en la toma de decisiones a una audiencia diversa, atención de 
    requerimientos. Generación de insights, reportes automatizados, y 
    creación/consumo de datawarehouse.  participación en proyectos para 
    diferentes productos con el objetivo de tener una mejor educación 
    financiera hacia el público interesado y por otra parte el análisis de los 
    mismo con el objetivo de tener diversas campañas para los clientes 
    además de captar nuevos. 
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
