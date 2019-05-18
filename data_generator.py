from faker import Faker
import random
import csv
import time
import sys
fake = Faker()
def US_parser(path):
    locations= ['None']
    pdis = []
    with open(path, "r") as csv_file:
        csv_content = csv.reader(csv_file, delimiter= ',')
        for line in csv_content:
            if line[0] not in pdis:
                pdis.append(line[0])
            if line[1] not in locations:
                locations.append(line[1])
    return locations,pdis

def generate_phone_number():
    return random.randint(900000000,1000000000)
def randomDate(start, end,format, prop):
    #Return 3 parameters day, month and year, in a list
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime)).split('/')

def data_generator(US,destination,size, delimiter, format):
    format = format.split(',')
    if US != 'None':
        locals,pdis = US_parser(US)
    final = []
    for i in range(int(size)):
        date = randomDate("1/1/1950", "1/1/2015",'%m/%d/%Y', random.random())
        k = l = 0
        temp = []
        password = fake.pystr(min_chars = 7)
        profile = fake.profile()
        profile['password'] = password
        profile['bdate_day'] = str(date[0])
        profile['bdate_month'] = str(date[1])
        profile['bdate_year'] = str(date[2])
        profile['address'] = profile['address'].replace('\n', ' ').replace(',','')
        profile['phone'] = str(generate_phone_number())
        if US != 'None':
            profile['locals'] = [random.choice(locals) for k in range(3)]
            profile['pdis'] = [random.choice(pdis) for l in range(1,5)]
        for param in format:
            if param =='None':
                continue
            elif param == 'locals':
                if US != 'None':
                    for local in profile['locals']:
                        temp.append(local)
                else:
                    continue
            elif param == 'pdis':
                if US != 'None':
                    for pdi in profile['pdis']:
                        temp.append(pdi)
                else:
                    continue
            else:
                temp.append(profile[param])

        final.append(temp)
    with open(destination,'w+') as f:
        for line in final:
            f.write(delimiter.join(line) + '\n')
    print("Sucess")

if __name__ == "__main__":
    data_generator(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4], sys.argv[5])
