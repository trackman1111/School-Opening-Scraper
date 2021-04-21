import logging
from timeit import default_timer as timer
import importlib
import os

# Runs all state scripts that are currently available
if __name__ == '__main__':
    # disabledStates = ["arizona", "virginia"]

    currentStates = ["alabama", "colorado", "illinois", "new_mexico", "maryland", "ohio", "oregon", "south_carolina",
                     "tennessee", "washington"]

    modules = {}
    for state in currentStates:
        try:
            modules[state] = importlib.import_module(state)
        except ImportError:
            logging.error("Failed to import %s", state, exc_info=True)
    
     for folder in ["temp","out"]:
    	if not os.path.isdir(folder):
    		try:
    			os.mkdir(folder)
    		except: 
    			print(folder+" folder does not exist and could not be created")
    		

    successes = []
    failures = []

    startTimer = timer()
    for state in currentStates:
        try:
            exec("modules['{stateName}'].main()".format(stateName=state))
            successes.append(state)
        except Exception:
            logging.error("Failed to fetch %s", state, exc_info=True)
            failures.append(state)

    endTimer = timer()
    elapsed = endTimer - startTimer

    print("Fetched data for " + str(successes) + " in " + str(elapsed) + " seconds.")
    if failures:
        print("Failed to fetch: " + str(failures))



