class TextReader:
    def __init__(self, name, language, battery):
        self.name = name
        self._language = language
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def show_info(self):
        print("Reader:", self.name)
        print("Language:", self._language)
        print("Battery:", str(self.__battery) + "%")

    def read_text(self):
        print(self.name + " is reading text.")


class DocumentReader(TextReader):
    def __init__(self, name, language, battery, page_number):
        super().__init__(name, language, battery)
        self.page_number = page_number

    def next_page(self):
        self.page_number = self.page_number + 1
        print(self.name + " moved to page " + str(self.page_number) + ".")

    def read_text(self):
        print(self.name + " is reading page " + str(self.page_number) + " in " + self._language + ".")
        print("Battery remaining: " + str(self.get_battery()) + "%")


class ProductLabelReader(TextReader):
    def __init__(self, name, language, battery, product):
        super().__init__(name, language, battery)
        self.product = product

    def show_product(self):
        print("Product:", self.product)

    def read_text(self):
        print(self.name + " is reading a product label in " + self._language + ".")
        print("Battery remaining: " + str(self.get_battery()) + "%")


document = DocumentReader("Document Reader", "English", 80, 1)
label = ProductLabelReader("Label Reader", "English", 60, "Cereal")

document.show_info()
print()
label.show_info()
print()

readers = [document, label]

for reader in readers:
    reader.read_text()

print()
document.next_page()
label.show_product()
