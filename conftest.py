from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true",
                     help="Run browser in headless mode")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("reports", today.strftime("%Y-%m-%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y-%m-%d_%H-%M-%S')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Test Report"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  # Use headless mode in CI
    options.add_argument("--no-sandbox")  # Needed in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    options.add_argument("--window-size=1920,1080")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
