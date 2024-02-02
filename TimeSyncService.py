import ntplib
from datetime import datetime, timedelta, time
import pytz

from Strings import Strings


class TimeSyncService:
    timeDifference = 0

    def getLocalSystemDateTime(self):
        ljubljanaTimezone = pytz.timezone('Europe/Ljubljana')
        return datetime.now(ljubljanaTimezone)

    def syncTime(self):

        print("\n")
        print(Strings.CheckingTimeDifferenceLabel)
        print("\n")

        ntpServer = 'pool.ntp.org'

        try:

            client = ntplib.NTPClient()

            timeBeforeSending = self.getLocalSystemDateTime()
            response = client.request(ntpServer)
            timeAfterSending = self.getLocalSystemDateTime()

            ping = (timeAfterSending - timeBeforeSending).total_seconds() / 2

            ntpTimestamp = response.tx_time
            utcDatetime = datetime.utcfromtimestamp(ntpTimestamp)
            ljubljanaTimezoneOffset = timedelta(hours=1)
            localDatetimeFromServer = utcDatetime + ljubljanaTimezoneOffset + timedelta(seconds=ping)

            localSystemTime = self.getLocalSystemDateTime()

            self.timeDifference = localDatetimeFromServer - localSystemTime

            print(Strings.TimeDifferenceLabel + self.timeDifference)

        except Exception as e:
            print(Strings.CantSyncTimesPossibleProblemWithInternet)
            print("\n")
            print("Exception" + str(e))


    def getCurrentExactDateTime(self):
        return self.getLocalSystemDateTime() + self.timeDifference


    def get6amDateTime(self):

        currentTime = self.getCurrentExactDateTime().time()

        if currentTime.hour > 6:
            sixAmDateTime = self.getCurrentExactDateTime() + timedelta(days=1)
            sixAmDateTime.replace(hour=6)
            sixAmDateTime.replace(minute=0)
            sixAmDateTime.replace(second=0)
            sixAmDateTime.replace(microsecond=0)
        else:
            sixAmDateTime = self.getCurrentExactDateTime() + timedelta(microseconds=1)
            sixAmDateTime.replace(hour=6)
            sixAmDateTime.replace(minute=0)
            sixAmDateTime.replace(second=0)
            sixAmDateTime.replace(microsecond=0)

        return sixAmDateTime

    def getTMinusTime(self):
        return self.get6amDateTime() - self.getCurrentExactDateTime()
