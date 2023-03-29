screen = Label('Start',-100,-100) #used as an event to let the game know what screen it is on.
rectanglesDrawn = Label(0,-100,-100) #stops the rectangles from drawing every frame
checkpointsHit = Label(0,-100,-100)
unplayable = Label(0,-100,-100)

checkpt1 = Rect(220,240,20,20,fill='yellow',visible=False)
checkpt2 = Rect(260,20,20,20,fill='yellow',visible=False)
checkpt3 = Rect(280,160,20,20,fill='yellow',visible=False)

win = Rect(20,20,20,20,fill='gold')
    
if screen.value=='Start': #if on the start screen
    yellowScreen = Rect(0,0,400,400,fill='yellow')
    startClicker = Rect(20,360,20,20,fill='red') #click this guy to start, so the mouse is at that position
    redPixels = Label('Click the Red Pixels To Start',200,200,size=20) 
    redPixels2 = Label("Be sure you click and don't move the mouse while you're clicking.",200,240)
    w1=Rect(60,40,60,40,visible=False)
    w2=Rect(160,40,120,120,visible=False)
    w3=Rect(0,80,100,80,visible=False)
    w4=Rect(120,100,40,60,visible=False)
    w5=Rect(300,40,40,120,visible=False)
    w6=Rect(340,100,20,60,visible=False) 
    w7=Rect(360,40,20,40,visible=False)
    w8=Rect(0,200,60,140,visible=False)
    w9=Rect(60,180,40,100,visible=False)
    w10=Rect(120,200,100,100,visible=False)
    w11=Rect(160,160,40,20,visible=False)
    w12=Rect(260,180,40,100,visible=False) #sets them here just so they don't actually crash anything down the line, or spawn thousands
    w13=Rect(240,220,20,40,visible=False) # of rectangles.
    w14=Rect(80,320,140,40,visible=False)
    w15=Rect(240,300,40,40,visible=False)
    w16=Rect(320,180,40,200,visible=False)
    w17=Rect(100,200,20,20,visible=False)
    w18=Rect(300,260,20,20,visible=False)
    w19=Rect(120,40,40,20,visible=False)
    w20=Rect(20,380,400,400,visible=False)
    w21=Rect(380,0,400,400,visible=False)
    w22=Rect(0,0,20,400,visible=False)
    w23=Rect(0,0,380,20,visible=False)    
    ### checking start square
def checkSquareForStart(square,checkX,checkY):
    if checkX>square.left-1:
        if checkX<square.right+1: # it's all plus or minus one pixel because the edges of shapes like to act funny
            if checkY>square.top-1:
                if checkY<square.bottom+1:
                    screen.value='playGame' #allows gameplay to begin
    ### checking kill square
def checkSquareForWallCollision(square,checkX,checkY): # 
    if checkX>square.left-1:
        if checkX<square.right+1:
            if checkY>square.top-1:
                if checkY<square.bottom+1:
                    if not screen.value=='gameEnd': #if the game hasnt already ended,
                        Rect(0,0,400,400,fill='white')
                        Label('You touched a wall.',200,200,size=20)
                        Label('This is the bit where you reset.',200,220,size=20)
                        Label('Go click the run button again.',200,240,size=20)
                        win.centerX=-100
                        win.centerY=-100
                        screen.value='gameEnd' #stops the game from making these shapes a lot of times
                        
    ### checking checkpoint squares
def checkCheckpoint(square,checkX,checkY):
    if checkX>square.left-1:
        if checkX<square.right+1:
            if checkY>square.top-1:
                if checkY<square.bottom+1:
                    checkpointsHit.value+=1
                    square.centerX=-100
                    square.centerY=-100
                    
    ### checking win blocks
def checkWinBlock(square,checkX,checkY):
    if checkX>square.left-1:
        if checkX<square.right+1:
            if checkY>square.top-1:
                if checkY<square.bottom+1:
                    if checkpointsHit.value==3:
                        screen.value ='endScreen'
                    else:
                        screen.value ='youCheated'
                    
                    
def onMousePress(mX,mY):
    checkSquareForStart(startClicker,mX,mY)
    if not screen.value=='Start':
        redPixels.visible=False
        redPixels2.visible=False
        startClicker.visible=False
        yellowScreen.visible=False # hides the starting objects,
        if screen.value=='playGame':
            if rectanglesDrawn.value==0:
                pass
            w1.visible=True
            w2.visible=True
            w3.visible=True
            w4.visible=True
            w5.visible=True
            w6.visible=True
            w7.visible=True
            w8.visible=True
            w9.visible=True
            w10.visible=True
            w11.visible=True #made visible now.
            w12.visible=True
            w13.visible=True
            w14.visible=True
            w15.visible=True
            w16.visible=True
            w17.visible=True
            w18.visible=True
            w19.visible=True
            w20.visible=True
            w21.visible=True
            w22.visible=True
            w23.visible=True
            rectanglesDrawn.value=1 #couldn't get groups working the way i wanted them to, so its a list of individual rectangles
        
