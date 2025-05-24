"""
This is a Chris Piech's program that prompts Karel to search for words.
"""

from karel.stanfordkarel import *

def main():
    display_intro_message()
    create_puzzle()
    solve_puzzle()
    display_end_message()


def create_puzzle():
    place_cardinal()
    place_chris()
    place_karel()
    return_to_start()
    fill_empty_spaces()


def solve_puzzle():
    delay()
    check_for_karel()
    check_for_cardinal()
    check_for_chris()
    delay()
    delay()
    delay()


def place_cardinal():
    moveToTopRow()
    if (random(0.25)):
        # p = 1/4
        writeCardinal()
    else:
        if (random(.3333)):
            # p = 3/4 * 1/3 = 1/4
            moveForwardOneLetter()
            writeCardinal()

        else:
            for i in range(8):
                moveForwardOneLetter()

            if (random(.5)):
                # p = 3/4 * 1/3 * 1/2 = 1/4
                writeCardinal()
            else:
                # p = 3/4 * 1/3 * 1/2 = 1/4
                moveForwardOneLetter()
                writeCardinal()
    return_to_start()


def check_for_karel():
    for j in range(7):
        checkRowForKarel()
        move_up_to_next_row()

    checkRowForKarel()
    return_to_start()
    delay()


def checkRowForKarel():
    for i in range(6):
        checkIfKarel()
        moveForwardOneLetter()


def place_chris():
    if (random(0.125)):
        writeChrisInRow()
    elif (random(0.1429)):
        moveOneLetterUp()
        writeChrisInRow()

    elif (random(0.1667)):
        for i in range(2):
            moveOneLetterUp()
        writeChrisInRow()

    elif (random(0.2)):
        for i in range(3):
            moveOneLetterUp()
        writeChrisInRow()

    elif (random(0.25)):
        for i in range(4):
            moveOneLetterUp()
        writeChrisInRow()

    elif (random(0.3333)):
        for i in range(5):
            moveOneLetterUp()
        writeChrisInRow()

    elif (random(0.5)):
        for i in range(6):
            moveOneLetterUp()
        writeChrisInRow()

    else:
        moveToTopRow()
        writeChrisInRow()

    return_to_start()


def place_karel():
    while True:
        if (beepers_present()):
            if (right_is_clear()):
                pick_beeper()
                return_to_start()

        if (random(0.2000)):  # place in row 1
            moveToTopRow()
            placeCSInColumn()
        else:
            if (random(0.2500)):  # place in row 2
                for i in range(6):
                    moveOneLetterUp()
                placeCSInColumn()

            else:
                if (random(0.3333)):  # place in row 3
                    for i in range(5):
                        moveOneLetterUp()
                    placeCSInColumn()

                else:
                    if (random(0.5000)):  # place in row 4
                        for i in range(4):
                            moveOneLetterUp()
                        placeCSInColumn()

                    else:  # place in row 5
                        for i in range(3):
                            moveOneLetterUp()
                        placeCSInColumn()

        if not (beepers_present()): break
    return_to_start()


def moveToTopRow():
    for i in range(7):
        moveOneLetterUp()


def writeChrisInRow():
    if (beepers_present()):
        if (random(.2)):
            moveForwardOneLetter()
        elif (random(.25)):
            for i in range(2):
                moveForwardOneLetter()

        elif (random(.3333)):
            for i in range(3):
                moveForwardOneLetter()

        elif (random(.5)):
            for i in range(4):
                moveForwardOneLetter()

        else:
            for i in range(5):
                moveForwardOneLetter()

    else:
        moveForwardOneLetter()
        if (beepers_present()):
            if (random(.25)):
                moveForwardOneLetter()

            elif (random(.3333)):
                for i in range(2):
                    moveForwardOneLetter()

            elif (random(.5)):
                for i in range(3):
                    moveForwardOneLetter()

            else:
                for i in range(4):
                    moveForwardOneLetter()

        else:
            for i in range(7):
                moveForwardOneLetter()
            if (beepers_present()):
                if (random(.25)):
                    for i in range(8):
                        moveBackOneLetter()

                elif (random(.3333)):
                    for i in range(7):
                        moveBackOneLetter()

                elif (random(.5)):
                    for i in range(6):
                        moveBackOneLetter()

                else:
                    for i in range(5):
                        moveBackOneLetter()

            else:
                if (random(.2)):
                    for i in range(8):
                        moveBackOneLetter()

                elif (random(.25)):
                    for i in range(7):
                        moveBackOneLetter()

                elif (random(.3333)):
                    for i in range(6):
                        moveBackOneLetter()

                elif (random(.5)):
                    for i in range(5):
                        moveBackOneLetter()

                else:
                    for i in range(4):
                        moveBackOneLetter()

    writeChris()


