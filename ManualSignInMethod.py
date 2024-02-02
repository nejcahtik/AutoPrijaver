from Strings import Strings
from TimeSyncService import TimeSyncService
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManualSignInMethod:

    timeSyncService = TimeSyncService()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome()
    numberOfRetries = 10


    def tryToRegister(self, nOfRetries):

        try:
            print(Strings.TryingToFindBookButton)
            print("\n")

            button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-sm")
            button.click()

            maxWaitTime = 10

            WebDriverWait(self.driver, maxWaitTime).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.message"))
            )

            button = self.driver.find_element(By.XPATH, "//button[text()='YES']")
            button.click()

            button = self.driver.find_element(By.ID, "14362")
            button.click()

            reservationConfirmedText = "You already have a booking for this event. If there is another slot you wish to " \
                                       "book, cancel your current booking first."

            WebDriverWait(self.driver, maxWaitTime).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{reservationConfirmedText}')]"))
            )

            print(Strings.ReservationConfirmed)
            print("\n")
            print(Strings.Enjoy)
            print("\n")
            print(Strings.Goodmorning)
        except Exception as e:
            print(Strings.FuckIFailed)
            print("\n")
            if(nOfRetries > 0):
                print(Strings.Retrying)
                self.tryToRegister(nOfRetries - 1)
            else:
                print(Strings.IGiveUp)


    def refreshBrowser(self):
        self.driver.refresh()

    def openSelenium(self):

        loginUrl = "https://popr.uni-lj.si/unauth/student/login"
        self.driver.get(loginUrl)


    def waitFor6am(self):

        timeToSleep = 300

        currentTMinusHours = self.getTMinusHours()

        while self.getTMinusHours() > 1:

            self.refreshBrowser()
            t.sleep(timeToSleep)

            if currentTMinusHours != self.getTMinusHours():
                currentTMinusHours = self.getTMinusHours()

                print(Strings.CheckingTMinusNote + str(self.getTMinusHours()))
                print("\n")

                if self.getTMinusHours() == 5:
                    print(Strings.ItsBoring)
                    print("\n")

                if self.getTMinusHours() == 4:
                    print(Strings.Severina)
                    print("\n")


        currentTMinusMinutes = self.getTMinusMinutes()
        while self.getTMinusMinutes() > 15:

            self.refreshBrowser()
            t.sleep(timeToSleep)

            if self.getTMinusMinutes() - currentTMinusMinutes > 15:
                currentTMinusMinutes = self.getTMinusMinutes()
                print(Strings.CheckingTMinusNote + self.getTMinusMinutes())
                print("\n")

        print(Strings.Last15Minutes)

        while self.getTMinusMinutes() > 5:

            self.refreshBrowser()
            t.sleep(timeToSleep)

            if self.getTMinusMinutes() - currentTMinusMinutes > 5:
                currentTMinusMinutes = self.getTMinusMinutes()
                print(Strings.CheckingTMinusNote + self.getTMinusMinutes())
                print("\n")

        print(Strings.Last5Minutes)
        print("\n")
        print(Strings.RecheckingTimeAndInternet)
        print("\n")

        self.timeSyncService.syncTime()

        timeToSleep = 30

        while self.getTMinusMinutes() > 1:
            self.refreshBrowser()
            t.sleep(timeToSleep)

            print(Strings.CheckingTMinusNote + self.getTMinusMinutes())
            print("\n")

        print(Strings.NotALotLeft + self.getTMinusSeconds() + Strings.Seconds)
        print("\n")


        while self.getTMinusSeconds() > 15:
            t.sleep(1)

        self.refreshBrowser()

        print(Strings.AightBoysThisIsIt)
        print("\n")

        while self.getTMinusSeconds() < 2:
            pass

        self.tryToRegister(self.numberOfRetries)


    def startManualProcedure(self):

        print(Strings.OpeningBrowserYouHave3MinutesToLogInAndGoToYourPage)
        print("\n")

        while True:

            self.openSelenium()

            maxWaitTime = 180

            beforeTime = self.timeSyncService.getCurrentExactDateTime()
            welcomeText = "Dobrodošli! / Welcome!"
            WebDriverWait(self.driver, maxWaitTime).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{welcomeText}')]"))
            )
            afterTime = self.timeSyncService.getCurrentExactDateTime()

            timeDiff = afterTime - beforeTime

            if timeDiff.total_seconds() < 179:
                break
            else:
                self.driver.close()
                print(Strings.YouFuckedUp)
                print("\n")


        currentTMinusHours = self.getTMinusHours()

        print(Strings.TMinusHoursNote + currentTMinusHours)
        print("\n")

        self.waitFor6am()


    def getTMinusHours(self):
        return self.timeSyncService.getTMinusTime().total_seconds() / 3600

    def getTMinusMinutes(self):
        return self.timeSyncService.getTMinusTime().total_seconds() / 60

    def getTMinusSeconds(self):
        return self.timeSyncService.getTMinusTime().total_seconds()

