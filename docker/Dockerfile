FROM ubuntu:18.04

COPY pip_docker /pip_docker
WORKDIR ./
VOLUME /save_file

RUN apt-get update && apt-get install -y \
	python3.6 \
	python3-pip
RUN pip3 install -r /pip_docker/dockerpip.txt

EXPOSE 8888

CMD ["/bin/bash", "-c", "jupyter notebook --ip='0.0.0.0' --port=8888 --no-browser --allow-root"]
