FROM python:3.6
LABEL maintainer="@brentclaster"
COPY . /simplepy
WORKDIR /simplepy
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["simplepy/app.py"]
