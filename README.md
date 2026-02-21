🚀 CodeAlpha_Project1: CI/CD Pipeline with Azure

🌟Project Overview
This repository contains a fully automated Cloud-Native CI/CD Pipeline built for the CodeAlpha DevOps Internship. The project automates the deployment of a Random Password Generator web application to the cloud, ensuring high availability and seamless updates.

Task 1: Build an automated CI/CD pipeline with Azure and deploy web apps via Azure App Service automatically.

🛠️ Tech Stack
LanguagePython (Flask)
ContainerizationDocker
Source ControlGitHub
CI/CD PlatformGitHub Actions
Cloud HostingMicrosoft Azure App Service
RegistryDocker Hub


📸Project Preview

🌐 Live Application
The application is live and accessible at:
👉 random-password-generator-bmhtekgkesh5esbr.austriaeast-01.azurewebsites.net

⚙️ Pipeline Success
Every commit triggers an automated build and deployment process.

🧬 Pipeline Architecture
The workflow follows these automated steps to ensure code quality and deployment speed:

Checkout Code: Pulls the source from GitHub.

Dockerize: Builds a lightweight Docker image of the Flask app.

Push to Registry: Securely uploads the image to Docker Hub.

Azure Deployment: Triggers Azure App Service to pull the latest image and restart the web server.


🚀 How to Run LocallyWant to test this project on your machine? Follow these steps:

Clone the Repo:
Bash
git clone https://github.com/sakshisalunkhe601/CodeAlpha_Project1.git

Build the Container:
Bashdocker build -t password-gen .

Launch the App:
Bashdocker run -p 5000:5000 password-gen

📁 Repository StructurePlaintextCodeAlpha_Project1/
├── .github/workflows/
│   └── main.yml        # CI/CD Pipeline Definition
├── static/             # CSS and Frontend Assets
├── templates/          # HTML Templates
├── app.py              # Flask Application Logic
├── Dockerfile          # Container Configuration
└── requirements.txt    # Python Dependencies

🎓 Internship Requirements Checklist
[x]Repository Named: CodeAlpha_ProjectName 
[x] Automated CI/CD Pipeline: Built with GitHub Actions 
[x] Live Cloud Deployment: Hosted on Azure  

🤝 Connect with Me
www.linkedin.com/in/sakshi-salunkhe-758005319
