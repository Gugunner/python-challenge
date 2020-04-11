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
changeList = []
csvPath = os.path.join('Resources', 'budget_data.csv')

def sumAmount(value: int):
    global totalValue
    totalValue += value

def findIncreaseAndDecreaseOfProfit(before: list, after: list):
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
        greatestLossMonth = after[0]

def addToChangeList(before: list, after: list):
    global changeList
    currentValue = int(before[1])
    differenceValue = int(after[1])-currentValue
    changeList.append(differenceValue)

with open(csvPath) as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')
    # advance csv to skip header
    next(csvreader)
    rows = [month for month in csvreader]
    # Use enumerate to get index
    for index, row in enumerate(rows):
        value = int(row[1])
        sumAmount(value)
        # Check so tha index does not go out of bounds
        if index + 1 < len(rows):
            findIncreaseAndDecreaseOfProfit(rows[index], rows[index + 1])
            addToChangeList(rows[index], rows[index + 1])
        
    # Create  all string variable before printing and writing to text file
    totalMonthsResult = f'Total Months: {len(rows)}'
    totalAmountResult = f'Total: ${totalValue}'
    averageChangeResult = f'Average Change: $''%.2f'%(sum(changeList, 0)/len(changeList))+'\n '
    greatestIncreaseProfit = f'Greatest Increase in Profits: {greatestProfitMonth} (${greatestProfitValue})'
    greatestDecreaseProfit = f'Greatest Decrease in Profits: {greatestLossMonth} (${greatestLossValue})'
    # Printing and writing to file
    analysis_file = os.path.join('analysis', 'analysis.txt')
    analysis = open(analysis_file, 'w')
    results = [' Financial Analysis', '----------------------------', f'{totalMonthsResult}', f'{totalAmountResult}', f'{averageChangeResult}'
               f'{greatestIncreaseProfit}', f'{greatestDecreaseProfit}' ]
    for result in results:
        print(result)
    fileResults = [f'{result}\n 'for result in results ]
    analysis.writelines(fileResults)

