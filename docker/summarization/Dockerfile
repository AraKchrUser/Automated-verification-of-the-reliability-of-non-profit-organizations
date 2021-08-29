FROM ubuntu:18.04

COPY dockerpip.txt /.
COPY summarization.py /.
#WORKDIR ./
VOLUME /home/user/src/hackaton_project/Automated-verification-of-the-reliability-of-non-profit-organizations/docker/save_file

RUN apt-get update && apt-get install -y \
	python3.7 \
	python3-pip \
    && pip3 install --upgrade pip
RUN pip3 install -r dockerpip.txt
ENV LANG C.UTF-8
#RUN locale-gen en_US.UTF-8
#RUN update-locale LANG=en_US.UTF-8 LC_MESSAGES=POSIX
#EXPOSE 8888

#CMD ["/bin/bash", "-c", "jupyter notebook --ip='0.0.0.0' --port=8888 --no-browser --allow-root"]
CMD ["/bin/bash"]