def check_for_cardinal():
    for i in range(7):
        moveOneLetterUp()

    checkIfCardinal()
    moveForwardOneLetter()
    checkIfCardinal()
    for i in range(7):
        moveForwardOneLetter()

    checkIfCardinal()
    moveForwardOneLetter()
    checkIfCardinal()
    return_to_start()
    delay()


def move_up_to_next_row():
    turn_left()
    move6()
    turn_left()
    moveToWall()
    turn_around()


def moveToWall():
    while (front_is_clear()):
        move()


def check_for_chris():
    for j in range(7):
        check_for_chrisInRow()
        move_up_to_next_row()

    check_for_chrisInRow()
    return_to_start()
    delay()


def check_for_chrisInRow():
    for i in range(6):
        checkIfChris()
        moveForwardOneLetter()


def checkForJava():
    for i in range(3):
        moveOneLetterUp()
    for j in range(4):
        for i in range(7):
            checkIfJava()
            moveForwardOneLetter()

        turn_left()
        for i in range(6):
            move()
        turn_left()
        moveToWall()
        turn_around()

    for i in range(7):
        checkIfJava()
        moveForwardOneLetter()

    return_to_start()
    delay()


def checkIfCardinal():
    if (beepers_present()):
        moveBeeperOver()
        if (beepers_present()):
            moveBeeperOver()
            if (no_beepers_present()):  # C found:
                put_beepersBack()
                moveOneLetterDown()
                if (right_is_clear()):
                    moveBeeperOver()
                    if (no_beepers_present()):  # A found:
                        put_beepersBack()
                        moveOneLetterDown()
                        if (right_is_clear()):
                            for i in range(11):
                                safeMoveBeeper()

                            if (beepers_present()):
                                moveBeeperOver()
                                if (no_beepers_present()):  # R found:
                                    put_beepersBack()
                                    moveOneLetterDown()
                                    if (right_is_clear()):
                                        for i in range(2):
                                            safeMoveBeeper()

                                        if (beepers_present()):
                                            moveBeeperOver()
                                            if (no_beepers_present()):  # D found:
                                                put_beepersBack()
                                                moveOneLetterDown()
                                                if (right_is_clear()):
                                                    for i in range(5):
                                                        safeMoveBeeper()

                                                    if (beepers_present()):
                                                        moveBeeperOver()
                                                        if (no_beepers_present()):
                                                            put_beepersBack()
                                                            moveOneLetterDown()
                                                            if (right_is_clear()):
                                                                for i in range(9):
                                                                    safeMoveBeeper()

                                                                if (beepers_present()):
                                                                    moveBeeperOver()
                                                                    if (no_beepers_present()):
                                                                        put_beepersBack()
                                                                        moveOneLetterDown()
                                                                        if (right_is_clear()):
                                                                            moveBeeperOver()
                                                                            if (no_beepers_present()):
                                                                                put_beepersBack()
                                                                                moveOneLetterDown()
                                                                                for i in range(8):
                                                                                    safeMoveBeeper()

                                                                                if (beepers_present()):
                                                                                    moveBeeperOver()
                                                                                    if (no_beepers_present()):
                                                                                        put_beepersBack()
                                                                                        circleCardinal()

                                                                                    else:
                                                                                        put_beepersBack()
                                                                                        moveToTopRow()

                                                                                else:
                                                                                    put_beepersBack()
                                                                                    moveToTopRow()

                                                                            else:
                                                                                put_beepersBack()
                                                                                for i in range(6):
                                                                                    moveOneLetterUp()

                                                                        else:
                                                                            put_beepersBack()
                                                                            for i in range(6):
                                                                                moveOneLetterUp()

                                                                    else:
                                                                        put_beepersBack()
                                                                        for i in range(5):
                                                                            moveOneLetterUp()

                                                                else:
                                                                    put_beepersBack()
                                                                    for i in range(5):
                                                                        moveOneLetterUp()

                                                            else:
                                                                put_beepersBack()
                                                                for i in range(4):
                                                                    moveOneLetterUp()

                                                        else:
                                                            put_beepersBack()
                                                            for i in range(4):
                                                                moveOneLetterUp()

                                                    else:
                                                        put_beepersBack()
                                                        for i in range(4):
                                                            moveOneLetterUp()

                                                else:
                                                    put_beepersBack()
                                                    for i in range(3):
                                                        moveOneLetterUp()

                                            else:
                                                put_beepersBack()
                                                for i in range(3):
                                                    moveOneLetterUp()

                                        else:
                                            put_beepersBack()
                                            for i in range(3):
                                                moveOneLetterUp()

                                    else:
                                        put_beepersBack()
                                        for i in range(2):
                                            moveOneLetterUp()

                                else:
                                    put_beepersBack()
                                    for i in range(2):
                                        moveOneLetterUp()

                            else:
                                put_beepersBack()
                                for i in range(2):
                                    moveOneLetterUp()

                        else:
                            put_beepersBack()
                            moveOneLetterUp()

                    else:
                        put_beepersBack()
                        moveOneLetterUp()

                else:
                    put_beepersBack()
                    moveOneLetterUp()

            else:
                put_beepersBack()

        else:
            put_beepersBack()

    else:
        put_beepersBack()


