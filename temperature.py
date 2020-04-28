cityTemp=open('C:\\Users\\91991\\2020\\python learning\\original.csv')



city,temp,units=cityTemp.readline().split(',')
prev_city=city
cityTemp.seek(0)
sum=0.0
count=0
avg_temp=0.0

for records in cityTemp:
    records=records.rstrip('\n')
    city,temp,units=records.split(',')
    
    
    if units=='C':
        temp=(float(temp)*1.8)+32
    
        
    if city!=prev_city:
        avg_temp= sum/count
        print(prev_city + "  " + str(round(avg_temp,2)))
        prev_city = city
        sum = 0.0
        count = 0
        avg_temp = 0.0
    sum += float(temp)
    count = count + 1
else:
    avg_temp=round(float(sum/count),2)
    print(prev_city + "  " + str(round(avg_temp,2)))
        
        
        
        
        
        
        
        
        
        
        
        
   
        
    


        
        
        
            

