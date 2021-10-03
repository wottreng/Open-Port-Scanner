import os


class fileTools:
    def __init__(self):
        from colorText import colorText
        self.colorText = colorText()

    def writeStrToFile(self, data: str, path: str = os.getcwd(), filename: str = "data.txt", method: str = "w"):
        with open(f"{path}/{filename}", method) as file:
            file.write(f"{data}\n")
        print(f"data writen to: {filename}")

    def writeListToFile(self, data: list, path: str = os.getcwd(), filename: str = "dataList.txt", method: str = "w"):
        with open(f"{path}/{filename}", method) as file:
            for line in data:
                file.write(f"{line}\n")
        print(f"data list written to: {filename}")

    def readFileList(self, path: str = os.getcwd(), filename: str = "dataList.txt"):
        dataList: list = []
        try:
            with open(f"{path}/{filename}", "r") as file:
                data: list = file.readlines()
            for line in data:
                dataList.append(line.strip())
        except:
            self.colorText.printColorText(f"[*] file not found: {filename}", color="red", bold=True)
        return dataList
