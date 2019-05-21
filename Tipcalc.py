from graphics import *



def calcTip(totalBill, percentOfBill):
    percent = percentOfBill / 100
    total = percent * totalBill
    return total


def main():
    win = GraphWin("Tip Calculator", 500,400) ##Create window object and set dimensions of frame
    win.setBackground("Black") ##set background of window to black


                 ##drawing the first line of text asking for total bill
    pt = Point(150,50) ##The point defines where in the window the text will be centered to
    askForBill = Text(pt, "Enter total bill: ")
    askForBill.setTextColor('White') ##define what color you want the text to be
    askForBill.draw(win) ##make sure you draw the new object to the window you want it in. 


                    ##drawing first input box to take the total bill
    pt2 = Point(350,50)
    billInput = Entry(pt2, 5) ##seting locaton and size of entry box
    billInput.setText("0.0") ##default text inside entry box
    billInput.draw(win)


                     ##draw second line of text asking for percentage
    pt3 = Point(150,100)
    askForPercent = Text(pt3, "Enter tip percent")
    askForPercent.setTextColor('White')
    askForPercent.draw(win)


                     ##drawing second input box to take the percentage
    pt4 = Point(350,100)
    percentInput = Entry(pt4, 5) ##seting locaton and size of entry box
    percentInput.setText("0.0") ##default text inside entry box
    percentInput.draw(win)


                    ##draw third line of text to label output
    pt5 = Point(150,150)
    Line3 = Text(pt5, "The tip you owe is:")
    Line3.setTextColor('White')
    Line3.draw(win)
    
                     ##drawing third box to display calculation
    pt6 = Point(350,150)
    tipOutput = Entry(pt6, 5) ##seting locaton and size of entry box
    tipOutput.setText("0.0") ##default text inside entry box
    tipOutput.draw(win)

                       ##Update button
    pt7 = Point(100,200) 
    pt8 = Point(200,250)
    rec = Rectangle(pt7,pt8)
    rec.setFill("white")
    rec.setOutline("black")
    rc = rec.getCenter()
    label1 = Text (rc, "Update")
    label1.setSize(10)
    rec.draw(win)
    label1.draw(win)
    
                    ##Quit Button    
    rec2 = rec.clone()
    rec2.move(150, 0)
    rc2 = rec2.getCenter()
    label2 = Text(rc2,"Quit")
    rec2.draw(win)
    label2.draw(win)
    m = rec2.getP1()
    n = rec2.getP2()
    


                 ##Update and quit button function
    for i in range(500):
        try:
            p = win.getMouse()
        except GraphicsError:
            win.close()
        if (p.getX() > pt7.getX()) and (p.getX() < pt8.getX()): ##if the mouse is clicked within the coordinates of the update button
            if(p.getY() > pt7.getY()) and (p.getY() < pt8.getY()):
                total = calcTip(eval(billInput.getText()), eval(percentInput.getText())) ##Call the calculate function to do the math and find the tip
                tipOutput.setText(total) ##Set the output box to display the answer
        elif (p.getX() > m.getX()) and (p.getX() < n.getX()) : ##else if the mouse is in the quit button coordinates
            if (p.getY() > m.getY()) and (p.getY() < n.getY()):
                win.close() ##close the window
                sys.exit() ##End program

main()
    


##    print("Your total tip owed is:", calcTip(bill, percent),"\n Click anywhere to exit.")
            
            
##Below is error handling. it is not yet implimented with the window, but it did work when the program was only text based
    
##while True:
##    try:
##        main()
##    except(ZeroDivisionError,ValueError):
##        print("That is invalid -try again")