def checkIfJava():
    if (beepers_present()):
        for i in range(6):
            safeMoveBeeper()

        if (beepers_present()):
            moveBeeperOver()
            if (no_beepers_present()):  # J found
                put_beepersBack()
                moveForwardOneLetter()
                moveOneLetterDown()
                moveBeeperOver()
                if (no_beepers_present()):  # A found
                    put_beepersBack()
                    moveForwardOneLetter()
                    moveOneLetterDown()
                    for i in range(13):
                        safeMoveBeeper()

                    if (beepers_present()):
                        moveBeeperOver()
                        if (no_beepers_present()):  # V found
                            put_beepersBack()
                            moveForwardOneLetter()
                            moveOneLetterDown()
                            moveBeeperOver()
                            if (no_beepers_present()):  # JAVA found
                                put_beepersBack()
                                circleJava()

                            else:
                                put_beepersBack()
                                for i in range(3):
                                    moveBackOneLetter()
                                    moveOneLetterUp()

                        else:
                            put_beepersBack()
                            for i in range(2):
                                moveBackOneLetter()
                                moveOneLetterUp()

                    else:
                        put_beepersBack()
                        for i in range(2):
                            moveBackOneLetter()
                            moveOneLetterUp()

                else:
                    put_beepersBack()
                    moveBackOneLetter()
                    moveOneLetterUp()

            else:
                put_beepersBack()

        else:
            put_beepersBack()


def checkIfChris():
    if (beepers_present()):
        moveBeeperOver()
        if (beepers_present()):
            moveBeeperOver()
            if (no_beepers_present()):  # C found:
                put_beepersBack()
                for i in range(5):
                    safeMove()
                if (front_is_clear()):
                    for i in range(4):
                        safeMoveBeeper()

                    if (beepers_present()):
                        moveBeeperOver()
                        if (no_beepers_present()):  # H found :
                            put_beepersBack()
                            for i in range(5):
                                safeMove()
                            if (front_is_clear()):
                                for i in range(11):
                                    safeMoveBeeper()

                                if (beepers_present()):
                                    moveBeeperOver()
                                    if (no_beepers_present()):  # R found:
                                        put_beepersBack()
                                        for i in range(5):
                                            safeMove()
                                        if (front_is_clear()):
                                            for i in range(5):
                                                safeMoveBeeper()

                                            if (beepers_present()):
                                                moveBeeperOver()
                                                if (no_beepers_present()):
                                                    put_beepersBack()
                                                    for i in range(5):
                                                        safeMove()
                                                    for i in range(12):
                                                        safeMoveBeeper()

                                                    if (beepers_present()):
                                                        moveBeeperOver()
                                                        if (no_beepers_present()):
                                                            put_beepersBack()
                                                            circleChris()

                                                        else:
                                                            put_beepersBack()
                                                            for i in range(4):
                                                                moveBackOneLetter()

                                                    else:
                                                        put_beepersBack()
                                                        for i in range(4):
                                                            moveBackOneLetter()

                                                else:
                                                    put_beepersBack()
                                                    for i in range(3):
                                                        moveBackOneLetter()

                                            else:
                                                put_beepersBack()
                                                for i in range(3):
                                                    moveBackOneLetter()

                                        else:
                                            put_beepersBack()
                                            for i in range(3):
                                                moveBackOneLetter()

                                    else:
                                        put_beepersBack()
                                        moveBackOneLetter()
                                        moveBackOneLetter()

                                else:
                                    put_beepersBack()
                                    moveBackOneLetter()
                                    moveBackOneLetter()

                            else:
                                put_beepersBack()
                                moveBackOneLetter()
                                moveBackOneLetter()

                        else:
                            put_beepersBack()
                            moveBackOneLetter()

                    else:
                        put_beepersBack()
                        moveBackOneLetter()

                else:
                    put_beepersBack()
                    moveBackOneLetter()

            else:
                put_beepersBack()

        else:
            put_beepersBack()


