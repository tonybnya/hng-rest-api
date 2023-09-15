# HNGx REST API

Welcome to the HNGx REST API! This API allows you to perform simple CRUD operations on a Person Resource.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Prerequisites

Before you get started, ensure you have the following prerequisites:

- Python 3.8 or higher installed on your system.
- Virtual environment (optional but recommended).

## Installation

Follow these steps to install and run the Awesome API:

1. Clone this repository to your local machine:
   
   ```bash
   git clone https://github.com/tonybnya/hng-rest-api.git
   cd hng-rest-api
   ```

2. Create and activate a virtual environment (recommended):
   
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   
   - On Windows
     
     `venv\Scripts\activate`
   
   - On Mac & Linux
     
     `source venv/bin/activate`

4. Install the required dependencies
   
   `pip install -r requirements.txt`

## Usage

To run the API locally, use the following command:

`python api.py`

There is also a `tests.py` file to test locally if everything works properly.

Your API will be accessible at `http://localhost:5000/`. You can then make HTTP requests to the provided endpoints.
