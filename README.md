# iCheckIn

Automation script for checking into [iZone](https://izone.sunway.edu.my/) classes.

## Built With

### Languages

- [![Python](https://img.shields.io/badge/Python-f7c93e?style=for-the-badge&logo=python&logoColor=#366c9c)](https://www.python.org/)

### Modules

- [Selenium](https://www.selenium.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Getting Started

### Prerequisites

1. Install [Google Chrome](https://www.google.com/chrome/)


2. Install a [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable) that is compatible with your Chrome browser, then extract the ZIP file and copy the `chromedriver.exe` file to your `/drivers` directory

3. Update your py launcher to the latest version

```
py -m ensurepip --upgrade
```

4. Update your pip package installer to the latest version

```
py -m pip install --upgrade pip
```

### Setup

1. Install `python-dotenv` and `selenium` modules

```
pip install python-dotenv
pip install selenium
```

2. Create a `.env` file with the following contents

```
STUDENT_ID=<YOUR STUDENT ID HERE>
PASSWORD=<YOUR IZONE PASSWORD HERE>
```

3. Run the script and pass the iCheckIn code as an argument. Example: iCheckIn code = 12345

```
python main.py 12345
```

## Tips

Create a simple terminal script and run it from your desktop to shave down even more time!

### Powershell

```
cd "path\to\iCheckIn" # Change this to the path of your iCheckIn directory

$code = Read-Host -Prompt "Enter iCheckIn code"

Write-Host "Checking in with code $code..."

python main.py $code
```

### Bash

```
#!/bin/bash

cd /path/to/iCheckIn # Change this to the path of your iCheckIn directory

read -p "Enter iCheckIn code: " code

echo "Checking in with code $code..."

python3 main.py "$code"
```

## Issues

View the [open issues](https://github.com/ChiefWoods/iCheckIn/issues) for a full list of proposed features and known bugs.

## Acknowledgements

Credits to Rachel Lim Wei Hui for the original script.

## Contact

[chii.yuen@hotmail.com](mailto:chii.yuen@hotmail.com)