def checkIfKarel():
    if (beepers_present()):
        for i in range(7):
            safeMoveBeeper()

        if (beepers_present()):
            moveBeeperOver()
            if (no_beepers_present()):  # K found
                put_beepersBack()
                for i in range(5):
                    safeMove()
                if (front_is_clear()):
                    if (beepers_present()):
                        moveBeeperOver()
                        if (no_beepers_present()):  # A found
                            put_beepersBack()
                            for i in range(5):
                                safeMove()
                            if (front_is_clear()):
                                for i in range(11):
                                    safeMoveBeeper()

                                if (beepers_present()):
                                    moveBeeperOver()
                                    if (no_beepers_present()):  # R found
                                        put_beepersBack()
                                        for i in range(5):
                                            safeMove()
                                        if (front_is_clear()):
                                            for i in range(3):
                                                safeMoveBeeper()

                                            if (beepers_present()):
                                                moveBeeperOver()
                                                if (no_beepers_present()):  # E found
                                                    put_beepersBack()
                                                    for i in range(5):
                                                        safeMove()
                                                    for i in range(8):
                                                        safeMoveBeeper()

                                                    if (beepers_present()):
                                                        moveBeeperOver()
                                                        if (no_beepers_present()):  # KAREL found
                                                            put_beepersBack()
                                                            circleKarel()

                                                        else:
                                                            put_beepersBack()
                                                            for i in range(4):
                                                                moveBackOneLetter()

                                                    else:
                                                        put_beepersBack()
                                                        for i in range(4):
                                                            moveBackOneLetter()

                                                else:
                                                    put_beepersBack()
                                                    for i in range(3):
                                                        moveBackOneLetter()

                                            else:
                                                put_beepersBack()
                                                for i in range(3):
                                                    moveBackOneLetter()

                                        else:
                                            put_beepersBack()
                                            for i in range(3):
                                                moveBackOneLetter()

                                    else:
                                        put_beepersBack()
                                        moveBackOneLetter()
                                        moveBackOneLetter()

                                else:
                                    put_beepersBack()
                                    moveBackOneLetter()
                                    moveBackOneLetter()

                            else:
                                put_beepersBack()
                                moveBackOneLetter()
                                moveBackOneLetter()

                        else:
                            put_beepersBack()
                            moveBackOneLetter()

                    else:
                        put_beepersBack()
                        moveBackOneLetter()

                else:
                    put_beepersBack()
                    moveBackOneLetter()

            else:
                put_beepersBack()

        else:
            put_beepersBack()


def safeMoveBeeper():
    if (beepers_present()):
        moveBeeperOver()


def fill_empty_spaces():
    for i in range(9):
        if (no_beepers_present()):
            randomLeter()
        else:
            for j in range(3):
                move()

        move2()

    if (no_beepers_present()):
        randomLeter()
    else:
        for j in range(3):
            move()

    for i in range(7):
        turn_left()
        for j in range(6):
            move()
        turn_left()
        moveToWall()
        turn_around()

        for j in range(9):
            if (no_beepers_present()):
                randomLeter()
            else:
                for k in range(3):
                    move()

            move2()

        if (no_beepers_present()):
            randomLeter()

    return_to_start()


def safeMove():
    if (front_is_clear()):
        move()


def randomLeter():
    if (random(0.0714)):
        drawA()
    elif (random(.0769)):
        drawC()
    elif (random(.0833)):
        drawD()
    elif (random(.0909)):
        drawE()
    elif (random(.1000)):
        drawH()
    elif (random(.1111)):
        drawI()
    elif (random(.1250)):
        drawJ()
    elif (random(.1429)):
        drawK()
    elif (random(.1667)):
        drawL()
    elif (random(.2000)):
        drawN()
    elif (random(.2500)):
        drawP()
    elif (random(.3333)):
        drawR()
    elif (random(.5000)):
        drawS()
    else :				drawV()


