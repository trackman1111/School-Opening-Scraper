import logging
from timeit import default_timer as timer
import alabama
#import arizona
import colorado
import illinois
import new_mexico
import maryland
import ohio
import oregon
import south_carolina
import tennessee
#import virginia
import washington

# Runs all state scripts that are currently available
if __name__ == '__main__':
    # disabledStates = ["arizona", "virginia"]

    currentStates = ["alabama", "colorado", "illinois", "new_mexico", "maryland", "ohio", "oregon", "south_carolina",
                     "tennessee", "washington"]

    successes = []
    failures = []

    startTimer = timer()
    for state in currentStates:
        try:
            exec("{stateName}.main()".format(stateName=state))
            successes.append(state)
        except Exception:
            logging.error("Failed to fetch %s", state, exc_info=True)
            failures.append(state)

    endTimer = timer()
    elapsed = endTimer - startTimer

    print("Fetched data for " + str(successes) + " in " + str(elapsed) + " seconds.")
    if failures:
        print("Failed to fetch: " +  str(failures))



