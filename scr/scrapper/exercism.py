import os
from time import sleep
from typing import Iterable, Sequence
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExercismScrapper:
    def __init__(self, driver: WebDriver, *, user: str, password: str, tracks: list[str], by_github=False) -> None:
        self.driver = driver
        self.wait_until = WebDriverWait(driver, 10).until
        self.user = user
        self.password = password
        self.by_github = by_github
        self.CLI_commands = []
        if isinstance(tracks, (Iterable, Sequence)):
            self.tracks = [*tracks]
        else:
            raise ValueError('tracks must be a iterable/sequence.')

        self.run()

    def __login(self):
        self.driver.get('https://exercism.org/users/sign_in')
        if self.by_github:
            self.driver.find_element(By.CLASS_NAME, 'github-btn').click()
            login = 'login_field'
            password = 'password'
            button = '/html/body/div[3]/main/div/div[3]/form/div/input[12]'
        else:
            login = 'user_email'
            password = 'user_password'
            button = '/html/body/div[1]/section[1]/div/form[2]/button'

        self.wait_until(
            EC.presence_of_element_located(
                (By.ID, login)
            )
        ).send_keys(self.user)

        self.driver.find_element(By.ID, password).send_keys(self.password)
        self.driver.find_element(By.XPATH, button).click()

        self.wait_until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'content')
            )
        )

    def scrap_exercises(self, track):
        url = f'https://exercism.org/tracks/{track}/exercises?status=completed'
        self.driver.get(url)

        elements = self.driver.find_elements(By.CLASS_NAME, '--info')
        homepage = self.driver.current_window_handle
        sleep(5)

        for element in elements:
            loc = element.location
            self.driver.execute_script(
                f'window.scrollTo({loc["x"]}, {loc["y"]});')
            self.driver.execute_script('window.scrollBy(0, -120);')

            ActionChains(self.driver).key_down(Keys.CONTROL).click(element) \
                .key_up(Keys.CONTROL).perform()

            self.driver.switch_to.window(self.driver.window_handles[-1])
            exercise_cli = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'c-copy-text-to-clipboard'))
            ).text
            self.CLI_commands.append(exercise_cli)
            self.driver.close()
            self.driver.switch_to.window(homepage)

    def run(self):
        self.__login()

        for track in self.tracks:
            self.scrap_exercises(track)

        self.driver.quit()

        for command in self.CLI_commands:
            os.system(command)
