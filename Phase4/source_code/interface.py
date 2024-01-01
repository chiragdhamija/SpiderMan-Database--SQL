# python interfeace to the database for project database
# Functionalities to be implemented:
# 1. Simple Sql query (Select, Insert, Update, Delete)
# 2. Complex Projection Query 
# 3. Aggreate Query
# 4. Nested Query
# Example: Villain Opposition Network report
# Example: Spider Person Efficiency report
# Example: Equipment Usage report
# Example: Mission Completion report


import pymysql
import pymysql.cursors
import subprocess as sp
import os
from PIL import Image
from io import BytesIO
import tempfile

c = None # cursor
conn = None # connection
tmp = None # shell pprocess variable
DB = 'spiderverse'

def is_image_valid(file_path):
    try:
        # Attempt to open the image file
        with Image.open(file_path) as img:
            # Check if the image loaded successfully
            return True
    except (OSError, PIL.UnidentifiedImageError, PIL.DecompressionBombError) as e:
        # Handle the exception (e.g., print an error message)
        print(f"Error loading image: {e}")
        return False

def display_image(image_data):
    # Open the image using Pillow
    image = Image.open(BytesIO(image_data))

    # Resize the image to fit the terminal width
    terminal_width = 70  # You can adjust this based on your terminal width
    aspect_ratio = image.width / image.height
    terminal_height = int(terminal_width / aspect_ratio)
    image = image.resize((terminal_width, terminal_height))

    '''    
    # Convert the image to ANSI escape codes for terminal graphics
    image_code = "\033]1337;File=width={},height={};inline=1:{}\007".format(
        image.width, image.height, BytesIO(image_data).read()
    )

    print(image_code)
    '''
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    image.save(temp_file, format="png")
    temp_file.close()

    # Use img2txt tool from iterm2-tools to display the image in the terminal
    sp.run(["img2txt", "-W", str(terminal_width), temp_file.name])

    # Clean up the temporary file after displaying the image
    os.unlink(temp_file.name)

def PrintTableContents(table):
    global c
    global conn

    try:
        headers = []
        # first print the headers
        c.execute("SHOW COLUMNS FROM " + table + ";")
        print("----------" + table + "----------")
        i = 0
        for row in c.fetchall():
            print(row['Field'], end="\t")
            headers.append(row['Field'])
            i += 1
        
        print("\n")
        
        # now print the contents
        c.execute("SELECT * FROM " + table + ";")
        for row in c.fetchall():
            for i in range(len(row)):
                print(row[headers[i]], end="\t")
            print("\n")
    
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1
        

    return 0

def PrintTables():
    global c
    try:
        c.execute("SHOW tables;")
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1

    print("Tables in the database: ")
    i = 1
    for row in c.fetchall():
        print(i,end=". ")
        print(row['Tables_in_'+DB], end=": \n")
        i+=1
        PrintColumns(row['Tables_in_'+DB])
        print()

    return 0

def PrintColumns(table):
    query = "DESC " + table 
    try:
        c.execute(query)
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1

    print("[Attributes of " + table + ":]")
    i = 1
    for row in c.fetchall():
        print("  ",end="")
        print(i,end=". ")
        print(row['Field'])
        i+=1

    return 0

def HandleSimpleSQL(query):
    # execute the query
    try:
        c.execute(query)
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1

    # print the result
    for row in c.fetchall():
        print(row)
    
    return 0

