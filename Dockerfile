FROM python:3.13.0-alpine
WORKDIR /app
COPY associativite.py /app
RUN pip3 install --root-user-action=ignore -U numpy
CMD ["python", "associativite.py"]
