FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY ./code/. .
RUN pip3 install pyTelegramBotApi -r requirements.txt

ENTRYPOINT ["python"]
CMD ["Bot.py"]