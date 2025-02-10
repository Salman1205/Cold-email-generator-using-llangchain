import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://career55.sapsf.eu/career?career%5fns=job%5flisting&company=systemvent&navBarLevel=JOB%5fSEARCH&rcm%5fsite%5flocale=en%5fUS&career_job_req_id=3481&selected_lang=en_US&jobAlertController_jobAlertId=&jobAlertController_jobAlertName=&browserTimeZone=Asia/Karachi&_s.crb=Uz30xM3gEXzpiB6HIAtAlZFZhZeo3zKyI63OnzR%2fg14%3d")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)