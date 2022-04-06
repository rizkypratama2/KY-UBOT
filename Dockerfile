FROM ramadhani892/ramubot:slim-buster
# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
##

RUN git clone -b KY-UBOT https://github.com/rizkypratama2/KY-UBOT /home/ram-ubot/ \
    && chmod 777 /home/ram-ubot \
    && mkdir /home/ram-ubot/bin/

RUN pip3 install -r https://raw.githubusercontent.com/rizkypratama2/KY-UBOT/KY-UBOT/requirements.txt
 
WORKDIR /home/ram-ubot/

CMD ["python3", "-m", "userbot"]