def display_intro_message() :
   
      # clearScrean()					#FAST RUN
      intro()  # FAST RUN
      delay()
      clearScrean()  # FAST RUN
   

def delay():
    for i in range(4):
       turn_left()
    #    for j in range(3):
    #       for i in range(50000):
    #          turn_left()   


def put_beepersBack():
   move()
   while(beepers_present())	:
      pick_beeper()
      turn_around()
      move()
      put_beeper()
      turn_around()
      move()
   
   turn_around()
   move()
   turn_around()


def moveBeeperOver():
   pick_beeper()
   move()
   put_beeper()
   turn_around()
   move()
   turn_around()


def moveForwardOneLetter():
   for i in range(5):
      move()


def moveBackOneLetter():
   turn_around()
   for i in range(5):
      move()
   turn_around()


def return_to_start():
   turn_around()
   moveToWall()
   turn_left()
   moveToWall()
   turn_left()


def moveOneLetterUp():
   turn_left()
   for i in range(6):
      move()
   turn_right()


def moveOneLetterDown():
   turn_right()
   for i in range(6):
      move()
   turn_left()


def writeChris():
   drawC()
   move2()
   drawH()
   move2()
   drawR()
   move2()
   drawI()
   move2()
   drawS()


def writeCS():
   drawJ()
   move2()
   moveOneLetterDown()
   drawA()
   move2()
   moveOneLetterDown()
   drawV()
   move2()
   moveOneLetterDown()
   drawA()
   moveOneLetterUp()
   moveOneLetterUp()
   for i in range(3):
      moveBackOneLetter()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   drawK()
   move2()
   moveForwardOneLetter()
   drawR()
   move2()
   drawE()
   move2()
   drawL()


def writeCardinal():
   drawC()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   moveOneLetterDown()
   drawA()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   moveOneLetterDown()
   drawR()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   moveOneLetterDown()
   drawD()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   moveOneLetterDown()
   drawI()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   moveOneLetterDown()
   drawN()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   moveOneLetterDown()
   drawA()
   turn_around()
   for i in range(3):
      move()
   turn_around()
   moveOneLetterDown()
   drawL()


def moveToErrorMarker():
   turn_left()
   move()


def returnFromErrorMarker():
   turn_around()
   move()
   turn_left()


def checkForSpace() :
   if(beepers_present()) :
      moveToErrorMarker()
      put_beeper()
      returnFromErrorMarker()
   
   moveToErrorMarker()
   for j in range(3):
      if(no_beepers_present()) :
         for i in range(4):
            if(no_beepers_present()) :
               returnFromErrorMarker()
               if(no_beepers_present()) :
                  moveForwardOneLetter()
                  if(beepers_present()) :
                     moveToErrorMarker()
                     put_beeper()
                  
                  else:
                     moveToErrorMarker()
               
               else :
                  moveToErrorMarker()
                  put_beeper()
                    
         if(no_beepers_present()) :
            turn_right()
            for i in range(4):
               moveBackOneLetter()
            moveOneLetterDown()
            turn_left()
         
   for i in range(4):
      if(no_beepers_present()) :
         returnFromErrorMarker()
         if(no_beepers_present()) :
            moveForwardOneLetter()
            if(beepers_present()) :
               moveToErrorMarker()
               put_beeper()
            
            else:
               moveToErrorMarker()
         
         else :
            moveToErrorMarker()
            put_beeper()     
   
   if(no_beepers_present()) :
      turn_around()
      move()
      turn_left()
   

def placeCSInColumn():
   if(random(0.1667)) :		# column 1
      checkForSpace()
      writeCSIfFree()
   
   else :
      if(random(0.2)) :
         moveForwardOneLetter()
         checkForSpace()
         writeCSIfFree()
      
      else :
         if(random(0.25)):
            for i in range(2):
               moveForwardOneLetter()
            checkForSpace()
            writeCSIfFree()
         
         else :
            if(random(0.3333)):
               for i in range(3):
                  moveForwardOneLetter()
               checkForSpace()
               writeCSIfFree()
            
            else :
               if(random(0.5)):
                  for i in range(4):
                     moveForwardOneLetter()
                  checkForSpace()
                  writeCSIfFree()
               
               else :
                  for i in range(5):
                     moveForwardOneLetter()
                  checkForSpace()
                  writeCSIfFree()
               
            
