# 1. Start with a Linux system that has Python 3.9 installed
FROM python:3.9-slim

# 2. Create a folder inside the box called /app
WORKDIR /app

# 3. Copy our code from your computer into the box
COPY . .

# 4. Install the library we need (FastAPI and Uvicorn)
# (In a real project, we use requirements.txt, but this is easier for now)
RUN pip install fastapi uvicorn

# 5. Tell the box to open port 8000
EXPOSE 8000

# 6. The command to run when the box starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]