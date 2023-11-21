
FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirement.txt
RUN pip install --trusted-host pypi.python.org -r requirement.txt
RUN pip install --trusted-host pypi.python.org -r requirement.txt
EXPOSE 5000
CMD ["python3" , "my_flask.py"]
