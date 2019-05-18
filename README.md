#Dataset Creator
This script uses the faker python library and therefore to use it you will need to install it

##Docs
This script generates random data according to user preference
###How-to-use
->python3 data_generator.py {SOURCE} {DEST} {SIZE} {DELIMITER} {PARAMETERS}

SOURCE: This is an optional parameters that parses 2 parameters out of a csv file into a list with no repetitions, write 'none' you don't want this option enabled
   Example Source:
        Grand Canyon National Park,Arizona
        Bryce Canyon National Park,Utah
        
->DEST: Specifies the target path for the created file

->SIZE: Specifies the number of users created

->DELIMITER: Specifies the delimiter between parameters

->PARAMETERS: Specifies which parameters the wants to create

--> Currently Supported:

    username
    password
    name
    address
    bdate_day
    bdate_month
    bdate_year
    locals (Requires {SOURCE}) - prints 3 elements of {SOURCE}[0] + None
    pdis (Requires {SOURCE}) - prints 1 to 5 elements of the {SOURCE}[1] list

### Sample uses
USAGE

python3 data_generatorV2.py '/home/user/Documents/US.txt' '/home/tld/Documents/output.txt' 10 username,password,name,address,bdate_day,bdate_month,bdate_year,locals,pdis

OUTPUT

april31,YjZhxRxnbmtaOVc,Colleen Gonzalez,157 Michael Causeway Apt. 134 East Dorothybury AR 63287,10,30,1971,Florida,California,None,Disneyland Park,Grand Canyon National Park,Monument Valley,Grand Canyon National Park

(...)

USAGE

python3 data_generator.py None '/home/user/Documents/test3.txt' 5 - address,name,password,username,bdate_day,bdate_month,bdate_year

OUTPUT

71703 Walter Mountains Apt. 618 Stephanieton KY 59042-Douglas Trevino-vmhXzAAElzbhZz-lisa42-02-19-2000

(...)
