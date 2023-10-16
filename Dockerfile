FROM python:3.11.5

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application runs on
EXPOSE 9213
# Define the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6789"]