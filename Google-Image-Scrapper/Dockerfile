FROM docker.io/condaforge/mambaforge@sha256:a119fe148b8a276397cb7423797f8ee82670e64b071dc39c918b6c3513bd0174

RUN bin/bash
EXPOSE 5000
## Creating the new conda environment with the desired packages using mamba
WORKDIR /opt
COPY environment.yml .
RUN mamba env create -f environment.yml
RUN echo "conda activate amazing_python_script" >> ~/.bashrc

# COPYING THE RELEVANT FILES
COPY static /opt/static
COPY templates /opt/templates
COPY main.py /opt/main.py
COPY scrapper.py /opt/scrapper.py

# Starting the server
ENTRYPOINT ["/opt/conda/envs/amazing_python_script/bin/python","-u", "/opt/main.py"]