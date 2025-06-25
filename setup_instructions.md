# Setup Instructions

Follow these steps to set up your environment for the Python Playwright Workshop:

## Prerequisites

- Python 3.7 or newer
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)

## Installation Steps

1. **Install dependencies**  
   Run the following command to install Playwright, pytest, and other requirements:
   ```sh
   pip install -r requirements.txt
   ```

2. **Install browser binaries**  
   After installing Playwright, download the necessary browser binaries:
   ```sh
   python -m playwright install
   ```

3. **(Optional) Jupyter Notebooks**  
   If you want to run the workshop notebooks, ensure you have Jupyter installed:
   ```sh
   pip install notebook
   ```

## Verifying the Installation

To verify that everything is set up correctly, you can run:
```sh
pytest --version
playwright --version
```

If you see the versions printed, you are ready to start the workshop!

---

## Running the Tests

To run the Playwright tests using pytest, simply execute:
```sh
pytest
```
This will automatically discover and run all test files and functions following the `test_*.py` naming convention.