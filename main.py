# ramdagadam ćuje se kada ti ga dam

from ManualSignInMethod import ManualSignInMethod
from Strings import Strings
from TimeSyncService import TimeSyncService

timeSyncService = TimeSyncService()
manualSignInMethod = ManualSignInMethod()

print(Strings.WarmupMessage)
timeSyncService.syncTime()
manualSignInMethod.startManualProcedure()









