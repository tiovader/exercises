from scrapper import *
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
import re


def main():
    with open('.config') as config:
        content = config.read()

        user = re.search(r'^user=(.+)$', content, re.MULTILINE).group(1)
        password = re.search(r'^password=(.+)$', content,
                             re.MULTILINE).group(1)

    options = FirefoxOptions()
    # options.add_argument('--headless')

    service = Service(r'C:\bin\geckodriver.exe')
    driver = Firefox(options=options, service=service, service_log_path='nul')

    ExercismScrapper(driver, user=user, password=password, tracks=[
                     'python'], github=True, download=True).run()


if __name__ == '__main__':
    main()
