# DevSecOps CI/CD Security Pipeline
   
   ![Security Pipeline](https://github.com/0xZeteo/devsecops-pipeline-project/actions/workflows/security-pipeline.yml/badge.svg)
   ![GitHub](https://img.shields.io/github/license/0xZeteo/devsecops-pipeline-project)
   ![GitHub last commit](https://img.shields.io/github/last-commit/0xZeteo/devsecops-pipeline-project)
   
A fully automated security pipeline that scans code for vulnerabilities, secrets, infrastructure misconfigurations, and container vulnerabilities before deployment.

## Overview

This project implements a multi-stage security pipeline using GitHub Actions that automatically runs on every code push. It demonstrates the "shift left" security approach by catching vulnerabilities early in the development lifecycle.

## Security Tools Integrated

### 1. **Gitleaks** - Secret Detection
- Scans repository history for accidentally committed secrets
- Detects API keys, tokens, passwords, and credentials
- Prevents credential leaks before they reach production

### 2. **Semgrep** - Static Application Security Testing (SAST)
- Analyzes Python code for security vulnerabilities
- Detects OWASP Top 10 issues (SQL injection, XSS, insecure configurations)
- Uses 1000+ community security rules

### 3. **Checkov** - Infrastructure as Code (IaC) Scanning
- Scans Terraform configurations for cloud misconfigurations
- Validates AWS security best practices
- Prevents deployment of insecure infrastructure

### 4. **Trivy** - Container Vulnerability Scanning
- Scans Docker images for known CVEs
- Detects vulnerabilities in base images and dependencies
- Identifies HIGH and CRITICAL severity issues

## Pipeline Architecture
Push/PR → Gitleaks → Semgrep → Checkov → Trivy → ✅ Deploy
   ↓           ↓         ↓          ↓
Secrets    Code Vuln   IaC Issues Container CVEs

Each stage must pass before the next runs. If any scanner finds issues, the pipeline fails and blocks deployment.

## How It Works

The pipeline is defined in `.github/workflows/security-pipeline.yml` and runs automatically when:
- Code is pushed to the `main` branch
- A pull request is opened against `main`

### Pipeline Stages

1. **secrets-scan**: Scans for leaked credentials using Gitleaks
2. **sast-scan**: Performs static code analysis using Semgrep
3. **iac-scan**: Validates infrastructure configurations using Checkov
4. **container-scan**: Scans Docker images for vulnerabilities using Trivy

## Key Features

- ✅ **Automated Security**: Runs on every code change
- ✅ **Multi-Layer Defense**: 4 different security scanners
- ✅ **Shift Left Approach**: Catches issues before deployment
- ✅ **Zero Manual Intervention**: Fully automated workflow
- ✅ **Production Ready**: Uses industry-standard tools

## Real Security Findings

During development, this pipeline caught:

- **Flask Security Issue**: Detected insecure host binding (0.0.0.0) that could expose the application publicly
- **S3 Misconfigurations**: Identified 7 AWS S3 bucket security issues including missing encryption, logging, and versioning
- **Container CVEs**: Found 3 HIGH severity vulnerabilities in Python dependencies

## Technologies Used

- **GitHub Actions** - CI/CD automation platform
- **Docker** - Containerization
- **Python/Flask** - Sample application
- **Terraform** - Infrastructure as Code
- **Security Tools**: Gitleaks, Semgrep, Checkov, Trivy

## Getting Started

### Prerequisites
- GitHub account
- Git installed locally
- Docker (optional, for local testing)

### Setup

1. Fork this repository
2. Clone to your local machine:
```bash
   git clone https://github.com/YOUR-USERNAME/devsecops-pipeline-project.git
   cd devsecops-pipeline-project
```
3. Make changes and push - the pipeline runs automatically!

## Viewing Pipeline Results

1. Go to the **Actions** tab in your GitHub repository
2. Click on any workflow run to see detailed results
3. Each security tool provides a detailed report of findings

## What I Learned

- How to integrate multiple security tools into a CI/CD pipeline
- The importance of automated security scanning in modern DevOps
- How to configure security tools to balance security and development velocity
- Real-world AWS security misconfigurations and how to prevent them
- Container security best practices

## Future Enhancements

- [ ] Add DAST (Dynamic Application Security Testing)
- [ ] Integrate with Slack for security notifications
- [ ] Add automated GitHub issue creation for findings
- [ ] Implement security scoring dashboard
- [ ] Add SCA (Software Composition Analysis)

## Author

**ZeteoSec** 
[Portfolio](https://zeteosec.com) | [GitHub](https://github.com/0xZeteo)

## License

This project is open source and available for educational purposes.