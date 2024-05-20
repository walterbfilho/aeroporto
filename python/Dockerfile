FROM python:3.9

COPY requirements.txt ./

WORKDIR /usr/app/src

RUN pip install -r ./requirements.txt

# 
#RUN pip install streamlit
#RUN pip install pandas
#RUN pip install mysql-connector-python

COPY main.py ./

CMD ["python", "main.py"]