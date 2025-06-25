# pycontest

A collection of exercises for [Pycon 2019](https://us.pycon.org/2019/) 
tutorial [To trust or to test?: Automated testing of scientific projects with pytest](https://us.pycon.org/2019/schedule/presentation/82/)

- You can find slides from the presentation [here](https://djarecka.github.io/pycontest/presentation/#1)
- You can find full video from the PyCon 2019 conference [here](https://pyvideo.org/pycon-us-2019/to-trust-or-to-test-automated-testing-of-scientific-projects-with-pytest.html)

Dependencies:
-------------

Tutorial requires Python 3.6, Matplotlib 3.0, Scipy, Numpy, Pytest and Hypothesis.
To create example animations you may need ffmpeg or mencoder packages. 

## Python Requirements:

[![Python](https://img.shields.io/badge/python-3.6%2B-blue?logo=python&logoColor=white)](https://www.python.org/)

### 1. Install ffmpeg and optionally Allure for checking out reports

**macOS**

[![Homebrew](https://img.shields.io/badge/Homebrew-%20Install-000?logo=homebrew&logoColor=white)](https://brew.sh/)

```bash
brew install ffmpeg
# Allure - optional (shown on github pages)
brew install allure
```

**Windows**

[![Chocolatey](https://img.shields.io/badge/Chocolatey-%20Install-blue?logo=chocolatey&logoColor=white)](https://chocolatey.org/install)
[![Scoop](https://img.shields.io/badge/Scoop-%20Install-blue?logo=windows&logoColor=white)](https://scoop.sh/)

```powershell
choco install ffmpeg
# Allure - optional (shown on github pages)
scoop install allure
```
- https://allurereport.org/docs/install/

### 2. Create and activate a virtual environment

**macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```powershell
python -m venv venv
.\venv\Scripts\activate.ps1
```

- You should see (venv) in your terminal, indicating you are in the virtual environment.

### 3. Install Python dependencies

**macOS**

```bash
pip install -r mac-requirements.txt
```

**Windows**

```powershell
pip install -r win-requirements.txt
```

### 4. Try running the tests (before solving)

**macOS**

```bash
pytest -v tests/
```

**Windows**

```powershell
pytest -v .\tests
```

### 5. Work through the problems alongside the presentation

### 6. Generate Allure Reports

- You can also generate a visual report of this baseline using Allure

**macOS**

```bash
pytest tests/ --alluredir allure-results
```

**Windows**

```powershell
pytest .\tests --alluredir allure-results
```

## 💡 Key Takeaways

Troubleshooting:
----------------
- to install the tutorial example code:
  ```
  $ pip install .
  ```

- to run the tutorial example code without installation:
  ```
  $ python -m pycontest.simulation
  ```

- in case you have more than one python distribution you may need to specify python version to pytest:
  ```
  $ python3 -m pytest tests                      
  ```
