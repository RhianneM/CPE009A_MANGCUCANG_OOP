from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        """
        Reads the content of a text file and prints it to the console.
        """
        try:
            with open(filepath, "r") as read_file:
                data = read_file.read()
                print(data)
                return data
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")

    def write(self, filepath, data):
        """
        Writes (overwrites) the provided string data to a text file.
        """
        with open(filepath, "w") as write_file:
            write_file.write(str(data))
            print(f"Data successfully written to {filepath}")
