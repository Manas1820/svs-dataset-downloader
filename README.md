# Documentation for the `Downloader` class

The `Downloader` class provides functionality to download and unzip files from a specified URL using Selenium WebDriver.

## Class Methods

### `__init__(self, download_directory="./", headless=True)`
The constructor method initializes the `Downloader` object. It takes two optional parameters:
- `download_directory` (default: "./"): Specifies the directory where the downloaded files will be saved.
- `headless` (default: True): Determines whether the Chrome WebDriver runs in headless mode or not.

### `_wait_for_download(self, timeout=120)`
This private method waits for the download to complete. It checks the Chrome Downloads page and returns the file paths of completed downloads. It takes an optional `timeout` parameter (default: 120 seconds) to specify the maximum time to wait for the download to complete.

### `download_zip_files(self, url)`
This method downloads zip files from a given URL. It performs the following steps:
1. Navigates to the specified URL.
2. Waits for the page to load.
3. Locates and clicks the accept button.
4. Finds the table element containing the files.
5. Iterates through each row of the table and checks if the file has a ".svs" extension.
6. If a ".svs" file is found, locates and clicks the download button.
7. Waits for the download to complete.
8. Logs the downloaded data.
9. Closes the WebDriver.

### `download_specific_project_files(self, txt_file="./")`
This method downloads zip files for specific projects listed in a text file. It takes an optional `txt_file` parameter (default: "./") that specifies the path to the text file containing project names. The method reads the file and iterates through each project name, calling the `download_zip_files` method for each project.

### `unzip_files(directory=None)`
This static method extracts files from tar.gz archives in a specified directory. It takes a required `directory` parameter that specifies the directory where the tar.gz files are located. The method loops through all files in the directory, identifies the ones with the ".tar.gz" extension, checks if the file size is greater than 0, and extracts the contents of the archive using the `tarfile` module.

## Example Usage

```python
# Create an instance of the Downloader class
downloader = Downloader(download_directory="./downloads", headless=True)

# Download zip files for specific projects listed in a text file
downloader.download_specific_project_files(txt_file="./projects.txt")

# Unzip files in the specified directory
downloader.unzip_files(directory="./downloads")
```

Note: Before using this class, make sure you have the required dependencies installed (Selenium WebDriver, ChromeDriver, and tarfile module).

## 👥 Authors

👤 **Manas**
* Github: [@manas1820](https://github.com/manas1820)

👤 **Nishita**
* Github: [@NishitaPatnaik21](https://github.com/NishitaPatnaik21)
