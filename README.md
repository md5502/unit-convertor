# Unit Converter

This is a Flask-based web application that allows users to convert units of length, weight, and temperature. The application is designed with a simple interface that makes it easy to perform conversions quickly and accurately.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Convert between different units of **Length** (e.g., millimeters, centimeters, meters, kilometers).
- Convert between different units of **Weight** (e.g., milligrams, grams, kilograms, ounces, pounds).
- Convert between different units of **Temperature** (e.g., Celsius, Fahrenheit, Kelvin).
- User-friendly interface with error handling and input validation.
- Responsive design for use on different screen sizes.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/unit-converter.git
    cd unit-converter
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Home Page**: Navigate to the home page and select the type of conversion you want to perform (Length, Weight, Temperature).

2. **Conversion**: Enter the value you want to convert, select the units to convert from and to, and click "Convert". The result will be displayed on the screen.

3. **Navigation**: Use the "Back" button to return to the home page and perform another conversion.

## Project Structure

```plaintext
unit-converter/
├── templates/
│   ├── base.html             # Base template for common structure
│   ├── home.html             # Home page template
│   ├── convert_length.html   # Length conversion template
│   ├── convert_weight.html   # Weight conversion template
│   └── convert_temp.html     # Temperature conversion template
├── static/
│   ├── css/                  # Stylesheets (optional)
│   └── js/                   # JavaScript files (optional)
├── utils.py                  # Utility functions for conversion logic
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
└── README.md                 # This README file
