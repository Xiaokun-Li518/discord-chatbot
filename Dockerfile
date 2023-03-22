FROM python:3

WORKDIR /discord_bot

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD python -u ./run.py