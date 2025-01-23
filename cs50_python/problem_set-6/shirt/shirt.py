import sys
import os
from PIL import Image, ImageOps

def p_shirt():
    correct_ext = [".jpg", ".jpeg", ".png"]
    full_cmd = sys.argv
    
    try:
        inp = True
        out = True
        equal =  True
        if len(full_cmd) == 3:
            file_before = sys.argv[1]
            file_after = sys.argv[2]

            if any(ext in file_before for ext in correct_ext)\
            and any(ext in file_after for ext in correct_ext):

                ext_FILEbefore = [file_before[index:]\
                for index, char in enumerate(file_before) if char == "."]

                ext_FILEafter = [file_after[index:]\
                for index, char in enumerate(file_after) if char == "."]

                if ext_FILEafter == ext_FILEbefore:
                    shirt_path = "shirt.png"

                    if os.path.exists(shirt_path):
                        shirt = Image.open(shirt_path)
                        person = Image.open(file_before)

                        person_resized = ImageOps.fit(person, shirt.size)

                        person_resized.paste(shirt, shirt)

                        person_resized.save(file_after)
                    else:
                        raise FileNotFoundError

                else:
                    equal = False
                    raise Exception
                
            elif any(ext not in file_before for ext in correct_ext):
                inp = False
                raise Exception
            elif any(ext not in file_after for ext in correct_ext):
                out = False
                raise Exception
        else:
            raise Exception
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)        
    except Exception:
        if len(full_cmd) < 3: print("Too few command-line arguments")
        if len(full_cmd) > 3: print("Too many command-line arguments")
        if inp == False: print("Invalid input")
        if out == False: print("Invalid output")
        if equal == False: print("Input and output have different extensions")
        sys.exit(1)
    
p_shirt()