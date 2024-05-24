FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /usr/app/src

#COPY streamlit run main.py ./
COPY . .

# Command to run the streamlit app
CMD ["streamlit", "run", "main.py"]