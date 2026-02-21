CodeAlpha_Project1: CI/CD Pipeline using Azure

Project Overview
This project demonstrates a fully automated CI/CD Pipeline designed to build, containerize, and deploy a Flask-based web application to the cloud. The goal was to implement a "Cloud Native" workflow that ensures every code change is automatically tested, packaged, and updated on the live server.


Technical Stack

Application: Python (Flask)

Containerization: Docker 

CI/CD Platform: GitHub Actions 

Registry: Docker Hub (Transitioning to Azure Container Registry) 

Cloud Provider: Azure App Service 

CI/CD Workflow

The pipeline is defined in .github/workflows/main.yml and consists of the following automated steps:
Code Checkout: Pulls the latest code from the main branch.
Docker Login: Authenticates with the container registry using secure secrets.
Build & Push: Builds a Docker image of the application and pushes it to the registry.
Azure Deployment: Automatically triggers a deployment to Azure App Service, pulling the latest container image to update the live website.

How to Run Locally:

You can view the live application here: random-password-generator-bmhtekgkesh5esbr.austriaeast-01.azurewebsites.net

Clone the repository:
Bash
git clone https://github.com/sakshisalunkhe601/CodeAlpha_Project1.git

Build the Docker image:
Bash
docker build -t password-gen .

Run the container:
Bash
docker run -p 5000:5000 password-gen

Internship Task Requirements

According to the CodeAlpha internship instructions:
Task 1: Build an automated CI/CD pipeline with Azure.
Status: Successfully implemented and monitored for smooth execution.
Repository Name: CodeAlpha_Project1.
