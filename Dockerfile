FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR NZTA
COPY requirements.txt /NZTA/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /NZTA/
CMD ["python", "manage.py", "runserver"]