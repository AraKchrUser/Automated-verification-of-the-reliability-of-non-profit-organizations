FROM ubuntu:18.04

COPY text.txt /.
COPY dockerpip.txt /.
COPY sentimentalanls.py /.

# Расскоментрируй!
#COPY /models_deeppavlov/elmo_ru-twitter_2013-01_2018-04_600k_steps.tar.gz /.
#COPY /models_deeppavlov/rusentiment_v10.tar.gz /.

VOLUME /home/user/src/hackaton_project/Automated-verification-of-the-reliability-of-non-profit-organizations/docker/save_file

RUN apt-get update && apt-get install -y \
	python3.7 \
	python3-pip \
    && pip3 install --upgrade pip
#    && apt-get -qq --no-install-recommends install \
#        wget \
#        libuv1-dev \
#        libcurl4-openssl-dev \
#    && rm -r /var/lib/apt/lists/*
#    && wget --no-check-certificate
RUN pip3 install -r dockerpip.txt
ENV LANG C.UTF-8



#RUN in docker:
#CMD ["/bin/bash", "python3 -m deeppavlov install rusentiment_elmo_twitter_cnn"]
#CMD ["/bin/bash", "-c", "python3", "sentimentalanls.py"]

CMD ["/bin/bash"]
#EXPOSE 5000
#
#CMD ["/bin/bash", "-c", "jupyter notebook --ip='0.0.0.0' --port=8888 --no-browser --allow-root"]