def writeCSIfFree():
   if(no_beepers_present()) :
      for i in range(4):
         moveBackOneLetter()
      for i in range(3):
         moveOneLetterUp()
      writeCS()
      turn_left()
      move()
   
   else :
      while(beepers_present()):
         pick_beeper()
      put_beeper()
   
   turn_right()


def intro() :
   moveToTopRow()
   turn_right()
   move2()
   turn_left()
   for i in range(3):
      moveForwardOneLetter()
   turn_around()
   move2()
   turn_around()
   drawK()
   move2()
   drawA()
   move2()
   drawR()
   move2()
   drawE()
   move2()
   drawL()
   move2()
   moveOneLetterDown()
   for i in range(4):
      moveBackOneLetter()
   drawC()
   move2()
   drawA()
   move2()
   drawN()
   move2()
   moveOneLetterDown()
   for i in range(4):
      moveBackOneLetter()
   drawS()
   move2()
   drawP()
   move2()
   drawE()
   move2()
   drawL()
   move2()
   drawL()
   move2()
   moveOneLetterDown()
   moveOneLetterDown()
   for i in range(4):
      moveBackOneLetter()
   move2()
   drawB()
   moveForwardOneLetter()
   drawY()
   move2()
   moveOneLetterDown()
   for i in range(3):
      moveBackOneLetter()
   drawC()
   move2()
   drawH()
   move2()
   drawR()
   move2()
   drawI()
   move2()
   drawS()
   move2()
   moveOneLetterDown()
   for i in range(5):
      moveBackOneLetter()
   drawP()
   move2()
   drawI()
   move2()
   drawE()
   move2()
   drawC()
   move2()
   drawH()
   return_to_start()


def display_end_message():
   clearScrean()
   for i in range(4):
      moveOneLetterUp()
   for i in range(3):
      moveForwardOneLetter()
   move2()
   move()
   drawE()
   move2()
   drawN()
   move2()
   drawD()
   return_to_start()
   delay()
   clearScrean()


def clearScrean():
   for i in range(46):
      for j in range(48):
         paint_corner('white')
         while(beepers_present()):
            pick_beeper()
         
         move()
      
      paint_corner('white')
      while(beepers_present()):
         pick_beeper()
      
      if(facing_east()):
         turn_left()
         move()
         turn_left()
      
      else :
         turn_right()
         move()
         turn_right()
      
   for j in range(48):
      paint_corner('white')
      while(beepers_present()):
         pick_beeper()
      
      move()
   
   paint_corner('white')
   while(beepers_present()):
      pick_beeper()
   
   return_to_start()


def circleChris():
   for i in range(3):
      move()
   turn_left()
   for i in range(3):
      move()
      paint_corner('black')
   
   move()
   turn_left()
   paint_corner('black')
   for i in range(22):
      move()
      paint_corner('black')
   
   move()
   turn_left()
   paint_corner('black')
   for i in range(3):
      move()
      paint_corner('black')
   
   move()
   turn_left()
   paint_corner('black')
   for i in range(23):
      move()
      paint_corner('black')
   
   turn_around()
   for i in range(23):
      move()
   turn_around()


def circleJava():
   for i in range(3):
      moveBackOneLetter()
      moveOneLetterUp()
   
   for j in range(2):
      for i in range(5):
         paint_corner('black')
         move()
         turn_right()
         move()
         turn_left()
      
      paint_corner('black')
      turn_right()
      move()
      paint_corner('black')
      turn_left()
   
   for i in range(6):
      paint_corner('black')
      move()
      turn_right()
      move()
      turn_left()
   
   paint_corner('black')
   move()
   paint_corner('black')
   move()
   turn_left()
   for i in range(4):
      move()
      paint_corner('black')
   
   for j in range(3):
      for i in range(5):
         paint_corner('black')
         move()
         turn_left()
         move()
         turn_right()
      
      paint_corner('black')
      move()
   
   turn_left()
   move()
   for i in range(2):
      paint_corner('black')
      move()
   
   turn_left()
   for i in range(3):
      move()
      paint_corner('black')
   
   move()
   turn_left()


def circleKarel():
   for i in range(3):
      move()
   turn_left()
   for i in range(3):
      move()
      paint_corner('black')
   
   move()
   turn_left()
   paint_corner('black')
   for i in range(22):
      move()
      paint_corner('black')
   
   move()
   turn_left()
   paint_corner('black')
   for i in range(3):
      move()
      paint_corner('black')
   
   move()
   turn_left()
   paint_corner('black')
   for i in range(23):
      move()
      paint_corner('black')
   
   turn_around()
   for i in range(23):
      move()
   turn_around()


