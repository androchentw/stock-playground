FROM python:3.12-slim

# prevents pyc files from being copied to the container
ENV PYTHONDONTWRITEBYTECODE 1

# Ensures that python output is logged in the container's terminal
ENV PYTHONUNBUFFERED 1

ARG HOME=/code

WORKDIR $HOME

COPY ./requirements.txt $HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . $HOME

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
