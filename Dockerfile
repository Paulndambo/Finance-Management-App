FROM python
WORKDIR /app/
COPY . /app/

RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]