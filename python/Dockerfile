FROM python

# Copy app files and set the working dir
COPY . app
WORKDIR /app

# Install python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["fastapi", "run" , "main.py", "--port", "80"]