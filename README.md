# ARSPASS - Password Generator

## Overview

ARSPASS is a password generator application built using Python and CustomTkinter. It allows users to generate strong passwords with adjustable difficulty levels and lengths. The application features an intuitive graphical user interface (GUI) for ease of use.

## Features

- **Difficulty Levels**: Choose between Easy, Medium, and Hard password complexity.
- **Adjustable Length**: Set password length between 6 and 36 characters.
- **Clipboard Copy**: Click the password field to automatically copy the generated password.
- **Customizable Theme**: The application loads themes from a JSON configuration file.
- **User-Friendly Interface**: Designed with a modern and clean UI using CustomTkinter.

## Installation

### Prerequisites

Ensure you have Python installed on your system (Python 3.x recommended). Additionally, install the required dependencies:

```bash
pip install customtkinter
```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Select the desired difficulty level (Easy, Medium, Hard).
3. Adjust the password length using the slider.
4. Click the **Generate Password** button.
5. Click on the generated password to copy it to the clipboard.

## Configuration

The application uses a `config.json` file for storing settings such as font family and theme.

Example `config.json` file:

```json
{
    "font.family": "Arial",
    "theme": "dark",
    "theme.color": "green"
}
```
