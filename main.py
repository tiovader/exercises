from scr import *
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service


def main():
    vars = EnviromentVariables()

    options = FirefoxOptions()
    options.add_argument('--headless')

    # O geckodriver tem que está localizado nesse pathing.
    # Caso contrário mudar o pathing do Service!
    service = Service(r'C:\bin\geckodriver.exe', log_path='nul')
    driver = Firefox(options=options, service=service)

    kwargs = {
        # Esses valores devem estar no .config
        **vars,
        # Tracks de onde o script vai pegar os códigos
        # Tem que ser uma lista, set ou tupla
        'tracks': [...],
        # O login é feito por meio do github?
        'by_github': ...
    }

    ExercismScrapper(driver, **kwargs)


if __name__ == '__main__':
    main()
