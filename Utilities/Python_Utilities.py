#--------------UTILS FOR PYTHON

import functools, os, json, datetime, time, sys
import colorama as clr
clr.init(autoreset=True)
red = clr.Fore.RED
blue= clr.Fore.BLUE
green = clr.Fore.GREEN
yellow = clr.Fore.YELLOW
magenta = clr.Fore.MAGENTA
cyan = clr.Fore.CYAN
black = clr.Fore.BLACK
white = clr.Fore.WHITE


#---------------------------------------------FUNCTIONS-----------------------------------------------------
SAVEFILE = None
SESSIONSTARTTIME = None

# 1) getretry function : asks if user wants to restart program, returns accordingly:
# returns True if input starts with "y" (includes yes, y, yeah, etc). Can change this.
# directly depends on getinput() function defined below.
def getretry():
      retry = getinput(prompt= "Run Program Again? (Yes/No): ",
                       choices= {"y","yes","n","no"},
                       ).lower()
      
      return True if retry.startswith("y") else False

# 1.b) Better getretry() independant of getinput():
def getretryv2():
    accepted = {"yes","y","no","n"}
    while True:
            retry = input("Restart? (Y/N):  ")
            if retry not in accepted:
                print("Invalid Input")
                continue
            else:
                 return retry.startswith("y")


# 2) getinput function: huge all-in-one input validation function with multiple toggles for every cases.
# includes only integers, only strings, strings with toggleable special characters, min/max. all string checks are performed on .strip().lower() version of input.
# NOTE:
# The function has a special if condition at the top to allow for special input needs where you need
# an otherwise only integer input with select choices for string inputs.
# This can result in getinput() providing different data types. Always ensure this part works as intended.

def getinput(
    prompt,

    # Mode toggles
    allowstr=True,      #whether or not to allow letters, automatically disables all checks for 'string rules' toggles.
    intgrs=False,       #whether or not numbers are allowed. when combined with false allowstr, switches to integer checking mode

    # String rules
    spclchar=False,         #whether special characters are allowed -- does not include spaces
    allowspaces=True,      #whether spaces are allowed anywhere in the string (by default whitespaces are removed with .strip() before this toggle is checked)
    min_length=1,           #minimum character length for input, only checked in string mode(inclusive)
    max_length=999,         #maximum character length for input, only checked in string mode (inclusive)

    # Integer rules
    min_value=1,            #minimum value for number. only applies in 'integer mode', i.e when only integer inputs are validated. 
    max_value=999,          #maximum value for number. only applies in 'integer mode', i.e when only integer inputs are validated.

    # Choices
    choices=None,           #if set to list/tuple/set, etc, function checks if input is a part of defined choices. special case in integer mode (refer above).

    # Error messages
    errormsg="Invalid input.",
    errormsg_stronly= "Input must have letters.",
    errormsg_intonly="Input must be a valid integer.",
    errormsg_intgrs="Numbers are not allowed.",
    errormsg_spclchar="Special characters are not allowed.",
    errormsg_spaces="Spaces are not allowed.",
    errormsg_choices="Invalid choice.",
    errormsg_range= "Input out of allowed range.",
):
    while True:
        raw = input(prompt)
        value = raw.strip().lower()

        if not value:
            print(f"Error: {errormsg}\nTry Again.\n")
            continue

        # ---------- INTEGER MODE ----------
        if intgrs and not allowstr:  
                try:
                    # INTEGER CHECK
                    num = int(value)
                except ValueError:
                    print(f"Error: {errormsg_intonly}\nTry Again.\n")
                    continue

                # RANGE CHECK
                if min_value is not None and max_value is not None and num not in range(min_value, max_value + 1):
                    print(f"Error: {errormsg_range}\nAllowed Range:\n{min_value} - {max_value}.\nTry Again.")
                    continue

                # CHOICES (case-insensitive) CHECK
                if choices is not None and num not in choices:
                    print(f"Error: {errormsg_choices}\nAllowed Choices:\n{choices}.\nTry Again.\n")
                    continue 

                return num

        # ---------- STRING MODE ----------
        if allowstr:
            # LENGTH CHECK
            length = len(value)
            if length not in range(min_length, max_length + 1):
                print(
                    f"Error: Input length must be between "
                    f"{min_length} and {max_length} characters.\n"
                    "Try Again.\n"
                )
                continue

            # LETTER CHECK
            if not any(ch.isalpha() for ch in value):
                print(f"Error: {errormsg}\nTry Again.\n")
                continue

            # INTEGER CHECK
            if not intgrs and any(ch.isdigit() for ch in value):
                print(f"Error: {errormsg_intgrs}\nTry Again.\n")
                continue

            # SPACES CHECK
            if not allowspaces and " " in value:
                print(f"Error: {errormsg_spaces}\nTry Again.\n")
                continue

            # SPECIAL CHARACTERS CHECK
            if not spclchar and any(not ch.isalnum() and ch != " " for ch in value):
                print(f"Error: {errormsg_spclchar}\nTry Again.\n")
                continue

            # CHOICES (case-insensitive) CHECK
            if choices is not None:
                if value.lower() not in {str(c).lower() for c in choices}:
                    print(f"Error: {errormsg_choices}\nTry Again.\n")
                    continue

            return value

        # ---------- INVALID CONFIG ----------
        print("Error: Invalid input configuration.\n")

