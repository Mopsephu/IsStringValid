_NUMBERS_ : tuple[int] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

#Returns True if the string can be converted to int/float
def is_valid(text : str, Type : type[int | float]) -> bool:
    foundSolution : bool = False;
    try:
        if Type is int:
            int(text);
            foundSolution = True;
        elif Type is float:
            if text.count(".") == 1:
                if text.find(".") > 0:
                    if int(text[text.find(".")-1]) in _NUMBERS_ and int(text[text.find(".")+1]) in _NUMBERS_:
                        float(text);
                        foundSolution = True;
        else:
            print(f"{Type} is not supportable type for comparisment!");
        return foundSolution;
    except ValueError:
        return False;
    except IndexError:
        return False;