# TODO GET TOTAL NUMBER OF MONTHS IN DATATSET
# TODO NET TOTAL AMOUNT OF PROFIT/LOSSES
# TODO GET AVERAGE OF CHANGES PROFIT LOSSES
# TODO GET GREATES INCREASE IN PROFIT
# TODO GET GREATEST DECREASE IN PROFIT
import csv
import os
# declare all global variables
totalValue: int = 0
totalLossesAmount: int = 0
totalProfitAmount: int = 0
greatestProfitValue: int = 0
greatestProfitMonth: str = ''
greatestLossValue: int = 0
greatestLossMonth: str = ''
csvPath = os.path.join('Resources', 'budget_data.csv')

def sumAmount(value: int):
    global totalValue
    totalValue += value

def findGreatestProfitAndLoss(before: list, after: list):
    global greatestProfitValue
    global greatestProfitMonth
    global greatestLossValue
    global greatestLossMonth
    beforeValue = int(before[1])
    afterValue = int(after[1])
    if (afterValue - beforeValue) > greatestProfitValue:
        greatestProfitValue = afterValue - beforeValue
        greatestProfitMonth = after[0]
    
    if (afterValue - beforeValue) < greatestLossValue:
        greatestLossValue = afterValue - beforeValue
        greatestLossMonth = before[0]
    

with open(csvPath) as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')
    # advance csv to skip header
    header = f'Header is: {next(csvreader)}'
    print(header)
    rows = [month for month in csvreader]
    # Use enumerate to get index
    for index, row in enumerate(rows):
        value = int(row[1])
        sumAmount(value)
        # Check so tha index does not go out of bounds
        if index + 1 < len(rows):
            findGreatestProfitAndLoss(rows[index], rows[index + 1])
        
    # Create  all string variable before printing and writing to text file
    totalMonthsResult = f'Total Months: {len(rows)}'
    totalAmountResult = f'Total: ${totalValue}'
    averageChangeResult = f'Average Change: $''%.2f'%((totalValue)/len(rows))
    greatestIncreaseProfit = f'Greatest Increase in Profits: {greatestProfitMonth} (${greatestProfitValue})'
    greatestDecreaseProfit = f'Greatest Decrease in Profits: {greatestLossMonth} (${greatestLossValue})'

    analysis_file = os.path.join('analysis', 'analysis.txt')
    analysis = open(analysis_file, 'w')
    results = ['Financial Analysis \n', '--------------------------- \n', f'{totalMonthsResult} \n', f'{totalAmountResult} \n', f'{averageChangeResult} \n'
               f'{greatestIncreaseProfit} \n', f'{greatestDecreaseProfit} \n' ]
    print(results)
    # analysis.writelines(results)

