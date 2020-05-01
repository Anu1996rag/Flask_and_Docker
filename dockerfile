FROM continuumio/anaconda3:4.4.0
COPY ./Flask_demo /usr/local/python
EXPOSE 5000
WORKDIR /usr/local/python
RUN pip install -r requirements.txt
CMD python flask_predict.py


