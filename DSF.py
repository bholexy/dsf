import csv

def slcsp():
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

        print("=================================" + " Zip Code: " + slcsp_zip_col + "========================================")
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
                        plan_rate = "%0.2f" % float(plan_row[3])
                        silver_plan_rates.append(plan_rate)
                        plan_id = plan_row[0]
                        state = plan_row[1]
                        metal_level = plan_row[2]
                        rate = plan_row[3]
                        rate_area = plan_row[4]


                        print(silver_plan_rates)
                        print(f'\t Plan ID: ' + plan_id + "\t State: " + state + "\t Metal Level: " + metal_level + "\t Rate:" + rate + "\t Rate Area:" + rate_area) 
                        if len(silver_plan_rates) > 1:
                            silver_plan_rates.sort()
                            slcsp_rate_col = silver_plan_rates[1]
                            print(type(silver_plan_rates[1]))
                            print(f"\t SLCSP found for " + plan_id )
                            print(silver_plan_rates)
                      
        with open('new_slcsp.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([slcsp_zip_col, slcsp_rate_col])
    print("Script Ran Successfully")


slcsp()