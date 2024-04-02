import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from win10toast import ToastNotifier
from selenium.common.exceptions import NoSuchElementException

toast = ToastNotifier()
driver = webdriver.Chrome() 
actionChains = ActionChains(driver)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def belgrade (applicantName, applicantDOB, applicantCount, applicantPhone, applicantEmail, applicantPassport, applicantCountry, applicantResidence):
    
    if driver.current_url == "https://konzinfobooking.mfa.gov.hu":
         driver.close()
         driver.get("https://konzinfobooking.mfa.gov.hu")
    else:
         driver.get("https://konzinfobooking.mfa.gov.hu")
    
    
    locationElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"label1\"]/button")))
    actionChains.move_to_element(locationElement).click().perform()

    inputLocationElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/input")))
    actionChains.move_to_element(inputLocationElement).click().send_keys("serbia").perform()
    belgradeElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modal2\"]/div/div/div[2]/div[83]/label")))
    actionChains.move_to_element(belgradeElement).click().perform()

    visaTypeElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(@data-target, '#modalCases')]")))
    actionChains.move_to_element(visaTypeElement).click().perform()

    inputVisaTypeElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/input")))
    actionChains.move_to_element(inputVisaTypeElement).click().send_keys("Visa").perform()
    visaCElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modalCases\"]/div/div/div[2]/div[40]/label")))
    actionChains.move_to_element(visaCElement).click().perform()

    saveTypeElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modalCases\"]/div/div/div[3]/button[2]")))
    actionChains.move_to_element(saveTypeElement).click().perform()

    nameElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label4']")))
    actionChains.move_to_element(nameElement).click().send_keys(applicantName).perform()

    birthDateElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='birthDate']")))
    actionChains.move_to_element(birthDateElement).click().send_keys(applicantDOB).perform()

    applicantsElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label6']")))
    driver.find_element(By.XPATH, "//*[@id='label6']").clear()
    actionChains.move_to_element(applicantsElement).click().send_keys(applicantCount).perform()

    phoneElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label9']")))
    actionChains.move_to_element(phoneElement).click().send_keys(applicantPhone).perform()

    emailElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label10']")))
    actionChains.move_to_element(emailElement).click().send_keys(applicantEmail).perform()

    passportNumberElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label1000']")))
    actionChains.move_to_element(passportNumberElement).click().send_keys(applicantPassport).perform()

    countryElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label1001']")))
    actionChains.move_to_element(countryElement).click().send_keys(applicantCountry).perform()

    residenceElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label1002']")))
    actionChains.move_to_element(residenceElement).click().send_keys(applicantResidence).perform()

    checkbox1Element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='slabel13']")))
    actionChains.move_to_element(checkbox1Element).click().perform()

    checkbox2Element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label13']")))
    actionChains.move_to_element(checkbox2Element).click().perform()

    saveElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary w-100']")))
    actionChains.move_to_element(saveElement).click().perform()

    errorElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Torles\"]/div/div/div[1]/div")))

def subotica(applicantName, applicantDOB, applicantCount, applicantPhone, applicantEmail, applicantPassport):

    if driver.current_url == "https://konzinfobooking.mfa.gov.hu":
         driver.close()
         driver.get("https://konzinfobooking.mfa.gov.hu")
    else:
         driver.get("https://konzinfobooking.mfa.gov.hu")

    locationElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"label1\"]/button")))
    actionChains.move_to_element(locationElement).click().perform()

    inputLocationElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/input")))
    actionChains.move_to_element(inputLocationElement).click().send_keys("serbia").perform()
    suboticaElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modal2\"]/div/div/div[2]/div[84]/label")))
    actionChains.move_to_element(suboticaElement).click().perform()

    visaTypeElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(@data-target, '#modalCases')]")))
    actionChains.move_to_element(visaTypeElement).click().perform()

    inputVisaTypeElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/input")))
    actionChains.move_to_element(inputVisaTypeElement).click().send_keys("Visa").perform()
    visaCElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modalCases\"]/div/div/div[2]/div[36]/label")))
    actionChains.move_to_element(visaCElement).click().perform()

    saveTypeElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modalCases\"]/div/div/div[3]/button[2]")))
    actionChains.move_to_element(saveTypeElement).click().perform()

    nameElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label4']")))
    actionChains.move_to_element(nameElement).click().send_keys(applicantName).perform()

    birthDateElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='birthDate']")))
    actionChains.move_to_element(birthDateElement).click().send_keys(applicantDOB).perform()

    applicantsElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label6']")))
    driver.find_element(By.XPATH, "//*[@id='label6']").clear()
    actionChains.move_to_element(applicantsElement).click().send_keys(applicantCount).perform()

    phoneElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label9']")))
    actionChains.move_to_element(phoneElement).click().send_keys(applicantPhone).perform()

    emailElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label10']")))
    actionChains.move_to_element(emailElement).click().send_keys(applicantEmail).perform()

    passportNumberElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label1000']")))
    actionChains.move_to_element(passportNumberElement).click().send_keys(applicantPassport).perform()

    checkbox1Element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='slabel13']")))
    actionChains.move_to_element(checkbox1Element).click().perform()

    checkbox2Element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label13']")))
    actionChains.move_to_element(checkbox2Element).click().perform()

    saveElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary w-100']")))
    actionChains.move_to_element(saveElement).click().perform()

    errorElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Torles\"]/div/div/div[1]/div")))