def HandleInsert():
    global c
    print("Available tables: ")
    print("----Entity Tables----")
    print("1. SpiderPerson")
    print("2. Villain")
    print("3. Mission")
    print("4. Organization")
    print("5. SideCharacter")
    print("6. ResearchNotes")
    print("7. Equipment")
    print("8. AbilitiesSpiderPerson")
    print("9. AbilitiesVillain")
    print("10. AbilitiesSideChar")

    print("----Relationship Tables----")
    print("1. Mentors")
    print("2. FacesOffAgainst")
    print("3. Owns")
    print("4. HeadsMission")
    print("5. MemberOf")
    print("6. AssociatesWith")
    print("7. Hypothesis")
    print("8. Participant")
    print("\nNOTE: Enter NULL for any field that is not applicable (for autoincrement fields)\n")

    print("Enter the table name: ")
    table = input()
    if table == "exit":
        return 0

    query = "INSERT INTO " + table
    query += " SET "

    match table:
        # Entity Tables
        case "SpiderPerson":
            print("Enter the SpiderPersonID:")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:   
                query += "SpiderIdentifier = " + SpiderPersonID + ", "

            print("Enter the SpiderPerson RealName: ")
            SpiderPersonName = input()
            if "NULL" not in SpiderPersonName:
                query += "RealName = \'" + SpiderPersonName + "\', "

            print("Enter the SpiderPerson Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "

            print("Enter the SpiderPerson HeroName: ")
            HeroName = input()
            if "NULL" not in HeroName:
                query += "HeroName = \'" + HeroName + "\', "

            print("Enter the SpiderPerson MissionLogs: ")
            MissionLogs = input()
            if "NULL" not in MissionLogs:
                query += "MissionLogs = \'" + MissionLogs + "\', "

            print("Enter the SpiderPerson Gender: ")
            Gender = input()
            if "NULL" not in Gender:
                query += "Gender = \'" + Gender + "\'"

        case "Villain":
            print("Enter the VillainID: ")
            VillainID = input()
            if "NULL" not in VillainID:
                query += "VillainIdentifier = " + VillainID + ", "
            
            print("Enter the Villain RealName: ")
            VillainName = input()
            if "NULL" not in VillainName:
                query += "RealName = \'" + VillainName + "\', "
            
            print("Enter the Villain Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "
            
            print("Enter the Villain Alias: ")
            Alias = input()
            if "NULL" not in Alias:
                query += "VillainName = \'" + Alias + "\', "
            
            print("Enter the Threat Level for the Villain: ")
            ThreatLevel = input()
            if "NULL" not in ThreatLevel:
                query += "ThreatLevel = " + ThreatLevel + ", "
            
            print("Enter the Villain Gender: ")
            Gender = input()
            if "NULL" not in Gender:
                query += "Gender = \'" + Gender + "\'"
            
        case "Mission":
            print("Enter the Mission Title: ")
            MissionTitle = input()
            if "NULL" not in MissionTitle:
                query += "Title = \'" + MissionTitle + "\', "
            
            print("Enter the Mission Objective: ")
            MissionObjective = input()
            if "NULL" not in MissionObjective:
                query += "Objectives = \'" + MissionObjective + "\', "
            
            print("Enter the Mission Resources Expended: ")
            MissionResourcesCost = input()
            if "NULL" not in MissionResourcesCost:
                query += "ResourcesUsed = \'" + MissionResourcesCost + "\', "
            
            print("Enter the Mission Outcome: ")
            MissionOutcome = input()
            if "NULL" not in MissionOutcome:
                query += "Outcome = \'" + MissionOutcome + "\', "
            
            print("Enter the Mission Location Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID 
       
        case "Organization":
            print("Enter the Organization ID: ")
            OrganizationID = input()
            if "NULL" not in OrganizationID:
                query += "OrganizationIdentifier = " + OrganizationID + ", "
            
            print("Enter the Organization Name: ")
            OrganizationName = input()
            if "NULL" not in OrganizationName:
                query += "Name = \'" + OrganizationName + "\', "
            
            print("Enter the Organization Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "
            
            print("Enter the Organization Time of Establishment (YYYY-MM-DD): ")
            TimeOfEstablishment = input()
            if "NULL" not in TimeOfEstablishment:
                query += "TimeOfEstablishment = \'" + TimeOfEstablishment + "\', "
            
            print("Enter the Organization Objectives: ")
            Objectives = input()
            if "NULL" not in Objectives:
                query += "Objectives = \'" + Objectives + "\', "
            
            print("Enter the Organization HQ-Location: ")
            Location = input()
            if "NULL" not in Location:
                query += "HeadquartersLocation = \'" + Location + "\', "
            
            print("Enter the Organization Logo (ID): ")
            Logo = input()
            if "NULL" not in Logo:
                query += "Logo = " + Logo 
        
        case "SideCharacter":
            print("Enter the SideCharacter ID: ")
            SideCharacterID = input()
            if "NULL" not in SideCharacterID:
                query += "CharacterIdentifier = " + SideCharacterID + ", "
            
            print("Enter the SideCharacter Name: ")
            SideCharacterName = input()
            if "NULL" not in SideCharacterName:
                query += "Name = \'" + SideCharacterName + "\', "
            
            print("Enter the SideCharacter Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "
            
            print("Enter the SideCharacter Alias: ")
            Alias = input()
            if "NULL" not in Alias:
                query += "MaskName = \'" + Alias + "\', "
            
            print("Enter the SideCharacter Gender: ")
            Gender = input()
            if "NULL" not in Gender:
                query += "Gender = \'" + Gender + "\'"            

        case "ResearchNotes":
            print("Enter the ResearchNotes Date (DD|MM|YYYY): ")
            Date = input()
            if "NULL" not in Date:
                query += "Date = " + Date + ", "
            
            print("Enter the ResearchNotes Title: ")
            Title = input()
            if "NULL" not in Title:
                query += "Topic = \'" + Title + "\', "
            
            print("Enter the ResearchNotes Content: ")
            Content = input()
            if "NULL" not in Content:
                query += "Content = \'" + Content + "\'"
                        
        case "Equipment":
            print("Enter the Equipment Name: ")
            EquipmentName = input()
            if "NULL" not in EquipmentName:
                query += "Name = \'" + EquipmentName + "\', "
            
            print("Enter the Equipment Type: ")
            EquipmentType = input()
            if "NULL" not in EquipmentType:
                query += "Type = \'" + EquipmentType + "\', "
            
            print("Enter the Equipment Description: ")
            EquipmentDescription = input()
            if "NULL" not in EquipmentDescription:
                query += "Description = \'" + EquipmentDescription + "\'"
            
        case "AbilitiesSpiderPerson":
            print("Enter the Corresponding SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID + ", "
            
            print("Enter the Ability Name: ")
            AbilityName = input()
            if "NULL" not in AbilityName:
                query += "Ability = \'" + AbilityName + "\'" 
        
        case "AbilitiesVillain":    
            print("Enter the Corresponding Villain ID: ")
            VillainID = input()
            if "NULL" not in VillainID:
                query += "VillainIdentifier = " + VillainID + ", "
            
            print("Enter the Ability Name: ")
            AbilityName = input()
            if "NULL" not in AbilityName:
                query += "Ability = \'" + AbilityName + "\'"
        
        case "AbilitiesSideChar":
            print("Enter the Corresponding SideCharacter ID: ")
            SideCharacterID = input()
            if "NULL" not in SideCharacterID:
                query += "CharacterIdentifier = " + SideCharacterID + ", "
            
            print("Enter the Ability Name: ")
            AbilityName = input()
            if "NULL" not in AbilityName:
                query += "Ability = \'" + AbilityName + "\'"
        
        # Relationship Tables
        case "Mentors":
            print("Enter the Student SpiderPerson ID: ")
            StudentID = input()
            if "NULL" not in StudentID:
                query += "SpiderPersonSpiderIdentifier = " + StudentID + ", "
            
            print("Enter the Mentor SpiderPerson ID: ")
            MentorID = input()
            if "NULL" not in MentorID:
                query += "MentorSpiderIdentifier = " + MentorID
            
        case "FacesOffAgainst":
            print("Enter the Villain ID: ")
            VillainID = input()
            if "NULL" not in VillainID:
                query += "VillainVillainIdentifier = " + VillainID + ", "
            
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID

        case "Owns":
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID + ", "
            
            print("Enter the Equipment Name: ")
            EquipmentName = input()
            if "NULL" not in EquipmentName:
                query += "Equipment = \'" + EquipmentName + "\'"
            
        case "HeadsMission":
            print("Enter the Mission Title: ")
            MissionTitle = input()
            if "NULL" not in MissionTitle:
                query += "MissionTitle = \'" + MissionTitle + "\', "
            
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID
            
        case "MemberOf":
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID + ", "
            
            print("Enter the Organization ID: ")
            OrganizationID = input()
            if "NULL" not in OrganizationID:
                query += "OrganizationOrganizationIdentifier = " + OrganizationID

        case "AssociatesWith":
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID + ", "
            
            print("Enter the SideCharacter ID: ")
            SideCharacterID = input()
            if "NULL" not in SideCharacterID:
                query += "SideCharacterCharacterIdentifier = " + SideCharacterID
            
        case "Hypothesis":
            print("Enter the ResearchNotes Title: ")
            ResearchNotesTitle = input()
            if "NULL" not in ResearchNotesTitle:
                query += "ResearchNote= \'" + ResearchNotesTitle + "\', "
            
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderIdentifier = " + SpiderPersonID
        
        case "Participant":
            print("Enter the Mission Title: ")
            MissionTitle = input()
            if "NULL" not in MissionTitle:
                query += "MissionTitle = \'" + MissionTitle + "\', "
            
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            if "NULL" not in SpiderPersonID:
                query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID
            
        case _:
            print("Invalid table name")
            return -1
    
    query += ";"
    # print(query) # debug statement
    # execute the query
    try:
        c.execute(query)
        return 0
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1

def HandleUpdate():
    global c
    print("Available tables: ")
    print("----Entity Tables----")
    print("1. SpiderPerson")
    print("2. Villain")
    print("3. Mission")
    print("4. Organization")
    print("5. SideCharacter")
    print("6. ResearchNotes")
    print("7. Equipment")
    print("8. AbilitiesSpiderPerson")
    print("9. AbilitiesVillain")
    print("10. AbilitiesSideChar")

    print("\nNOTE: Enter NULL for any field that is not applicable (for autoincrement fields)\n")

    print("Enter the table name: ")
    table = input()
    if table == "exit":
        return 0

    query = "UPDATE " + table
    query += " SET "

    match table:
        # Entity Tables
        case "SpiderPerson":
            print("Enter the SpiderPersonID to be Updated: ")
            while 1:
                SpiderPersonID = input()
                try:
                    SpiderPersonID = int(SpiderPersonID)
                    SpiderPersonID = str(SpiderPersonID)
                    break
                except:
                    print("Please enter a valid integer.")
            
            print("\nEnter Modified Values:\n")
            
            print("Enter the SpiderPerson RealName: ")
            SpiderPersonName = input()
            if "NULL" not in SpiderPersonName:
                query += "RealName = \'" + SpiderPersonName + "\', "

            print("Enter the SpiderPerson Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "

            print("Enter the SpiderPerson HeroName: ")
            HeroName = input()
            if "NULL" not in HeroName:
                query += "HeroName = \'" + HeroName + "\', "

            print("Enter the SpiderPerson MissionLogs: ")
            MissionLogs = input()
            if "NULL" not in MissionLogs:
                query += "MissionLogs = \'" + MissionLogs + "\', "

            print("Enter the SpiderPerson Gender: ")
            Gender = input()
            if "NULL" not in Gender:
                query += "Gender = \'" + Gender + "\' "
                 
            query += "WHERE SpiderIdentifier = " + SpiderPersonID
            
        case "Villain":
            print("Enter the VillainID to be Updated: ")
            while 1:
                VillainID = input()
                try:
                    VillainID = int(VillainID)
                    VillainID = str(VillainID)
                    break
                except:
                    print("Please enter a valid integer.")
                    
            print("\nEnter Modified Values:\n")
            
            print("Enter the Villain RealName: ")
            VillainName = input()
            if "NULL" not in VillainName:
                query += "RealName = \'" + VillainName + "\', "
            
            print("Enter the Villain Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "
            
            print("Enter the Villain Alias: ")
            Alias = input()
            if "NULL" not in Alias:
                query += "VillainName = \'" + Alias + "\', "
            
            print("Enter the Threat Level for the Villain: ")
            ThreatLevel = input()
            if "NULL" not in ThreatLevel:
                query += "ThreatLevel = " + ThreatLevel + ", "
            
            print("Enter the Villain Gender: ")
            Gender = input()
            if "NULL" not in Gender:
                query += "Gender = \'" + Gender + "\' "
                
            query += "WHERE VillainIdentifier = " + VillainID
            
        case "Mission":
            print("Enter the Mission Title to be Updated: ")
            MissionTitle = input()
            while 1:
                try:
                    MissionTitle = int(MissionTitle)
                    MissionTitle = str(MissionTitle)
                    break
                except:
                    print("Please enter a valid integer.")
            
            print("\nEnter Modified Values:\n")                
            
            print("Enter the Mission Objective: ")
            MissionObjective = input()
            if "NULL" not in MissionObjective:
                query += "Objectives = \'" + MissionObjective + "\', "
            
            print("Enter the Mission Resources Expended: ")
            MissionResourcesCost = input()
            if "NULL" not in MissionResourcesCost:
                query += "ResourcesUsed = \'" + MissionResourcesCost + "\', "
            
            print("Enter the Mission Outcome: ")
            MissionOutcome = input()
            if "NULL" not in MissionOutcome:
                query += "Outcome = \'" + MissionOutcome + "\', "
            
            print("Enter the Mission Location Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID 
            
            query += "WHERE Title = \'" + MissionTitle + "\'"
       
        case "Organization":
            print("Enter the Organization ID to be Updated: ")
            while 1:
                OrganizationID = input()
                try:
                    OrganizationID = int(OrganizationID)
                    OrganizationID = str(OrganizationID)
                    break
                except:
                    print("Please enter a valid integer.")
                
            print("\nEnter Modified Values:\n")
            
            print("Enter the Organization Name: ")
            OrganizationName = input()
            if "NULL" not in OrganizationName:
                query += "Name = \'" + OrganizationName + "\', "
            
            print("Enter the Organization Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "
            
            print("Enter the Organization Time of Establishment (YYYY-MM-DD): ")
            TimeOfEstablishment = input()
            if "NULL" not in TimeOfEstablishment:
                query += "TimeOfEstablishment = \'" + TimeOfEstablishment + "\', "
            
            print("Enter the Organization Objectives: ")
            Objectives = input()
            if "NULL" not in Objectives:
                query += "Objectives = \'" + Objectives + "\', "
            
            print("Enter the Organization HQ-Location: ")
            Location = input()
            if "NULL" not in Location:
                query += "HeadquartersLocation = \'" + Location + "\', "
            
            print("Enter the Organization Logo (ID): ")
            Logo = input()
            if "NULL" not in Logo:
                query += "Logo = " + Logo 
            
            query += "WHERE OrganizationIdentifier = " + OrganizationID
        
        case "SideCharacter":
            print("Enter the SideCharacter ID to be Updated: ")
            while 1:
                SideCharacterID = input()
                try:
                    SideCharacterID = int(SideCharacterID)
                    SideCharacterID = str(SideCharacterID)
                    break
                except:
                    print("Please enter a valid integer.")
            
            print("Enter the SideCharacter Name: ")
            SideCharacterName = input()
            if "NULL" not in SideCharacterName:
                query += "Name = \'" + SideCharacterName + "\', "
            
            print("Enter the SideCharacter Dimension-ID: ")
            DimensionID = input()
            if "NULL" not in DimensionID:
                query += "DimensionID = " + DimensionID + ", "
            
            print("Enter the SideCharacter Alias: ")
            Alias = input()
            if "NULL" not in Alias:
                query += "MaskName = \'" + Alias + "\', "
            
            print("Enter the SideCharacter Gender: ")
            Gender = input()
            if "NULL" not in Gender:
                query += "Gender = \'" + Gender + "\'"     
            
            query += "WHERE CharacterIdentifier = " + SideCharacterID       

        case "ResearchNotes":
            print("Enter the ResearchNotes Title to be Updated: ")
            ResearchNotesTitle = input()                
            
            print("Enter the ResearchNotes Date (DD|MM|YYYY): ")
            Date = input()
            if "NULL" not in Date:
                query += "Date = " + Date + ", "
            
            print("Enter the ResearchNotes Content: ")
            Content = input()
            if "NULL" not in Content:
                query += "Content = \'" + Content + "\'"
            
            query += "WHERE Topic = \'" + ResearchNotesTitle + "\'"
                        
        case "Equipment":
            print("Enter the Equipment Name: ")
            EquipmentName = input()
            
            print("Enter the Equipment Type: ")
            EquipmentType = input()
            if "NULL" not in EquipmentType:
                query += "Type = \'" + EquipmentType + "\', "
            
            print("Enter the Equipment Description: ")
            EquipmentDescription = input()
            if "NULL" not in EquipmentDescription:
                query += "Description = \'" + EquipmentDescription + "\'"
                
            query += "WHERE Name = \'" + EquipmentName + "\'"
            
        case "AbilitiesSpiderPerson":
            print("Enter the Corresponding SpiderPerson ID: ")
            SpiderPersonID = input()
            while 1:
                try:
                    SpiderPersonID = int(SpiderPersonID)
                    break
                except:
                    print("Please enter a valid integer.")
            
            print("Enter the Ability Name: ")
            AbilityName = input()
            if "NULL" not in AbilityName:
                query += "Ability = \'" + AbilityName + "\'" 
            
            query += "WHERE SpiderPersonSpiderIdentifier = " + SpiderPersonID
        
        case "AbilitiesVillain":    
            print("Enter the Corresponding Villain ID: ")
            VillainID = input()
            while 1:
                try:
                    VillainID = int(VillainID)
                    break
                except:
                    print("Please enter a valid integer.")
            
            print("Enter the Ability Name: ")
            AbilityName = input()
            if "NULL" not in AbilityName:
                query += "Ability = \'" + AbilityName + "\'"
            
            query += "WHERE VillainIdentifier = " + VillainID
        
        case "AbilitiesSideChar":
            print("Enter the Corresponding SideCharacter ID: ")
            SideCharacterID = input()
            while 1:
                try:
                    SideCharacterID = int(SideCharacterID)
                    break
                except:
                    print("Please enter a valid integer.")
        
            print("Enter the Ability Name: ")
            AbilityName = input()
            if "NULL" not in AbilityName:
                query += "Ability = \'" + AbilityName + "\'"
            
            query += "WHERE CharacterIdentifier = " + SideCharacterID
        
        case _:
            print("Invalid table name")
            return -1
    
    query += ";"
    # print(query) # debug statement
    # execute the query
    try:
        c.execute(query)
        return 0
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1

def HandleDelete():
    global c
    print("Available tables: ")
    print("----Entity Tables----")
    print("1. SpiderPerson")
    print("2. Villain")
    print("3. Mission")
    print("4. Organization")
    print("5. SideCharacter")
    print("6. ResearchNotes")
    print("7. Equipment")
    print("8. AbilitiesSpiderPerson")
    print("9. AbilitiesVillain")
    print("10. AbilitiesSideChar")

    print("\nEnter the Corresponding Primary Key for the table for deletion in each table\n")
    '''
    print("----Relationship Tables----")
    print("1. Mentors")
    print("2. FacesOffAgainst")
    print("3. Owns")
    print("4. HeadsMission")
    print("5. MemberOf")
    print("6. AssociatesWith")
    print("7. Hypothesis")
    print("8. Participant")
    print("\nNOTE: Enter NULL for any field that is not applicable (for autoincrement fields)\n")
    '''

    print("Enter the table name: ")
    table = input()
    if table == "exit":
        return 0

    query = "DELETE FROM " + table
    query += " WHERE "

    match table:
        # Entity Tables
        case "SpiderPerson":
            print("Enter the SpiderPersonID: ")
            SpiderPersonID = input()

            query += "SpiderIdentifier = " + SpiderPersonID
        
        case "Villain":
            print("Enter the VillainID: ")
            VillainID = input()

            query += "VillainIdentifier = " + VillainID
        
        case "Mission":
            print("Enter the Mission Title: ")
            MissionTitle = input()

            query += "Title = \'" + MissionTitle + "\'"

        case "Organization":
            print("Enter the Organization ID: ")
            OrganizationID = input()

            query += "OrganizationIdentifier = " + OrganizationID
        
        case "SideCharacter":
            print("Enter the SideCharacter ID: ")
            SideCharacterID = input()

            query += "CharacterIdentifier = " + SideCharacterID
        
        case "ResearchNotes":
            print("Enter the ResearchNotes Topic: ")
            ResearchNotesTopic = input()

            query += "Topic = \'" + ResearchNotesTopic + "\'"
        
        case "Equipment":
            print("Enter the Equipment Name: ")
            EquipmentName = input()

            query += "Name = \'" + EquipmentName + "\'"
        
        case "AbilitiesSpiderPerson":
            print("Enter the Corresponding SpiderPerson ID: ")
            SpiderPersonID = input()

            query += "SpiderPersonSpiderIdentifier = " + SpiderPersonID
        
        case "AbilitiesVillain":
            print("Enter the Corresponding Villain ID: ")
            VillainID = input()

            query += "VillainIdentifier = " + VillainID
        
        case "AbilitiesSideChar":
            print("Enter the Corresponding SideCharacter ID: ")
            SideCharacterID = input()

            query += "CharacterIdentifier = " + SideCharacterID

        # Relationship Tables DELETE CASACADE

    # execute the query
    try:
        c.execute(query)
        return 0
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1

def HandleProjection():
    global c
    print("Choose Among following Projection Options: ")
    print("1. SpiderPerson and Associated Villains and SideCharacters ")
    print("2. SpiderPerson and Abilities ")
    print("3. Villain and Abilities ")
    print("4. SideCharacter and Abilities ")
    print("5. SpiderPerson and Associated Equipment ")
    print("6. SpiderPerson and Associated Missions ")

    print("\nEnter your choice: ")
    choice = input()
    while True:
        try:
            choice = int(choice)
            break
        except:
            print("Please enter a valid integer.")
    
    match choice:
        case 1:
            print("----------SpiderPerson and Associated Villains and SideCharacters----------")
            query = '''SELECT SpiderPerson.SpiderIdentifier, SpiderPerson.RealName, SpiderPerson.HeroName, Villain.VillainIdentifier, Villain.RealName, SideCharacter.CharacterIdentifier, SideCharacter.Name 
                       FROM SpiderPerson LEFT JOIN FacesOffAgainst ON SpiderPerson.SpiderIdentifier = FacesOffAgainst.SpiderPersonSpiderIdentifier 
                       LEFT JOIN Villain ON FacesOffAgainst.VillainVillainIdentifier = Villain.VillainIdentifier 
                       LEFT JOIN AssociatesWith ON SpiderPerson.SpiderIdentifier = AssociatesWith.SpiderPersonSpiderIdentifier 
                       LEFT JOIN SideCharacter ON AssociatesWith.SideCharacterCharacterIdentifier = SideCharacter.CharacterIdentifier;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1

            # print the result
            print("SpiderPersonID\tRealName\tHeroName\tVillainID\tVillainName\tSideCharacterID\tSideCharacterName")
            for row in c.fetchall():
                print(row["SpiderIdentifier"], "\t", row["RealName"], "\t", row["HeroName"], "\t", row["VillainIdentifier"], "\t", row["RealName"], "\t", row["CharacterIdentifier"], "\t", row["Name"])
            
            return 0

        case 2:
            print("----------SpiderPerson and Abilities----------")
            query = '''SELECT SpiderPerson.SpiderIdentifier, SpiderPerson.RealName, SpiderPerson.HeroName, AbilitiesSpiderPerson.Ability
                        FROM SpiderPerson LEFT JOIN AbilitiesSpiderPerson ON SpiderPerson.SpiderIdentifier = AbilitiesSpiderPerson.SpiderPersonSpiderIdentifier;''' 

            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("SpiderPersonID\tRealName\tHeroName\tAbility")
            for row in c.fetchall():
                print(row["SpiderIdentifier"], "\t", row["RealName"], "\t", row["HeroName"], "\t", row["Ability"])
            
            return 0
        
        case 3:
            print("----------Villain and Abilities----------")
            query = '''SELECT Villain.VillainIdentifier, Villain.RealName, Villain.VillainName, AbilitiesVillain.Ability
                        FROM Villain LEFT JOIN AbilitiesVillain ON Villain.VillainIdentifier = AbilitiesVillain.VillainIdentifier;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("VillainID\tRealName\tVillainName\tAbility")
            for row in c.fetchall():
                print(row["VillainIdentifier"], "\t", row["RealName"], "\t", row["VillainName"], "\t", row["Ability"])

            return 0
        
        case 4:
            print("----------SideCharacter and Abilities----------")
            query = '''SELECT SideCharacter.CharacterIdentifier, SideCharacter.Name, SideCharacter.MaskName, AbilitiesSideChar.Ability
                        FROM SideCharacter LEFT JOIN AbilitiesSideChar ON SideCharacter.CharacterIdentifier = AbilitiesSideChar.CharacterIdentifier;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("SideCharacterID\tName\tAlias\tAbility")
            for row in c.fetchall():
                print(row["CharacterIdentifier"], "\t", row["Name"], "\t", row["MaskName"], "\t", row["Ability"])

            return 0
        
        case 5:
            print("----------SpiderPerson and Associated Equipment----------")
            query = '''SELECT SpiderPerson.SpiderIdentifier, SpiderPerson.RealName, SpiderPerson.HeroName, Equipment.Name
                        FROM SpiderPerson LEFT JOIN Owns ON SpiderPerson.SpiderIdentifier = Owns.SpiderPersonSpiderIdentifier
                        LEFT JOIN Equipment ON Owns.Equipment = Equipment.Name;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("SpiderPersonID\tRealName\tHeroName\tEquipment")
            for row in c.fetchall():
                print(row["SpiderIdentifier"], "\t", row["RealName"], "\t", row["HeroName"], "\t", row["Name"])
            
            return 0
        
        case 6:
            print("----------SpiderPerson and Associated Missions----------")
            query = '''SELECT SpiderPerson.SpiderIdentifier, SpiderPerson.RealName, SpiderPerson.HeroName, Mission.Title
                        FROM SpiderPerson LEFT JOIN Participant ON SpiderPerson.SpiderIdentifier = Participant.SpiderPersonSpiderIdentifier
                        LEFT JOIN Mission ON Participant.MissionTitle = Mission.Title;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("SpiderPersonID\tRealName\tHeroName\tMissionTitle")
            for row in c.fetchall():
                print(row["SpiderIdentifier"], "\t", row["RealName"], "\t", row["HeroName"], "\t", row["Title"])

            return 0
    
        case _:
            print("Invalid choice")
            return -1

def HandleAggregate():
    global c

    print("Choose Among following Aggregate Options: ")
    print("1. Average Threat Level of Villains ")
    print("2. Total Number of Missions (Grouped by Outcome) ")
    print("3. Number of SpiderPersons and Villains in each Dimension ")
    print("4. Total Equipment used by each SpiderPersons ")

    print("\nEnter your choice: ")
    choice = input()
    while True:
        try:
            choice = int(choice)
            break
        except:
            print("Please enter a valid integer.")
    
    match choice:
        case 1:
            print("----------Average Threat Level of Villains----------")
            query = '''SELECT AVG(ThreatLevel) AS T_L FROM Villain;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            for row in c.fetchall():
                print(row["T_L"])
            
            return 0

        case 2:
            print("----------Total Number of Missions (Grouped by Outcome)----------")
            query = '''SELECT Outcome, COUNT(*) AS C FROM Mission GROUP BY Outcome;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("Outcome\tCount")
            
            for row in c.fetchall():
                print(row["Outcome"], "\t", row["C"])
            
            return 0
        
        case 3:
            print("----------Number of SpiderPersons and Villains in each Dimension----------")
            query = '''SELECT SpiderPerson.DimensionID, COUNT(*) AS C FROM SpiderPerson GROUP BY DimensionID;'''

            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("----------SpiderPersons----------")
            print("DimensionID\tCount")
            for row in c.fetchall():
                print(row["DimensionID"], "\t", row["C"])
            
            query = '''SELECT Villain.DimensionID, COUNT(*) AS C FROM Villain GROUP BY DimensionID;'''

            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            print("----------Villains----------")
            print("DimensionID\tCount")
            # print the result
            for row in c.fetchall():
                print(row["DimensionID"], "\t", row["C"])
            
            return 0
        
        case 4:
            print("----------Total Equipment used by each SpiderPersons----------")
            query = '''SELECT SpiderPerson.SpiderIdentifier, SpiderPerson.RealName, SpiderPerson.HeroName, COUNT(*) FROM SpiderPerson LEFT JOIN Owns ON SpiderPerson.SpiderIdentifier = Owns.SpiderPersonSpiderIdentifier GROUP BY SpiderPerson.SpiderIdentifier;'''

            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("ID\tReal Name\tHero Name\tCount")
            for row in c.fetchall():
                print(row["SpiderIdentifier"], "\t", row["RealName"], "\t", row["HeroName"], "\t", row["COUNT(*)"])
            
            return 0
        
        case _:
            print("Invalid choice")
            return -1
        
        
def HandleSearch():
    global c
    
    print("Choose Among following Search Options: ")
    print("1. Search for Villains of SpiderPerson (by ID)")
    print("2. Search for Mission assigned to SpiderPerson (by ID)")
    print("3. Search for Equipment used by SpiderPerson (by ID)")
    print("4. Search for ResearchNotes written by SpiderPerson (by ID)")
    print("5. Search for Members of Organization (by ID)")


    print("\nEnter your choice: ")
    choice = input()
    while True:
        try:
            choice = int(choice)
            break
        except:
            print("Please enter a valid integer.")
    
    match choice:
        case 1:
            print("----------Search for Villains of SpiderPerson (by ID)----------")
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            query = '''SELECT Villain.VillainIdentifier, Villain.RealName, Villain.VillainName, Villain.ThreatLevel
                        FROM SpiderPerson LEFT JOIN FacesOffAgainst ON SpiderPerson.SpiderIdentifier = FacesOffAgainst.SpiderPersonSpiderIdentifier
                        LEFT JOIN Villain ON FacesOffAgainst.VillainVillainIdentifier = Villain.VillainIdentifier
                        WHERE SpiderPerson.SpiderIdentifier = ''' + SpiderPersonID + ";"
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            print("----------Villains----------\n")
            # print the result in a formatted way
            print("ID\tReal Name\tVillain Name\tThreat Level")
            for row in c.fetchall():
                print(row["VillainIdentifier"], "\t", row["RealName"], "\t", row["VillainName"], "\t", row["ThreatLevel"])
            
            return 0
        
        case 2:
            print("----------Search for Mission assigned to SpiderPerson (by ID)----------")
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            query = '''SELECT Mission.Title, Mission.Objectives, Mission.ResourcesUsed, Mission.Outcome
                        FROM SpiderPerson LEFT JOIN Participant ON SpiderPerson.SpiderIdentifier = Participant.SpiderPersonSpiderIdentifier
                        LEFT JOIN Mission ON Participant.MissionTitle = Mission.Title
                        WHERE SpiderPerson.SpiderIdentifier = ''' + SpiderPersonID + ";"
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            print("----------Missions----------")
            print("Title\tObjectives\tResources Used\tOutcome")
            # print the result
            for row in c.fetchall():
                print(row["Title"], "\t", row["Objectives"], "\t", row["ResourcesUsed"], "\t", row["Outcome"])

            return 0
        
        case 3:
            print("----------Search for Equipment used by SpiderPerson (by ID)----------")
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            query = '''SELECT Equipment.Name, Equipment.Type, Equipment.Description
                        FROM SpiderPerson LEFT JOIN Owns ON SpiderPerson.SpiderIdentifier = Owns.SpiderPersonSpiderIdentifier
                        LEFT JOIN Equipment ON Owns.Equipment = Equipment.Name
                        WHERE SpiderPerson.SpiderIdentifier = ''' + SpiderPersonID + ";"
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            print("----------Equipment----------")
            print("Name\tType\tDescription")
            # print the result
            for row in c.fetchall():
                print(row["Name"], "\t", row["Type"], "\t", row["Description"])

            return 0
        
        case 4:
            print("----------Search for ResearchNotes written by SpiderPerson (by ID)----------")
            print("Enter the SpiderPerson ID: ")
            SpiderPersonID = input()
            query = '''SELECT ResearchNotes.Date, ResearchNotes.Topic, ResearchNotes.Content
                        FROM SpiderPerson LEFT JOIN Hypothesis ON SpiderPerson.SpiderIdentifier = Hypothesis.SpiderIdentifier
                        LEFT JOIN ResearchNotes ON Hypothesis.ResearchNote = ResearchNotes.Topic
                        WHERE SpiderPerson.SpiderIdentifier = ''' + SpiderPersonID + ";"
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            print("----------ResearchNotes----------")
            print("Date\tTopic\tContent")
            # print the result
            for row in c.fetchall():
                print(row["Date"], "\t", row["Topic"], "\t", row["Content"])

            return 0
        
        case 5:
            print("----------Search for Members of Organization (by ID)----------")
            print("Enter the Organization ID: ")
            OrganizationID = input()
            query = '''SELECT SpiderPerson.SpiderIdentifier, SpiderPerson.RealName, SpiderPerson.HeroName
                        FROM Organization LEFT JOIN MemberOf ON Organization.OrganizationIdentifier = MemberOf.OrganizationOrganizationIdentifier
                        LEFT JOIN SpiderPerson ON MemberOf.SpiderPersonSpiderIdentifier = SpiderPerson.SpiderIdentifier
                        WHERE Organization.OrganizationIdentifier = ''' + OrganizationID + ";"
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            print("----------Members----------")
            print("ID\tReal Name\tHero Name")
            # print the result
            for row in c.fetchall():
                print(row["SpiderIdentifier"], "\t", row["RealName"], "\t", row["HeroName"])

            return 0
        
        case _:
            print("Invalid choice")
            return -1
        
def HandleAnalytical():
    global c
    
    print("Choose Among following Analytical Options: ")
    print("1. SpiderPerson Efficiency report ")
    print("2. Villain Opposition Network report ")
    print("3. Equipment Usage report ")

    print("\nEnter your choice: ")
    choice = input()
    while True:
        try:
            choice = int(choice)
            break
        except:
            print("Please enter a valid integer.")

    match choice:
        case 1:
            print("----------SpiderPerson Efficiency report----------")
            query = '''SELECT SpiderPerson.SpiderIdentifier, SpiderPerson.RealName, SpiderPerson.HeroName, COUNT(*) AS MissionsAssigned
                        FROM SpiderPerson LEFT JOIN Participant ON SpiderPerson.SpiderIdentifier = Participant.SpiderPersonSpiderIdentifier
                        LEFT JOIN Mission ON Participant.MissionTitle = Mission.Title
                        WHERE Mission.Outcome NOT IN ('unsuccessful', 'incomplete', 'Ongoing')
                        GROUP BY SpiderPerson.SpiderIdentifier;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
        
            # print the result
            print("ID\tReal Name\tHero Name\tMissions Assigned")
            for row in c.fetchall():
                print(row["SpiderIdentifier"], "\t", row["RealName"], "\t", row["HeroName"], "\t", row["MissionsAssigned"])
            
            return 0
        
        case 2:
            print("----------Villain Opposition Network report----------")
            query = '''SELECT Villain.VillainIdentifier, Villain.RealName, Villain.VillainName, COUNT(*) AS SpiderPersonsFacedOff, AbilitiesVillain.Ability AS Ability
                        FROM Villain LEFT JOIN FacesOffAgainst ON Villain.VillainIdentifier = FacesOffAgainst.VillainVillainIdentifier
                        LEFT JOIN AbilitiesVillain ON Villain.VillainIdentifier = AbilitiesVillain.VillainIdentifier
                        GROUP BY Villain.VillainIdentifier, AbilitiesVillain.Ability;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("ID\tReal Name\tVillain Name\tSpiderPersons FacedOff\tAbility")
            for row in c.fetchall():
                print(row["VillainIdentifier"], "\t", row["RealName"], "\t", row["VillainName"], "\t", row["SpiderPersonsFacedOff"], "\t", row["Ability"])

            return 0
        
        case 3:
            print("----------Equipment Usage report----------")
            query = '''SELECT Equipment.Name, Equipment.Type, COUNT(*) AS SpiderPersonsUsing
                        FROM Equipment LEFT JOIN Owns ON Equipment.Name = Owns.Equipment
                        GROUP BY Equipment.Name;'''
            
            try:
                c.execute(query)
            except pymysql.Error as e:
                print("An error occurred:", e.args[0])
                return -1
            
            # print the result
            print("Name\tType\tSpiderPersons Using")
            for row in c.fetchall():
                print(row["Name"], "\t", row["Type"], "\t", row["SpiderPersonsUsing"])

            return 0
        
        case _:
            print("Invalid choice")
            return -1
           
def HandleSelect():
    global c
    global conn
    global tmp
    
    tmp = sp.call('clear', shell=True)
    
    print("Available tables: ")
    print("----Entity Tables----")
    print("1. SpiderPerson")
    print("2. Villain")
    print("3. Mission")
    print("4. Organization")
    print("5. SideCharacter")
    print("6. ResearchNotes")
    print("7. Equipment")
    print("8. AbilitiesSpiderPerson")
    print("9. AbilitiesVillain")
    print("10. AbilitiesSideChar")

    print("----Relationship Tables----")
    print("1. Mentors")
    print("2. FacesOffAgainst")
    print("3. Owns")
    print("4. HeadsMission")
    print("5. MemberOf")
    print("6. AssociatesWith")
    print("7. Hypothesis")
    print("8. Participant")
    
    print("----External Tables----")
    print("1. Images")
    
    table = input("\nEnter the table name to select data from: ")
    if table == "Images":
        c.execute("SELECT * FROM Images")
        images = c.fetchall()
        
        for image in images:
            id = image['id']
            data = image['image']
            print(f"Image {id}:")
            display_image(data)
        
    else:
        PrintTableContents(table)           
        
def HandleChoice(choice):
    global c
    global conn
    match choice:
        case 1:
            print("----------Simple SQL query----------")
            print("Enter your query: ")
            query = input()
            if query == "exit":
                return 0

            # check if query is valid
            if query.split()[0].lower() != "select":
                print("Invalid query")
                return 0

            HandleSimpleSQL(query)
        case 2:
            print("----------Fetching Content of a table----------")
            HandleSelect()
        case 3:
            print("----------Insert Operation----------")
            HandleInsert()
            # conn.commit()
        case 4:
            print("----------Delete Operation----------")
            HandleDelete()
            # conn.commit()
        case 5:
            print("----------Update Operation----------")
            HandleUpdate()
        case 6:
            print("----------Projection Operation----------")
            HandleProjection()
        case 7:
            print("----------Aggregate Operation----------")
            HandleAggregate()
        case 8:
            print("----------Search Operation----------")
            HandleSearch()
        case 9:
            print("----------Analytical Operation----------")
            HandleAnalytical()
        case _:
            print("Invalid choice")
            return 0    
               
def main():
    global c
    global conn
    global tmp    
    
    tmp = sp.call('clear', shell=True)
    
    print("Enter the username: ")
    username = input()
    print("Enter the password: ")
    password = input()
    
    print("Trying to connect to the database...", end="")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        conn = pymysql.connect(
                            #   host='localhost',
                            #   port=30306,
                              user=username,
                              password=password,
                              db=DB,
                              autocommit=True,
                              cursorclass=pymysql.cursors.DictCursor
                              )
        tmp = sp.call('clear', shell=True)

        if(conn.open):
            print("Connected")
            c = conn.cursor()
        else:
            print("Failed to connect")
            print("Exiting...")
            exit(1)

        input("PRESS ENTER TO CONTINUE>")
        tmp = sp.call('clear', shell=True)
    
    except Exception as e:
        print("Exception occured:{}".format(e))
        
        print("Exiting...")
        exit(1)
        

    #Load Images from the Images folder into Images table in the database
    i = 1
    try:
        c.execute("CREATE TABLE IF NOT EXISTS Images (id INT, image LONGBLOB)")
        c.execute("DELETE FROM Images")
    except pymysql.Error as e:
        print("An error occurred:", e.args[0])
        return -1
        
    for filename in os.listdir("Images"):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            is_image_valid("Images/" + filename)
            with open("Images/" + filename, 'rb') as file:
                Ablob = file.read()
                if Ablob:
                     c.execute("INSERT INTO Images VALUES (%s, %s)", (i, Ablob))
                     i += 1 

    #Print the tables in the database
    print("----------Welcome to the Spiderverse Database----------")
    print("----------Tables in the database----------")    
    PrintTables() 


    while True:
        #take input from user
        print("\n----------Available Operations----------")
        print(" 1. Standard SQL query (Select, Insert, Update, Delete)")
        print(" 2. Fetching Content of a table")
        print(" 3. Insertion Operation")
        print(" 4. Delete Operation")
        print(" 5. Update Operation")
        print(" 6. Projection Operation")
        print(" 7. Aggregate Operation")
        print(" 8. Search Operation")
        print(" 9. Analytical Operation")
        print("-------------------------------------------")

        while True:
            choice = input("\nEnter your choice: ")
            
            try:
                choice = int(choice)
                break
            except:
                print("Please enter a valid integer.")

        HandleChoice(choice)
        Continue = input("Do you want to continue? (Y/N): ")
        tmp = sp.call('clear', shell=True)
        if Continue == "Y" or Continue == "y":
            continue

        break

    print("----------Thank you for using the Spiderverse Database----------")
    conn.commit()
    c.close()
    conn.close()
    return 0

if __name__ == "__main__":
    main()