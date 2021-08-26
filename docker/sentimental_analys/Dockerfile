FROM ubuntu:18.04

COPY text.txt /.
COPY dockerpip.txt /.
#WORKDIR ./
VOLUME /home/user/src/hackaton_project/Automated-verification-of-the-reliability-of-non-profit-organizations/docker/save_file

RUN apt-get update && apt-get install -y \
	python3.6 \
	python3-pip \
    && pip3 install --upgrade pip
RUN pip3 install -r dockerpip.txt

COPY sentimentalanls.py /.
CMD ["/bin/bash", "python -m deeppavlov install rusentiment_elmo_twitter_cnn"]
#Выполнить в виртуальной машине
#CMD ["/bin/bash", "-c", "python3", "sentimentalanls.py"]
CMD ["/bin/bash"]
#EXPOSE 8888
#
#CMD ["/bin/bash", "-c", "jupyter notebook --ip='0.0.0.0' --port=8888 --no-browser --allow-root"]
