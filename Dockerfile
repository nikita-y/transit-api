#   Download layer
#   Dowloads and unzips files from njtransit.com
#   This part is less likly to change
FROM ubuntu:latest as download
RUN  apt-get update \
    && apt-get install -y zip unzip wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/data
RUN wget -q https://www.njtransit.com/bus_data.zip
RUN wget -q https://www.njtransit.com/rail_data.zip

RUN mkdir bus && unzip bus_data.zip -d bus
RUN mkdir rail && unzip rail_data.zip -d rail

#   Runtaime layer
#   installs pip packages and
#   Copies files from download layer and project files
FROM python:3.8 as runtime

WORKDIR /usr/app

COPY --from=download /usr/data/bus data/bus/
COPY --from=download /usr/data/rail data/rail/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

ENTRYPOINT ["python"]
CMD ["/usr/app/app.py"]
