# testing-wikipedia

## Introduction

This project is a Python-based automated testing framework designed to facilitate UI testing for web applications.
Leveraging the Selenium, it provides a suite of tests across various pages of a web application to ensure
functionality, usability, and reliability.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [License](#license)

## Installation

To install the required dependencies for this project, you'll need Python installed on your system.
After cloning the repository, navigate to the project directory and run:

```pip install -r requirements.txt```


This command will install all necessary Python packages listed in `requirements.txt`.

## Usage

To run the tests, navigate to `wikipedia` directory and execute:

```pytest tests.py```


This will run all tests defined in the `tests.py` file.

## Features

- Page Object Model (POM) design pattern for better maintainability.
- Support for multiple web browsers.
- Configurable test suites.

## Dependencies

- Python 3.11
- Selenium 4.12.0
- pytest 7.4.2
- pytest-html 4.1.1

## Configuration

Edit the `pytest.ini` file for project-specific configurations, such as log format and logging level.

In `conftest.py`, within the `driver()` fixture, you can set your preferred browser in the `get_driver()` function.
You can choose between Firefox and Google Chrome by typing `"firefox"` or `"chrome"`.

In `conftest.py`, you can change the value of the `amount` argument to adjust the number of terms that will be drawn
for the `choose_search_terms()` function.

To generate an HTML report of the test results, you can use the `pytest-html` plugin.
Append the following command `--html=<report_name>.html` at the end of your pytest command.

## Examples

Type `pytest tests.py -k '<test_name>'` to run specific test.

For example `pytest tests.py -k 'test_wikipedia_search'`


## License

This project is licensed under the MIT License.
