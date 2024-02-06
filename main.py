# ramdagadam ćuje se kada ti ga dam

from Strings import Strings
from TimeSyncService import TimeSyncService

timeSyncService = TimeSyncService()

print(Strings.WarmupMessage)

print(Strings.AskForTimeslot)

while True:
    timeSlotStr = input(Strings.EnterNumber)

    try:
        timeSlot = int(timeSlotStr)

        if timeSlot > 0:
            break
    except Exception:
        pass
    print(Strings.YouFuckedUpEnteringNumber)

print(Strings.Deal)
print("\n")

from ManualSignInMethod import ManualSignInMethod

manualSignInMethod = ManualSignInMethod()
manualSignInMethod.setTimeSlot(timeSlot)
timeSyncService.syncTime()
manualSignInMethod.startManualProcedure()









