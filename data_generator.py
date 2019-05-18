from faker import Faker
import random
import csv
import time
import sys
fake = Faker()
def additional_data_parser(path):
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

def generate_list_no_repetition(dataset, size):
    temp = []
    while(len(temp) < size):
        local = random.choice(dataset)
        if local not in temp:
            temp.append(local)
    return temp

def data_generator(path,destination,size, delimiter,allow_duplicates, format):
    format = format.split(',')
    if path != 'None':
        locals,pdis = additional_data_parser(path)
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
        if path != 'None':
            if int(allow_duplicates) == 0:
                profile['locals'] = generate_list_no_repetition(locals,3)
                profile['pdis'] = generate_list_no_repetition(pdis, random.randint(1,4))
            else:
                profile['locals'] = [random.choice(locals) for i in range(3)]
                profile['pdis'] = [random.choice(pdis) for i in range(random.randint(1,4))]

        for param in format:
            if param =='None':
                continue
            elif param == 'locals':
                if path != 'None':
                    for local in profile['locals']:
                        temp.append(local)
                else:
                    continue
            elif param == 'pdis':
                if path != 'None':
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
    data_generator(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4], sys.argv[5], sys.argv[6])
