FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install jupyter

# Generate Jupyter config
RUN jupyter notebook --generate-config

# Copy your Jupyter config file
COPY jupyter_server_config.py /root/.jupyter/

COPY . .

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser", "--notebook-dir=/app"]

