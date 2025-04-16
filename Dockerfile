FROM python:3.12-slim

WORKDIR /cme_tool

COPY . /cme_tool

RUN pip install -r requirements.txt

EXPOSE 8501

ARG API_KEY
ENV API_KEY=$API_KEY

CMD ["streamlit", "run", "src/streamlit_app.py"]
