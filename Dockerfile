FROM rizkypratama2/ky-ubot:alpha

RUN git clone -b KY-UBOT https://github.com/rizkypratama2/KY-UBOT /root/userbot
WORKDIR /root/userbot

CMD ["python3", "-m", "userbot"]
