FROM python:3.8-slim
EXPOSE 8000
COPY ./requirements.txt /requirements.txt
COPY . /counting
WORKDIR /counting

RUN apt-get update && apt-get install -y python3-opencv
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    /py/bin/pip install torch==1.12.0 torchvision==0.13.0 torchaudio===0.12.0 -f https://download.pytorch.org/whl/cu116/torch_stable.html && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER django-user

# Gunicorn as app server
# CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 CowdCountingSystem.wsgi