def circleCardinal():
   paint_corner('black')
   for i in range(3):
      move()
      paint_corner('black')
   
   if(front_is_blocked()) :
      turn_left()
      for i in range(46):
         move()
         paint_corner('black')
      
      turn_left()
      for i in range(4):
         move()
         paint_corner('black')
      
      turn_left()
      for i in range(46):
         move()
         paint_corner('black')
      
      turn_around()
      for i in range(46):
         move()
      turn_right()
      move()
   
   else :
      move()
      paint_corner('black')
      turn_left()
      for i in range(46):
         move()
         paint_corner('black')
      
      turn_left()
      for i in range(4):
         move()
         paint_corner('black')
      
      turn_left()
      for i in range(46):
         move()
         paint_corner('black')
      
      turn_around()
      for i in range(46):
         move()
      turn_right()
   

def move2() :
   move()
   move()


def move3() :
   for i in range(3):
      move()
   

def move4() :
   for i in range(4):
      move()


def move6() :
   for i in range(6):
      move()
   

def drawA():
   put_beeper()
   turn_left()
   for i in range(4):
      paint_corner('green')
      move()
   
   turn_right()
   move()
   for i in range(2):
      paint_corner('green')
      move()
   
   turn_right()
   move()
   for i in range(3):
      paint_corner('green')
      move()
   
   paint_corner('green')
   turn_around()
   move2()
   turn_left()
   for i in range(2):
      move()
      paint_corner('green')
   
   turn_around()
   move2()
   turn_right()
   move2()
   turn_left()


def drawC():
   for i in range(2):
      put_beeper()
   move2()
   turn_around()
   for i in range(2):
      paint_corner('blue')
      move()
   
   turn_right()
   move()
   for i in range(3):
      paint_corner('blue')
      move()
   
   turn_right()
   move()
   for i in range(2):
      paint_corner('blue')
      move()
   
   turn_right()
   move()
   paint_corner('blue')
   move2()
   paint_corner('blue')
   move()
   turn_left()


def drawD():
   for i in range(3):
      put_beeper()
   for i in range(3):
      paint_corner('cyan')
      move()
   
   turn_left()
   move()
   for i in range(3):
      paint_corner('cyan')
      move()
   
   turn_left()
   move()
   for i in range(2):
      paint_corner('cyan')
      move()
   
   turn_left()
   for i in range(4):
      paint_corner('cyan')
      move()
   
   turn_left()
   for i in range(3):
      paint_corner('cyan')
      move()
   

def drawE():
   for i in range(4):
      put_beeper()
   turn_left()
   for i in range(4):
      paint_corner('green')
      move()
   
   paint_corner('green')
   turn_right()
   for i in range(3):
      move()
      paint_corner('green')
   
   turn_right()
   move2()
   turn_right()
   for i in range(2):
      move()
      paint_corner('green')
   
   move()
   turn_left()
   move2()
   turn_left()
   for i in range(3):
      move()
      paint_corner('green')
   
   
def drawH():
   for i in range(5):
      put_beeper()
   turn_left()
   for i in range(4):
      paint_corner('magenta')
      move()
   
   paint_corner('magenta')
   turn_around()
   move2()
   turn_left()
   for i in range(2):
      move()
      paint_corner('magenta')
   
   move()
   turn_left()
   move2()
   turn_around()
   for i in range(4):
      paint_corner('magenta')
      move()
   
   paint_corner('magenta')
   turn_left()


def drawB():
   for i in range(2):
      put_beeper()
   turn_left()
   for i in range(4):
      paint_corner('black')
      move()
   
   paint_corner('black')
   turn_right()
   for i in range(2):
      move()
      paint_corner('black')
   
   move()
   turn_right()
   move()
   paint_corner('black')
   move()
   turn_right()
   for i in range(2):
      move()
      paint_corner('black')
   
   turn_around()
   move2()
   turn_right()
   move()
   paint_corner('black')
   move()
   turn_right()
   move()
   for i in range(2):
      paint_corner('black')
      move()
   
   turn_around()


def drawY():
   for i in range(6):
      put_beeper()
   move()
   turn_left()
   for i in range(3):
      paint_corner('black')
      move()
   
   turn_left()
   move()
   turn_right()
   paint_corner('black')
   move()
   paint_corner('black')
   turn_right()
   move2()
   turn_right()
   for i in range(2):
      paint_corner('black')
      move()
   
   move2()
   turn_right()
   move2()
   turn_around()


