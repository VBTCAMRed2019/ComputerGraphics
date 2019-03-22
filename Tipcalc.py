from graphics import *



def calcTip(totalBill, percentOfBill):
    percent = percentOfBill / 100
    total = percent * totalBill
    return total


def main():
    win = GraphWin("Tip Calculator", 500,400) ##Create window object and set dimensions of frame
    win.setBackground("Black") ##set background of window to black

    ##drawing the first line of text asking for total bill
    pt = Point(150,50) 
    askForBill = Text(pt, "Enter your total bill: ")
    askForBill.setTextColor('White')
    askForBill.draw(win)

    ##drawing first input box to take the total bill
    pt2 = Point(350,50)
    billInput = Entry(pt2, 5) ##seting locaton and size of entry box
    billInput.setText("0.0") ##default text inside entry box
    billinput.draw(win)

    ##draw second line of text asking for percentage
    pt3 = Point(150,150)
    askForPercent = Text(pt3, "Enter the percentage of the bill you want to tip: ")
    askForPercentage.setTextColor('White')
    askForBill.draw(win)

    ##drawing second input box to take the percentage
    pt2 = Point(350,50)
    percentInput = Entry(pt2, 5) ##seting locaton and size of entry box
    percentInput.setText("0.0") ##default text inside entry box
    percentInput.draw(win)


    print("Your total tip owed is:", calcTip(bill, percent),"\n Click anywhere to exit."))
            
            

    
while True:
    try:
        main()
    except(ZeroDivisionError,ValueError):
        print("That is invalid -try again")
