from graphics import *



def calcTip(totalBill, percentOfBill):
    percent = percentOfBill / 100
    total = percent * totalBill
    return total


def main():
    win = GraphWin("Tip Calculator", 400,250) ##Create window object and set dimensions of frame
    win.setBackground("purple") ##set background of window to orange

    ##-------------Total bill label box -------------##
    pt = Point(150,50) ##The point defines where in the window the text will be centered to
    askForBill = Text(pt, "Enter total bill: ")
    askForBill.setTextColor('White') ##define what color you want the text to be
    askForBill.draw(win) ##make sure you draw the new object to the window you want it in. 

    ##-------------Total bill input box -------------##
    pt2 = Point(300,50)
    billInput = Entry(pt2, 5) ##seting locaton and size of entry box
    billInput.setText("0.0") ##default text inside entry box
    billInput.draw(win)


    ##-------------Tip percent label box -------------##
    pt3 = Point(150,100)
    askForPercent = Text(pt3, "Enter tip percent:")
    askForPercent.setTextColor('White')
    askForPercent.draw(win)

    ##-------------Tip percent input box -------------##
    pt4 = Point(300,100)
    percentInput = Entry(pt4, 5) ##seting locaton and size of entry box
    percentInput.setText("0.0") ##default text inside entry box
    percentInput.draw(win)


    ##-------------Tip owed label box -------------##
    pt5 = Point(150,200)
    Line3 = Text(pt5, "The tip you owe is:")
    Line3.setTextColor('White')
    Line3.draw(win)


    ##------------- Tip owed output box-------------##
    pt6 = Point(300,200)
    tipOutput = Entry(pt6, 5) ##seting locaton and size of entry box
    tipOutput.setText(calcTip) ##default text inside entry box
    tipOutput.draw(win) 


    ##-------------Update button-------------##
    
    pt7 = Point(125,125) 
    pt8 = Point(275,175)
    rec = Rectangle(pt7,pt8)
    rec.setFill("white")
    rec.setOutline("black")
    rc = rec.getCenter()
    label1 = Text (rc, "Update")
    label1.setSize(11)
    rec.draw(win)
    label1.draw(win)


    ##-------------Update button function UNFINISHED-------------##
    
    for i in range(500):
        try:
            p = win.getMouse()
        except GraphicsError:
            win.close()
        if (p.getX() >pt7.getX()) and (p.getY() < pt8.getY()):
            percent = percentInput / 100
            total = percent * billInput
            newM = total
            output1.setText(newM)
        elif (p.getX() > m.getX()) and (p.getX() < n.getX()):
            if (p.getY() > m.getY()) and (p.getY() <n.getY()):
                win.close()







main() # keep this.






    


##    print("Your total tip owed is:", calcTip(bill, percent),"\n Click anywhere to exit.")
            
            
##Below is error handling. it is not yet implimented with the window, but it did work when the program was only text based
    
##while True:
##    try:
##        main()
##    except(ZeroDivisionError,ValueError):
##        print("That is invalid -try again")
