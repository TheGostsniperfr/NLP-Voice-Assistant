# NLP Voice Assistant

## Overview

This is the project of our Natural Language Processing class at Politechnika Krakowska.

Our project is an NLP (Natural Language Processing) voice assistant with a GUI made in Python.
This voice assistant can recognize spoken commands, process natural language inputs, and respond accordingly.
The GUI provides an intuitive interface for users to interact with the assistant, enhancing the overall user experience.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.11 < .X version
- `pip` (Python package installer)

## Setup

Follow these steps to set up your environment and install the required packages:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/TheGostsniperfr/NLP-Voice-Assistant.git
    cd NLP-Voice-Assistant
    ```

2. **Create a Virtual Environment**:

    *The project might work only on windows because we haven't tested it on other OS [[AppOpener](https://pypi.org/project/appopener/) could be available only on Windows].*

    - On **Windows**:
      ```bash
      python -m venv myenv
      myenv\Scripts\activate
      ```
    - On **macOS/Linux**:
      ```bash
      python3 -m venv myenv
      source myenv/bin/activate
      ```

3. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

After setting up the environment, you can use the project as follows:

1. **Activate the Virtual Environment**:
    - On **Windows**:
      ```bash
      myenv\Scripts\activate
      ```
    - On **macOS/Linux**:
      ```bash
      source myenv/bin/activate
      ```

2. **Run the Project**:
    ```bash
    python main.py
    ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
