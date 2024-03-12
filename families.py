instrument_families = { #fixed typo in dictionary name
  "Strings": ["Guitar", "Banjo", "Sitar"],
  "Percussion": ["Conga", "Cymbal", "Cajon"],
  "Woodwinds": ["Flute", "Oboe", "Clarinet"]
}

def print_instrument_families():
  for family in instrument_families: #fixed syntax error
    try: #added exception handling
      print("Some instruments in the {} family are: {}".format(family, instrument_families[family])) #formatted string
    except TypeError: #added custom error messages
      print("Type Error")
    except NameError:
      print("Name Error")
    except Exception:
      print("Other Error")

print_instrument_families()
