#For local storage, I decided to use JavaScript Object Notation - "JSON" - see 'https://docs.python.org/3/library/json.html' for details
#This storage type works well, since this safety data intended to be a number of short headlines with relevant data, I.E key:value pairs
#From this json file, the program should compile a list of each first-level item in the json file, since these are each induvidual chemical entry for the user to select
#And finally a way, propably via some other functions or plugins, to convert it into printable formats, propably something like .pdf, .docx or .odt
#Perhaps make a GUI for entering new chemicals and then selecting them, for ease of usage, including a way for the user to define working directory themselves if needed
#May also need a way to incorporate simple graphics objects like tables, for instance having the json file reference an imagine that is then pulled into the file generated upon selection
import json

#JSON test case, simple dictionary with a single entry, dihydrogen monoxide, which in turn contains a bunch of key:value pairs of different parameters and related data
#These entries aren't quite complete, if I were to bring these to a lab, extra data would be added
test_json = {
    "Dihydrogen monoxide": {                            #For those uninitiated, this is a parody name technically correct, but not commonly used outside of jokes
        "Other names": "Water",
        "Category": "Uncategorized",
        "Boiling point": "100 C",
        "Melting point": "0 C",
        "Density": "1.00 g/cm^3",
        "Specific heat capaicty": "4184 J / (kg * K)",  #Specific heat capacity uses kelvin, K
        "Warning labels": "None",
        "Toxicity data": "None; edible",
        "Storage": "Closed vessel or drawn from tap",
        "Disposal": "Drain - it is simply water"
    },
    "Hydrochloric acid": {
        "Other names": "Chlorane, Muriatic acid",
        "Category": "Mineral acid",
        "Boiling point": "Concentration dependent - see table",    #This poses a problem, it would be useful to have the program incorporate the table referenced, currently it can't
        "Melting point": "Concentration dependent - see table",     #Same as boiling point comment
        "Warning labels": "Corrosive, Irritant",
        "Hazard statements": "H290, H314, H335",
        "Storage": "In closed dark glass bottle or other low-light, non-corrosive enivronment",
        "Disposal": "Dilute WELL in water and pour down drain, or collect in halogen waste",
        "Notes": "Beware, generates heat on mixing with water. Hydrogen chloride is the name of the gaseous form"
    },
    "Sodium Hydroxide": {
        "Other names": "Caustic soda, Lye",
        "Category": "Mineral base",
        "Boiling point": "1388 C",
        "Melting point": "323 C",
        "Warning labels": "Corrosive, Irritant",
        "Hazard statements": "H290, H302, H314",
        "Storage": "Store in closed, non-corrosive glass or other material",
        "Disposal": "Dilute WELL and pour down drain, or dispose of in organic/solid waste",
        "Notes": "Typically supplied in dry pellet form and mixed into water upon need - dilution in water generates heat!"
    }
}

with open("chemical_safety_data.json", "w") as file:   #Learning json, these two lines first open the data .json file (or creates it if it does not exist) in write mode, as 'file'
    json.dump(test_json, file, indent=4)               #This line then overwrites (or creates) the .json file with the data, currently the test case above

with open("chemical_safety_data.json", "r") as file:   #Same as example above, except with read mode "r"
    safety_data = json.load(file)                      #This loads the json file into the safety_data variable for use by the program

print(safety_data)


