FROM pypy:latest
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
CMD python inventory.py