def onMouseMove(mX,mY):
    if unplayable.value==1:
        screen.value='youCheated' #makes the game so you can't actually change the ending by touching another wall
    if unplayable.value==2:
        screen.value='endScreen' #makes the game constantly set to end screen as your screen
    if rectanglesDrawn.value==1:
        if not screen.value=='gameEnd':
            checkSquareForWallCollision(w1,mX,mY)
            checkSquareForWallCollision(w2,mX,mY)
            checkSquareForWallCollision(w3,mX,mY)
            checkSquareForWallCollision(w4,mX,mY)
            checkSquareForWallCollision(w5,mX,mY)
            checkSquareForWallCollision(w6,mX,mY)
            checkSquareForWallCollision(w7,mX,mY)
            checkSquareForWallCollision(w8,mX,mY)
            checkSquareForWallCollision(w9,mX,mY)
            checkSquareForWallCollision(w10,mX,mY) #checks the walls for collision
            checkSquareForWallCollision(w11,mX,mY)
            checkSquareForWallCollision(w12,mX,mY)
            checkSquareForWallCollision(w13,mX,mY)
            checkSquareForWallCollision(w14,mX,mY)
            checkSquareForWallCollision(w15,mX,mY)
            checkSquareForWallCollision(w16,mX,mY)
            checkSquareForWallCollision(w17,mX,mY)
            checkSquareForWallCollision(w18,mX,mY)
            checkSquareForWallCollision(w19,mX,mY)
            checkSquareForWallCollision(w20,mX,mY)
            checkSquareForWallCollision(w21,mX,mY)
            checkSquareForWallCollision(w22,mX,mY)
            checkSquareForWallCollision(w23,mX,mY)
            
            checkCheckpoint(checkpt1,mX,mY)
            checkCheckpoint(checkpt2,mX,mY)
            checkCheckpoint(checkpt3,mX,mY) #checks each checkpoint, and you should get a checkpoint counter of 3 by the end of the game,
                                        #unless you cheated, in which case you get the cheater screen
            checkWinBlock(win,mX,mY)
        
        if screen.value=='youCheated': #the cheating screen
            Rect(0,0,400,400,fill='Red')
            Label("You truly are the scum of society.",200,200,fill='darkRed')
            Label("You really cheated in a maze game.",200,240,fill='darkRed')
            Label("This game is singleplayer, why even try.",200,280,fill='darkRed')
            Label("And you got caught. Even sadder.",200,300,fill='darkRed')
            Label("Don't even retry. You just suck, you scum.",200,320,fill='darkRed')
            win.centerX=-100
            win.centerY=-100
            w1.centerX=-1000
            w2.centerX=-1000
            w3.centerX=-1000
            w4.centerX=-1000
            w5.centerX=-1000
            w6.centerX=-1000
            w7.centerX=-1000
            w8.centerX=-1000
            w9.centerX=-1000
            w10.centerX=-1000
            w11.centerX=-1000
            w12.centerX=-1000
            w13.centerX=-1000
            w14.centerX=-1000
            w15.centerX=-1000 #moving them offscreen to prevent alternate endings after the game has already ended
            w16.centerX=-1000
            w17.centerX=-1000
            w18.centerX=-1000
            w19.centerX=-1000
            w20.centerX=-1000
            w21.centerX=-1000
            w22.centerX=-1000
            w23.centerX=-1000
        if screen.value=='endScreen': #the winning screen
            Rect(0,0,400,400,fill='gold')
            Label("You won! Good job, I don't know what to write here.",200,200,fill='darkRed')
            w1.centerX=-1000
            w2.centerX=-1000
            w3.centerX=-1000
            w4.centerX=-1000
            w5.centerX=-1000
            w6.centerX=-1000
            w7.centerX=-1000
            w8.centerX=-1000
            w9.centerX=-1000
            w10.centerX=-1000
            w11.centerX=-1000
            w12.centerX=-1000
            w13.centerX=-1000
            w14.centerX=-1000
            w15.centerX=-1000 #moving them offscreen to prevent alternate endings after the game has already ended
            w16.centerX=-1000
            w17.centerX=-1000
            w18.centerX=-1000
            w19.centerX=-1000
            w20.centerX=-1000
            w21.centerX=-1000
            w22.centerX=-1000
            w23.centerX=-1000
def onMouseDrag(mX,mY):
    screen.value='youCheated' #dragging the mouse to try to cheat isn't ok. and i will not treat it as such.
    unplayable.value=1
    w1.centerX=-1000
    w2.centerX=-1000
    w3.centerX=-1000
    w4.centerX=-1000
    w5.centerX=-1000
    w6.centerX=-1000
    w7.centerX=-1000
    w8.centerX=-1000
    w9.centerX=-1000
    w10.centerX=-1000
    w11.centerX=-1000
    w12.centerX=-1000
    w13.centerX=-1000
    w14.centerX=-1000
    w15.centerX=-1000 #moving them offscreen to prevent alternate endings after the game has already ended
    w16.centerX=-1000
    w17.centerX=-1000
    w18.centerX=-1000
    w19.centerX=-1000
    w20.centerX=-1000
    w21.centerX=-1000
    w22.centerX=-1000
    w23.centerX=-1000
    
    
