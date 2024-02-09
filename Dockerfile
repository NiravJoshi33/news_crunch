# Use an official Python runtime as a parent image
FROM python:3.12.1-bullseye

# Set the image name and tag
LABEL image_name="newscrunch"
LABEL image_tag="latest"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]