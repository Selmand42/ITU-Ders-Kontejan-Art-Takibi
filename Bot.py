from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument("arg1", type=int, nargs="?", default=60)
parser.add_argument("arg2", type=int, nargs="?", default=60)
parser.add_argument("crns", nargs="*")
args = parser.parse_args()
crn = ",".join(args.crns)

url = "https://obs.itu.edu.tr/"

js_code = f"""
(function () {{
    var crn = [{crn}];
    const crninputs = document.querySelectorAll("input[type='number']");
    for (var i = 0; i < crn.length; i++) {{
        crninputs[i].value = crn[i];
        crninputs[i].dispatchEvent(new Event('input', {{ bubbles: true }}));
    }}
    void (0);
}})();
"""


driver = webdriver.Chrome()

try:
    driver.get(url)
    time.sleep(args.arg1)
    while True:
        driver.execute_script(js_code)
        button = driver.find_element(By.XPATH, "//*[@id=\"page-wrapper\"]/div[2]/div/div/div[3]/div/form/button")
        button.click()
        time.sleep(1)
        button = driver.find_element(By.XPATH, "//*[@id=\"modals-container\"]/div/div[2]/div/div[3]/button[2]")
        button.click()

        time.sleep(args.arg2)

except KeyboardInterrupt:
    print("Exit")
finally:
    driver.quit()