# 3) getintegerinput function: function used when only integer inputs are needed, pretty much same as getinput function
# fossilized, not needed, getinput does all the work of this function, yet may serve useful where it is faster to code calls for this function rather than getinput 
# due to the higher number of parameters to define to switch getinput into integer mode.
# does not contain the special integer case condition coded in getinput

def getintegerinput(
    prompt,
    errormsg="Value must be a valid integer.",
    errormsgmin="Value is too low.",
    errormsgmax="Value is too high.",
    min=None,
    max=None,
    intonly=True
):
    while True:
        raw = input(prompt).strip()
        raw = raw.replace(",","") if "," in raw else raw
        try:
            value = int(raw)
        except ValueError:
            print(f"Error: {errormsg}\nTry Again.\n")
            continue

        if intonly:
            if min is not None and value < min:
                print(f"Error: {errormsgmin}\nTry Again.\n")
                continue
            if max is not None and value > max:
                print(f"Error: {errormsgmax}\nTry Again.\n")
                continue

        return value
    
# 4) gettimeprint(): returns time elapsed since SESSIONSTARTTIME, which has to be a previously defined global variable.

def gettimeprint():
    elapsedseconds = int(time.time() - SESSIONSTARTTIME)
    hours = elapsedseconds // 3600
    minutes = (elapsedseconds % 3600) // 60
    seconds = elapsedseconds % 60
    timeprint = f"{hours}hrs {minutes}mins {seconds}s"
    return timeprint

# 6) savesuggestion: saves suggestions. takes a "mode" and "suggestion" parameter. suggestion save format can be altered. by default saves day, date and time as well.

def savesuggestion(
        suggestion,
        mode
):
    folderpath = R"C:\Users\Daivik\Documents\VS"
    filename = SAVEFILE
    fullpath = os.path.join(folderpath, filename)
    timeprint = gettimeprint()
    DATETIMEFORMATTED = datetime.datetime.now().strftime("%A, %B %d, %Y,  %H:%M:%S")
    newentry = {
        "Day and Date": DATETIMEFORMATTED,
        "Time  Played at Input": timeprint,
        "Mode": mode,
        "Suggestion": suggestion.title(),
    }
    currentdata = []
    if os.path.exists(fullpath):
        try:
            with open(fullpath, "r") as f:
                currentdata = json.load(f)
        except json.JSONDecodeError:
            pass
    else:
        print("Error.\nFile Not Found")
    currentdata.append(newentry)
    try:
        os.makedirs(folderpath, exist_ok= True)
        with open(fullpath, "w") as f:
            json.dump(currentdata, f, indent=4)
            return True
    except  Exception as e:
        print(f"Error Saving File: {e}")
        return False

# 7) wrapper function template:

def my_decorator(func):
    @functools.wraps(func) # 1. Preserves the name of the original function
    def wrapper(*args, **kwargs): # 2. Accepts ANY arguments
        # --- DO STUFF BEFORE ---
        print(">>> Starting function...")
        
        # 3. Run original function with its arguments
        result = func(*args, **kwargs)
        
        # --- DO STUFF AFTER ---
        print(">>> Function finished.")
        
        return result # 4. Return the value
    return wrapper


def isprime(n):
    if n <= 1:
        is_prime = False
    else:
        is_prime = True  # Flag variable
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime

def title(string):
    return string.strip().lower().title()

if __name__ == "__main__":
    import pygame