class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод получения текущего url"""

        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        """Метод проверки кодового слова"""

        value_word = word.text
        assert value_word == result
        print("Проверочное слово сошлось")