def startbg():
    belgrade(entName.get(), entDOB.get(), entCount.get(), entPhone.get(), entEmail.get(), entPassport.get(), entCountry.get(), entResidence.get())
    time.sleep(5)
    if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button") == True:
            time.sleep(random.randint(80, 100))
            startbg()
    else:
        toast.show_toast(
        "Embassy slot found!",
        "Belgrade",
        duration = 20,
        threaded = True,
        )
        time.sleep(20)
        toast.show_toast(
        "Embassy slot found!",
        "Belgrade",
        duration = 20,
        threaded = True,
        )
        time.sleep(20)
        toast.show_toast(
        "Embassy slot found!",
        "Belgrade, 30 minutes to take it",
        duration = 20,
        threaded = True,
        )
        time.sleep(1800)

def startsb():
    subotica(entName.get(), entDOB.get(), entCount.get(), entPhone.get(), entEmail.get(), entPassport.get())
    time.sleep(5)
    if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button") == True:
            time.sleep(random.randint(80, 100))
            startsb()
    else:
        toast.show_toast(
        "Embassy slot found!",
        "Subotica",
        duration = 20,
        threaded = True,
        )
        time.sleep(20)
        toast.show_toast(
        "Embassy slot found!",
        "Subotica",
        duration = 20,
        threaded = True,
        )
        time.sleep(20)
        toast.show_toast(
        "Embassy slot found!",
        "Subotica",
        duration = 20,
        threaded = True,
        )
        time.sleep(1800)   

def startbgsb():
    belgrade(entName.get(), entDOB.get(), entCount.get(), entPhone.get(), entEmail.get(), entPassport.get(), entCountry.get(), entResidence.get())
    if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button") == True:
            time.sleep(random.randint(80, 100))
            subotica(entName.get(), entDOB.get(), entCount.get(), entPhone.get(), entEmail.get(), entPassport.get())
            if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button") == True:
                time.sleep(random.randint(80, 100))
                startbgsb()
            else:
                toast.show_toast(
                "Embassy slot found!",
                "Subotica",
                duration = 20,
                threaded = True,
                )
                time.sleep(20)
                toast.show_toast(
                "Embassy slot found!",
                "Subotica",
                duration = 20,
                threaded = True,
                )
                time.sleep(20)
                toast.show_toast(
                "Embassy slot found!",
                "Subotica",
                duration = 20,
                threaded = True,
                )
                time.sleep(1800)    
    else:
        toast.show_toast(
        "Embassy slot found!",
        "Belgrade",
        duration = 20,
        threaded = True,
        )
        time.sleep(20)
        toast.show_toast(
        "Embassy slot found!",
        "Belgrade",
        duration = 20,
        threaded = True,
        )
        time.sleep(20)
        toast.show_toast(
        "Embassy slot found!",
        "Belgrade",
        duration = 20,
        threaded = True,
        )
        time.sleep(1800)

def stop():
    driver.close()
    sys.exit()

window = tk.Tk()
window.title("Embassy Slot Requester")
window.resizable(width=False, height=False)

frmEntry = tk.Frame(master=window)
lblName = tk.Label(master=frmEntry, text="Имя и Фамилия")
entName = tk.Entry(master=frmEntry, width=30)
lblDOB = tk.Label(master=frmEntry, text="Дата рождения ДД.ММ.ГГГГ")
entDOB = tk.Entry(master=frmEntry, width=30)
lblCount = tk.Label(master=frmEntry, text="Количество подающих")
entCount = tk.Entry(master=frmEntry, width=30)
lblPhone = tk.Label(master=frmEntry, text="Номер телефона")
entPhone = tk.Entry(master=frmEntry, width=30)
lblEmail = tk.Label(master=frmEntry, text="Email")
entEmail = tk.Entry(master=frmEntry, width=30)
lblPassport = tk.Label(master=frmEntry, text="Номер паспорта | XXXXXXXXX")
entPassport = tk.Entry(master=frmEntry, width=30)
lblCountry = tk.Label(master=frmEntry, text="(Только Белград) Гражданство | Russian Federation")
entCountry = tk.Entry(master=frmEntry, width=30)
lblResidence = tk.Label(master=frmEntry, text="(Только Белград) Номер и дата окончания ВНЖ | A000000 ДД.ММ.ГГГГ")
entResidence = tk.Entry(master=frmEntry, width=30)

lblName.grid(row=0, column=0, sticky="e")
entName.grid(row=0, column=1, sticky="w")
lblDOB.grid(row=1, column=0, sticky="e")
entDOB.grid(row=1, column=1, sticky="w")
lblCount.grid(row=2, column=0, sticky="e")
entCount.grid(row=2, column=1, sticky="w")
lblPhone.grid(row=3, column=0, sticky="e")
entPhone.grid(row=3, column=1, sticky="w")
lblEmail.grid(row=4, column=0, sticky="e")
entEmail.grid(row=4, column=1, sticky="w")
lblPassport.grid(row=5, column=0, sticky="e")
entPassport.grid(row=5, column=1, sticky="w")
lblCountry.grid(row=6, column=0, sticky="e")
entCountry.grid(row=6, column=1, sticky="w")
lblResidence.grid(row=7, column=0, sticky="e")
entResidence.grid(row=7, column=1, sticky="w")

btnBelgrade = tk.Button(
    master=window,
    text="Start Belgrade",
    command=startbg
)
btnSubotica = tk.Button(
    master=window,
    text="Start Subotica",
    command=startsb
)
btnBelgradeSubotica = tk.Button(
    master=window,
    text="Start Belgrade and Subotica",
    command=startbgsb
)
btnStop = tk.Button(
    master=window,
    text="Exit",
    command=stop
)

frmEntry.grid(row=0, column=0, padx=10)
btnBelgrade.grid(row=0, column=1, pady=10)
btnSubotica.grid(row=0, column=2, pady=10)
btnBelgradeSubotica.grid(row=0, column=3, pady=10)
btnStop.grid(row=0, column=4, padx=10)

window.mainloop()