FROM ramadhani892/ramagans:slim-buster

RUN git clone -b KY-UBOT https://github.com/rizkypratama2/KY-UBOT /home/kyubot/
WORKDIR /home/kyubot/

CMD ["python3", "-m", "userbot"]

