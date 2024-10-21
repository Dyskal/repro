FROM python:3.13.0-alpine
WORKDIR /app
COPY associativite.py /app
RUN pip3 install --root-user-action=ignore -U numpy
ENTRYPOINT ["python", "associativite.py"]
CMD ["--start", "0.0", "--end", "5.0", "--step", "0.1"]

