import csv

Time=[]
X=[]
Y=[]
Z=[]
Time1=[]
counter=0
counter1=0
with open('Both_vehicle_dynamic_different_lane.csv', 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Time", "X","Y","Z", "Lane_Type", "Possible_Lane_Change","Vehicle","Type Of Scenario","X1","Y1","Z1", "Lane_Type1", "Possible_Lane_Change1","Vehicle1","Type Of Scenario1"])

        with open('Manual_control_datas.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[0]!= 'No':
                    X=float(row[1])
                    #print(type(X))
                    #print(row[1])
                    with open('Autopilot.csv') as csvfile:
                        readCSV1 = csv.reader(csvfile, delimiter=',')
                        for row1 in readCSV1:
                            if row1[0]!= 'No':
                                if round(float(row[1]),5)==round(float(row1[1]),5):
                                    #print('ok')
                                    #print(row[0],row[1],row[2])
                                    #print(row1[0],row1[1],row1[2])
                                    counter+=1
                                    counter1+=1
                                    writer.writerow([counter1, str(row[1]), str(row[2]),str(row[3]),str(row[4]), str(row[5]), str(row[6]),str("Manual"),str("Autopilot_stationary_with_wait_time"), str(row1[2]),str(row1[3]),str(row1[4]), str(row1[5]), str(row1[6]),str("Autopilot"),str("Autopilot_stationary_with_wait_time")])
                                    if counter>=1:
                                        print(counter1)
                                        break
                            else:
                                pass
                else:
                    pass
                counter=0
