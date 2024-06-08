FROM python:3

COPY iphinter.py .

CMD [ "python3", "iphinter.py" ]
