import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import tarfile
import traceback
import logging

logger = logging.getLogger(__name__)


class Downloader:

    def __init__(self, download_directory="./", headless=True):
        self.options = Options()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--headless")

        self.prefs = {"profile.default_content_setting_values.automatic_downloads": 1}
        self.options.add_experimental_option("prefs", self.prefs)

        self.driver = webdriver.Chrome(options=self.options)

        self.download_directory = download_directory

    def _wait_for_download(self, timeout=120):
        if not self.driver.current_url.startswith("chrome://downloads"):
            self.driver.get("chrome://downloads/")
        return self.driver.execute_script(
            """
            var elements = document.querySelector('downloads-manager')
            .shadowRoot.querySelector('#downloadsList')
            .items
            if (elements.every(e => e.state === 'COMPLETE'))
            return elements.map(e => e.filePath || e.file_path || e.fileUrl || e.file_url);
            """
        )

    def download_zip_files(self, url):
        logger.info(f"Fetching data for : {url}")

        self.driver.get(url)
        time.sleep(7)

        accept_button = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[4]/div/div/div/div[2]/button"
        )

        accept_button.click()
        time.sleep(2)
        table = self.driver.find_element(
            by=By.XPATH, value='//*[@id="biospecimen"]/div/div/div[3]/div/table/tbody'
        )
        for row in table.find_elements("xpath", ".//tr"):
            for td in row.find_elements("xpath", ".//td[1]/span"):
                val = td.text

                if ".svs" in val:
                    try:
                        download_button = row.find_elements(
                            "xpath", ".//td[4]/div/span[2]/button"
                        )

                        WebDriverWait(self.driver, 120).until(
                            download_button[0].click()
                        )
                        time.sleep(1200)

                    except Exception as e:
                        traceback.print_exc()
                        logger.error(e)
                        pass

        time.sleep(180)
        logger.info(f"Downloaded data from : {url} \n")

        self.driver.close()

    def download_specific_project_files(self, txt_file="./"):
        with open(txt_file, "r") as project_names:
            result = project_names.readlines()

        counter = 0

        for text in result:
            self.download_zip_files(
                f"https://portal.gdc.cancer.gov/cases/{text.strip()}"
            )
            counter += 1

        logger.log(f"Downloaded {counter} files")

    @staticmethod
    def unzip_files(directory=None):
        if directory is None:
            Exception("Please provide a directory")

        logger.info(f"Unzipping files in {directory}")
        count = 0

        # Loop through all files in the directory

        for file_name in os.listdir(directory):
            if file_name.endswith(".tar.gz"):
                file_path = os.path.join(directory, file_name)
                if os.path.getsize(file_path) > 0:
                    with tarfile.open(os.path.join(directory, file_name), "r:gz") as tar_ref:
                        tar_ref.extractall(directory)
                    # Extract the contents of the .tar.gz file
                    count = count + 1

        logger.info(f"Unzipped {count} files")
