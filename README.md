# Fintekera-WebScraping-Project-Note
# Scrape-pipeline
# Fintekera Scraping Project

## Overview

This is a private repository for the Fintekera project. It contains code and resources developed exclusively for Fintekera and is subject to a Non-Disclosure Agreement (NDA). Only authorized team members and 
individuals under the NDA should access and use the contents of this repository.

**Confidentiality**: This repository and its contents are confidential. By accessing this repository, you agree to abide by the terms of the NDA signed with [Fintekera and to protect the confidentiality of 
the information and code within.

## Purpose

Fintekera Scraping Project is a Python based code that scrapes multiple job listing and salary database websites to aggregate salary information of different jobs across the different sites. This data is 
collected, processed, and analyzed to provide insights into salary trends, job market conditions, and other relevant metrics. 

## Getting Started

This section should be reserved for instructions and information on how to get started with the project, if applicable. However, due to the confidential nature of the project and NDA, we cannot provide public 
instructions in this README.

## Functionalities
All the codes are in Python coding language and the pipeline is a Python file that is run in GitHub Actions to obtain the required data files.
The codes follow a series a step to scrape a website: 

1.Setting the environment: A virtual web browser is created using Chrome driver to scrape data from the job website. The driver sets parameters based on the website being scraped. 

2.Scraping the data: After the virtual browser is set, the code starts scraping the job titles and salary based on the website tags. Each website has a different tag name for the element to extract, therefore each website code will have a different structure. 

3.Data Organizing: The data scraped from the website is then converted into a data frame based on the client's requirements. The data is cleaned by removing the unknown values and characters and the final data frame is exported in a CSV or Excel format. 

Each website has a Python file for scraping which is called in the pipeline code to run all of them parallelly. 

## Architecture
The system architecture of our data scraping tool involves a carefully chosen a set of technologies and components to ensure efficiency, scalability, and maintainability.
Technologies Used: Our project leverages a combination of powerful technologies to achieve its objectives. Here is a breakdown of the key technologies used: 

### Python: 

We chose python as the primary programming language for its popularity and versatility in web scraping. Python provides a rich ecosystem of libraries and frameworks, making it well-suited for our data extraction needs. 

### BeautifulSoup: 

BeautifulSoup is employed for HTML parsing allowing us to navigate and search HTML and XML documents effortlessly. This library enhances the extraction of data from various website structures. 

### Selenium: 

Selenium is utilized for web automation, enabling us to interact with websites that require user actions. This automation is crucial for efficient and uninterrupted data scraping. 

### MySQL: 

MySQL caters to our data storage and retrieval requirements. Custom scripts have been developed to ensure seamless integration and interaction with these database systems. 

## Adecco.py Documentation

## Overview

`Adecco.py` is a Python script that scrapes job information from the Adecco website and saves it to a CSV file.

## Usage

1. Modify the `num_pages` parameter in the `scrape_jobs` method to control the number of pages to scrape.
2. Run the script to initiate the scraping process and save the data to a CSV file.

## Dependencies

- Selenium
- BeautifulSoup
- Pandas

## General Guidelines for Similar Scripts
For other scraping scripts in the project, follow these general guidelines:

### Parameter Configuration:

Locate the method responsible for scraping (e.g., scrape_jobs).
Adjust any parameters specific to the website or scraping requirements.
### Execution:

Run the script to initiate the scraping process.
Data will be saved automatically to an appropriate file format (e.g., CSV, Excel).
### Dependencies:

Ensure the necessary dependencies (Selenium, BeautifulSoup, Pandas) are installed.

Notes:
Scripts follow a similar structure and logic, ensuring consistency across different scrapers.
Always review specific comments within each script for any site-specific details or adjustments.

## Coding Guidelines
To maintain consistency and readability, we follow these coding guidelines:

Use consistent indentation (spaces or tabs).
Write descriptive variable and function names.
Keep lines within a reasonable length (usually 79-80 characters).
Include comments where necessary to explain complex sections.
Follow the PEP 8 style guide.

## Codebase Structure
Our project follows a structured organization:

src/: Primary files for the project.
requirements.txt: Lists necessary dependencies.
main.py: Entry point of the application.

## Issues and Concerns
Concerns include dynamic scraping challenges, anti-scraping mechanisms, data integrity, utility of data, and the possibility of website changes.


## License

This project is protected under a Non-Disclosure Agreement (NDA) between UTD's BUAN 6390 Group 1 and Fintekera. Unauthorized use, distribution, or sharing of this code and its associated resources is prohibited.

## Contact

For questions, support, or assistance related to this project, please contact:

## Confidentiality Notice

Please remember to handle all project-related information and code in this repository with the utmost confidentiality and in accordance with the NDA. Unauthorized access or sharing of this information may 
have legal consequences.