def drawI():
   for i in range(6):
      put_beeper()
   move2()
   turn_left()
   for i in range(4):
      paint_corner('orange')
      move()
   
   paint_corner('orange')
   turn_around()
   move4()
   turn_left()
   move()


def drawJ():
   for i in range(7):
      put_beeper()
   turn_left()
   move()
   paint_corner(PINK)
   turn_right()
   move()
   turn_right()
   move()
   paint_corner(PINK)
   turn_left()
   move()
   turn_left()
   for i in range(3):
      move()
      paint_corner(PINK)
   
   turn_left()
   move2()
   turn_right()
   move()
   turn_right()
   for i in range(3):
      paint_corner(PINK)
      move()
   
   paint_corner(PINK)
   turn_right()
   move4()
   turn_left()


def drawK():
   for i in range(8):
      put_beeper()
   turn_left()
   for i in range(4):
      paint_corner('red')
      move()
   
   paint_corner('red')
   turn_right()
   move3()
   paint_corner('red')
   turn_right()
   move()
   turn_right()
   move()
   paint_corner('red')
   turn_left()
   move()
   turn_right()
   move()
   paint_corner('red')
   turn_left()
   move()
   turn_left()
   move()
   paint_corner('red')
   turn_right()
   move()
   turn_left()
   move()
   paint_corner('red')


def drawN():
   for i in range(10):
      put_beeper()
   
   turn_left()
   for i in range(4):
      paint_corner('blue')
      move()
   
   paint_corner('blue')
   turn_right()
   move()
   turn_right()
   move()
   paint_corner('blue')
   turn_left()
   move()
   turn_right()
   move()
   paint_corner('blue')
   move2()
   turn_left()
   move()
   turn_left()
   for i in range(4):
      paint_corner('blue')
      move()
   
   paint_corner('blue')
   turn_around()
   move4()
   turn_left()


def drawP():
   for i in range(11):
      put_beeper()
   
   turn_left()
   for i in range(4):
      paint_corner('blue')
      move()
   
   paint_corner('blue')
   turn_right()
   move()
   for i in range(2):
      paint_corner('blue')
      move()
   
   turn_right()
   move()
   paint_corner('blue')
   move()
   turn_right()
   for i in range(2):
      move()
      paint_corner('blue')
   
   turn_left()
   move2()
   turn_left()
   move2()


def drawR() :
   for i in range(12):
      put_beeper()
   
   turn_left()
   for i in range(4):
      paint_corner('cyan')
      move()
   
   paint_corner('cyan')
   turn_right()
   move()
   for i in range(2):
      paint_corner('cyan')
      move()
   
   turn_right()
   move()
   paint_corner('cyan')
   move()
   turn_right()
   for i in range(2):
      move()
      paint_corner('cyan')
   
   turn_around()
   move2()
   turn_right()
   move()
   paint_corner('cyan')
   move()
   paint_corner('cyan')
   turn_left()


def drawS():
   for i in range(13):
      put_beeper()
   
   for i in range(3):
      paint_corner('red')
      move()
   
   turn_left()
   move()
   paint_corner('red')
   move()
   turn_left()
   move()
   for i in range(2):
      paint_corner('red')
      move()
   
   turn_right()
   move()
   paint_corner('red')
   move()
   turn_right()
   for i in range(3):
      move()
      paint_corner('red')
   
   turn_right()
   move4()
   turn_left()


def drawV():
   # unique beeper pile for V
   for i in range(14):
      put_beeper()
   
   
   turn_left()
   move()
   for i in range(3):
      move()
      paint_corner('green')
   
   turn_around()
   move4()
   turn_left()
   move()
   paint_corner('green')
   turn_left()
   move()
   turn_right()
   for i in range(2):
      paint_corner('green')
      move()
   
   turn_left()
   for i in range(3):
      move()
      paint_corner('green')
   
   turn_around()
   move4()
   turn_left()


def drawL():
   # unique beeper pile for L
   for i in range(9):
      put_beeper()
   
   drawStem()
   drawLeg()


def drawLeg() :
   for i in range(3):
      move()
      paint_corner('yellow')
   

def drawStem() :
   turn_left()
   move4()
   turn_around()
   for i in range(4):
      paint_corner('yellow')
      move()
   
   paint_corner('yellow')
   turn_left()


def turn_right():
   for i in range(3):
      turn_left()


def turn_around():
   turn_left()
   turn_left()


if __name__ == "__main__":
    main()
