# Automatic Data Extraction and Storage Project

This is my first Data Engineering project, where I have developed a Python application to extract data from various web pages automatically and on a scheduled basis. The extracted data is then stored in a local database.

## Description

This project was created as part of my Data Engineering learning journey. It demonstrates the automation of extracting data from web sources and storing it in a database for later analysis.

## Features

- [x] API created in Django
- [x] Data extraction from web pages using libraries such as Beautiful Soup and Selenium
- [x] Automatic scheduling of extraction tasks using a tool like Cron
- [x] Data storage in a local Postgresql database
- [x]  Error management and retries to ensure extraction reliability

## Project structure

- `BookClub/`: Contains the source code of the extraction application
- `static/`: Stores the chromedriver
- `first_project_data_engineering/`: Contains Django configuration files

## How-to use

1. Clone this repository on your local machine.
2. Navigate to the project directory.
3. Configure the web pages you want to extract in the source code.
4. Install the dependencies used.
5. Set up the scheduling of the extraction tasks using tools such as Cron.
6. Run the extract script to start collecting data.

```bash
git clone https://github.com/GustavoRibeiroSantos/First-Data-analytics-project.git
cd First-Data-analytics-project
python manage.py
```

## Contributions
Contributions are welcome! If you find problems, bugs or have suggestions for improvements, feel free to open issues or send pull requests.

### Have fun exploring and processing the data! 📊🔍
