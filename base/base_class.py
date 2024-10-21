class Base():
    def __init__(self, driver):
        self.driver = driver

    """Метод получения текущего url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Метод проверки кодового слова"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")
