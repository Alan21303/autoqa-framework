# **autoqa-framework**

## **🧪 Overview**

**autoqa-framework** is a robust, cross-browser **test automation framework** designed to streamline the testing process for web applications. Utilizing **Python**, **Selenium WebDriver**, and **GitHub Actions**, this framework supports **parallel test execution** across multiple browsers, ensuring efficient and reliable test automation.

---

## **🎯 Objective**

The primary goal of this project is to:

- **Automate Web Application Testing**: Implement end-to-end (**E2E**) tests using Selenium WebDriver.
- **Cross-Browser Compatibility**: Execute tests on multiple browsers (**Chrome** and **Firefox**) to ensure consistent application behavior.
- **Continuous Integration**: Integrate automated tests into a **CI pipeline** using GitHub Actions for seamless execution on code changes.

---

## **⚙️ Features**

- **Cross-Browser Testing**: Supports **Chrome** and **Firefox** browsers.
- **Parallel Test Execution**: Run tests concurrently across different browsers.
- **Headless Mode**: Execute tests without opening browser windows, suitable for **CI environments**.
- **HTML Test Reports**: Generate detailed test reports in **HTML format**.
- **CI/CD Integration**: Automated test execution triggered on code pushes and pull requests to the **main branch**.

---

## **🚀 Getting Started**

### **Prerequisites**

Ensure you have the following installed:

- **Python 3.11**
- **pip** (Python package installer)

### **Installation**

1. Clone the repository:

```bash
git clone https://github.com/Alan21303/autoqa-framework.git
cd autoqa-framework
Install dependencies:

bash
Copy
Edit
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install selenium webdriver-manager pytest-html
Running Tests Locally
To execute tests locally:

bash
Copy
Edit
pytest -m e2e --browser chrome --headless --html=reports/report_chrome.html --self-contained-html
Replace chrome with firefox to run tests on Firefox.

🔄 CI/CD Workflow
The framework utilizes GitHub Actions for Continuous Integration:

Workflow File: .github/workflows/ci.yml

Triggers:

push to the main branch

pull_request targeting the main branch

Workflow Steps
Checkout Repository: Retrieves the latest code.

Set Up Python: Configures Python 3.11 environment.

Install Dependencies: Installs required Python packages.

Install Browsers: Installs Chrome and Firefox browsers.

Run Tests: Executes tests with specified browser in headless mode.

Upload HTML Report: Uploads the generated HTML report as an artifact.

🔧 Modifying the Framework

To customize the framework:

Add New Tests: Create new test scripts in the tests directory.

Update Browser Versions: Modify the browser installation commands in the CI workflow file.

Configure Test Settings: Adjust settings in the pytest.ini file as needed.

📘 Documentation

For detailed documentation:

Selenium WebDriver: https://www.selenium.dev/documentation/en/

GitHub Actions: https://docs.github.com/en/actions

pytest: https://docs.pytest.org/en/stable/
```
