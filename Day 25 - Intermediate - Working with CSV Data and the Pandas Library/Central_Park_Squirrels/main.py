import pandas

file_loc = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
data = pandas.read_csv(file_loc)
my_findings_dict ={
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [len(data[data['Primary Fur Color'] == 'Gray']), len(data[data['Primary Fur Color'] == 'Cinnamon']), len(data[data['Primary Fur Color'] == 'Black'])]
}
print(my_findings_dict)
new_data = pandas.DataFrame(my_findings_dict)
new_data.to_csv('my_findings.csv')
