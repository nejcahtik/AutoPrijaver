# ramdagadam ćuje se kada ti ga dam

from LoginMethod import LoginMethod
from ManualSignInMethod import ManualSignInMethod
from Strings import Strings
from TimeSyncService import TimeSyncService

userData = GetUserData()
timeSyncService = TimeSyncService()

print(Strings.WarmupMessage)
print("\n")

timeSyncService.syncTime()

if userData.loginMethod == LoginMethod.AUTOMATIC:
    # not yet implemented
    pass
elif userData.loginMethod == LoginMethod.MANUAL:
    manualSignInMethod = ManualSignInMethod()
    manualSignInMethod.startManualProcedure()









