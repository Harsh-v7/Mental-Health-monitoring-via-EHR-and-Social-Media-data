# Mental-Health-monitoring-via-EHR-and-Social-Media-data

**Technologies:** AWS (EC2, S3, Lambda, RDS), Python, React, NLP  

---

## Project Overview

This project is a full-stack mental health monitoring platform that integrates patient Electronic Health Records (EHR) with real-time sentiment analysis of Twitter data to detect early signs of anxiety and depression. The system leverages cloud infrastructure and advanced NLP techniques to provide actionable insights for healthcare providers.

---

## Features

- **Integrated Data Sources:** Combines structured patient health records with unstructured social media sentiment for a comprehensive mental health overview.
- **Real-time Twitter Sentiment Analysis:** Utilizes NLP to analyze live Twitter streams, detecting emotional trends related to anxiety and depression.
- **Cloud-Hosted Solution:** Deployed on AWS using EC2 for compute, S3 for secure storage, Lambda for serverless processing, and RDS for relational database management.
- **Security & Compliance:** Implements secure IAM access controls and encrypted storage to adhere to HIPAA compliance standards.
- **Performance Optimizations:** Enhanced system responsiveness by optimizing SQL queries and implementing AWS auto-scaling features.
- **Data Visualization:** Interactive Python dashboards provide clear visual insights extracted from combined data sources.

---

## Architecture

1. **Frontend:** React application for user interaction and visualization.
2. **Backend:** Python-based APIs for data processing and integration.
3. **Data Storage:** AWS RDS stores patient EHR data securely.
4. **Data Processing:** AWS Lambda functions handle Twitter data ingestion and sentiment analysis.
5. **Storage:** AWS S3 stores logs, processed data, and backups.
6. **Security:** AWS IAM roles and policies ensure secure access control.

---

## Getting Started

### Prerequisites

- AWS account with necessary permissions (EC2, S3, Lambda, RDS, IAM)
- Python 3.x
- Node.js and npm
- Twitter API access credentials

### Installation

1. Clone the repo:  
   ```bash
   git clone https://github.com/yourusername/mental-health-monitoring-system.git
   cd mental-health-monitoring-system
