import ntplib
from datetime import datetime, timedelta, timezone
import pytz

from Strings import Strings


class TimeSyncService:
    timeDifference = timedelta(days=0)

    def getLocalSystemDateTime(self):
        ljubljanaTimezone = pytz.timezone('Europe/Ljubljana')
        return datetime.now(ljubljanaTimezone)

    def syncTime(self):

        print(Strings.CheckingTimeDifferenceLabel)

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
            ljubljanaTimezone = timezone(ljubljanaTimezoneOffset)

            localDatetimeFromServer = utcDatetime + ljubljanaTimezoneOffset + timedelta(seconds=ping)
            localDatetimeFromServer = localDatetimeFromServer.replace(tzinfo=ljubljanaTimezone)

            localSystemTime = self.getLocalSystemDateTime()

            self.timeDifference = localDatetimeFromServer - localSystemTime

            print(Strings.TimeDifferenceLabel + str(self.timeDifference))

        except Exception as e:
            print(Strings.CantSyncTimesPossibleProblemWithInternet)
            print("Exception: " + str(e))


    def getCurrentExactDateTime(self):
        return self.getLocalSystemDateTime() + self.timeDifference


    def get6amDateTime(self):

        currentTime = self.getCurrentExactDateTime().time()
        wantedHour = 6
        wantedMinute = 0
        wantedSecond = 0

        if currentTime.hour > wantedHour:
            sixAmDateTime = self.getCurrentExactDateTime() + timedelta(days=1)
            sixAmDateTime = sixAmDateTime.replace(hour=wantedHour)
            sixAmDateTime = sixAmDateTime.replace(minute=wantedMinute)
            sixAmDateTime = sixAmDateTime.replace(second=wantedSecond)
            sixAmDateTime = sixAmDateTime.replace(microsecond=0)
        else:
            sixAmDateTime = self.getCurrentExactDateTime() + timedelta(microseconds=1)
            sixAmDateTime = sixAmDateTime.replace(hour=wantedHour)
            sixAmDateTime = sixAmDateTime.replace(minute=wantedMinute)
            sixAmDateTime = sixAmDateTime.replace(second=wantedSecond)
            sixAmDateTime = sixAmDateTime.replace(microsecond=0)

        return sixAmDateTime

    def getTMinusTime(self):
        return self.get6amDateTime() - self.getCurrentExactDateTime()
