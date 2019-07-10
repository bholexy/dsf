# import csv

# with open('slcsp.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='=')
#     line_count = 0
#     for row in csv_reader:
#         # if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         # else:
#             print(f'\t{row[0]} works in the  department, and was born in .')
#         #     line_count += 1
#     print(f'Processed {line_count} lines.')

import csv




slcsp_reader = csv.reader(open("slcsp.csv"))

for slcsp_row in slcsp_reader:
    
    slcsp_zip_col = (slcsp_row[0])
    slcsp_rate_col = None
    if slcsp_zip_col == "zipcode":
        with open('new_slcsp.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['zipcode', 'rate'])
        csvFile.close()        
        continue

    print("=================================" + slcsp_zip_col + "========================================")
    zips_reader = csv.reader(open("zips.csv"))
    for zips_row in zips_reader:
        if zips_row[0] == slcsp_zip_col: 
            zips_zip_col = zips_row[0]
            plans_reader = csv.reader(open("plans.csv"))
            silver_plan_array = []
            silver_plan_rates = []
            for plan_row in plans_reader:
                plan_id_col_zip = plan_row[0][-5:]
                if plan_id_col_zip == zips_zip_col and plan_row[2] == "Silver":
                    plan_rate = plan_row[3]
                    silver_plan_rates.append(plan_rate)
                    plan_id = plan_row[0]
                    state = plan_row[1]
                    metal_level = plan_row[2]
                    rate = plan_row[3]
                    rate_area = plan_row[4]


                    print(silver_plan_rates)
                    print(f'\t \t Plan ID: ' + plan_id + "\t State: " + state + "\t Metal Level: " + metal_level + "\t Rate:" + rate + "\t Rate Area:" + rate_area) 
                    if len(silver_plan_rates) > 1:
                        silver_plan_rates.sort()
                        slcsp_rate_col = silver_plan_rates[0]
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^This is index 1")
                        print(silver_plan_rates)
                    # try:
                    #     slcsp_data = silver_plan[1]
                    #     slcsp_rate_col = rate
                    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^This is index 1")
                    # except IndexError:
                    #     flcsp_data = silver_plan[0]
                    #     slcsp_rate_col = None
                    #     print(silver_plan[0])
                    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ THIS IS INDEX 2")
    with open('new_slcsp.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([slcsp_zip_col, slcsp_rate_col])







p = "stressful"
print(p[-4:])





























# import csv


# slcsp_reader = csv.reader(open("slcsp.csv", 'r'))


# # if (slcsp_reader[0] == zips_reader[0]):
# while True:
#     slcsp_row = 
#     try:
#         zips_reader = csv.reader(open("zips.csv", 'r'))
#         slcsp_row = slcsp_reader.next()
#         zips_row = zips_reader.next()
#         equal = (slcsp_row[0] == zips_row[0])
#         print(zips_reader)
#     except StopIteration:
#         break


