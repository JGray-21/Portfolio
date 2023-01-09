import csv

data = []
with open('files/insurance.csv', newline='') as csv_file:
    csv_dic = csv.DictReader(csv_file)
    for item in csv_dic:
        data.append(item)

#average age, insurance cost, number of children, and BMI
sum_age = 0
sum_cost = 0
sum_children = 0
sum_bmi = 0
count = 0

for item in data:
    sum_age += int(item['age'])
    sum_cost += float(item['charges'])
    sum_children += int(item['children'])
    sum_bmi += float(item['bmi'])
    count += 1

print('There are {} people in this data set.'.format(count))
print('The average age is {}.'.format(int(sum_age/count)))
print('The average number of children is {}.'.format(int(sum_children/count)))
print('The average BMI is {}.'.format(sum_bmi/count))
print('The average cost is {}.'.format(sum_cost/count))

#average cost (Smokers vs. Non-smokers)
smoker_count = 0
non_smoker_count = 0
sum_smoker_cost = 0
sum_non_smoker_cost = 0

for item in data:
    if item['smoker'] == 'yes':
        smoker_count += 1
        sum_smoker_cost += float(item['charges'])
    elif item['smoker'] == 'no':
        non_smoker_count += 1
        sum_non_smoker_cost += float(item['charges'])
        
print('The average cost for smokers is {}'.format(sum_smoker_cost/smoker_count))
print('The average cost for non smokers is {}.'.format(sum_non_smoker_cost/non_smoker_count))
#Population of each region