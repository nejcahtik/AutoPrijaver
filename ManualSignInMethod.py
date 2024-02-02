from Strings import Strings
from TimeSyncService import TimeSyncService
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManualSignInMethod:

    timeSyncService = TimeSyncService()
    driver = webdriver.Chrome()
    timeSlot = -1


    def tryToRegister(self, nOfRetries):

        try:
            print(Strings.TryingToFindBookButton)

            maxWaitTime = 5

            WebDriverWait(self.driver, maxWaitTime).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()=' Book ']"))
            )

            maxWaitTime = 5

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()=' Book ']"))
            )

            button = self.driver.find_elements(By.XPATH, "//button[text()=' Book ']")[self.timeSlot-1]

            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)

            self.driver.execute_script("arguments[0].click();", button)

            button = WebDriverWait(self.driver, maxWaitTime).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Yes']"))
            )
            button.click()

            button = WebDriverWait(self.driver, maxWaitTime).until(
                EC.presence_of_element_located((By.NAME, "_eventId_book"))
            )
            button.click()

            reservationConfirmedText = "You already have a booking for this event. If there is another slot you wish to " \
                                       "book, cancel your current booking first."

            WebDriverWait(self.driver, maxWaitTime).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{reservationConfirmedText}')]"))
            )

            print(Strings.ReservationConfirmed)
            print(Strings.Enjoy)
            print(Strings.Goodmorning)
        except Exception as e:
            print(Strings.FuckIFailed)

            if nOfRetries > 0:
                print(Strings.Retrying)
                self.tryToRegister(nOfRetries - 1)
            else:
                print(Strings.IGiveUp)


    def refreshBrowser(self):
        self.driver.refresh()

    def openSelenium(self):

        loginUrl = "https://popr.uni-lj.si/unauth/student/login"
        self.driver.get(loginUrl)


    def waitTill6am(self):

        timeToSleep = 300

        currentTMinusHours = self.getTMinusHours()

        while self.getTMinusHours() > 1:

            self.refreshBrowser()
            t.sleep(timeToSleep)

            if int(currentTMinusHours) != int(self.getTMinusHours()):
                currentTMinusHours = self.getTMinusHours()

                print(Strings.CheckingTMinusHours + str(self.getTMinusHours()))

                if int(self.getTMinusHours()) == 5:
                    print(Strings.ItsBoring)

                if int(self.getTMinusHours()) == 4:
                    print(Strings.Severina)


        currentTMinusMinutes = self.getTMinusMinutes()
        while self.getTMinusMinutes() > 15:

            self.refreshBrowser()
            t.sleep(timeToSleep)

            if self.getTMinusMinutes() - currentTMinusMinutes > 15:
                currentTMinusMinutes = self.getTMinusMinutes()
                print(Strings.CheckingTMinusMinutes + str(self.getTMinusMinutes()))

        print(Strings.Last15Minutes)

        while self.getTMinusMinutes() > 5:

            self.refreshBrowser()
            t.sleep(timeToSleep)

            if self.getTMinusMinutes() - currentTMinusMinutes > 5:
                currentTMinusMinutes = self.getTMinusMinutes()
                print(Strings.CheckingTMinusMinutes + str(self.getTMinusMinutes()))

        print(Strings.Last5Minutes)
        print(Strings.RecheckingTimeAndInternet)

        self.timeSyncService.syncTime()

        timeToSleep = 30

        while self.getTMinusMinutes() > 1:
            self.refreshBrowser()
            t.sleep(timeToSleep)

            print(Strings.CheckingTMinusMinutes + str(self.getTMinusMinutes()))

        print(Strings.NotALotLeft + str(self.getTMinusSeconds()) + Strings.Seconds)

        while self.getTMinusSeconds() > 15:
            t.sleep(1)

        self.refreshBrowser()

        print(Strings.AightBoysThisIsIt)

        while self.getTMinusSeconds() > -2:
            pass

        self.tryToRegister(10)


    def startManualProcedure(self):

        print(Strings.OpeningBrowserYouHave3MinutesToLogInAndGoToYourPage)

        while True:

            self.openSelenium()

            maxWaitTime = 180
            try:
                welcomeText = "Further information"
                WebDriverWait(self.driver, maxWaitTime).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{welcomeText}')]"))
                )
                break
            except Exception:
                print(Strings.YouFuckedUp)


        print(Strings.Goodnight)

        self.waitTill6am()
        # self.tryToRegister(2)


    def getTMinusHours(self):
        return self.timeSyncService.getTMinusTime().total_seconds() / 3600

    def getTMinusMinutes(self):
        return self.timeSyncService.getTMinusTime().total_seconds() / 60

    def getTMinusSeconds(self):
        return self.timeSyncService.getTMinusTime().total_seconds()

    def setTimeSlot(self, ts):
        self.timeSlot = ts

