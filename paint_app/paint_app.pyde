def setup():
    size(600, 600)
    background('#004477')
    ernest = createFont('Ernest.ttf', 20)
    textFont(ernest)
    noLoop()
    
rainbow = [
    '#FF0000', '#FF9900', '#FFFF00',
    '#00FF00', '#0099FF', '#6633FF'
    ]
    
brushcolor = rainbow[0]
brushshape = ROUND
brushsize = 3
painting = False
paintmode = 'free'
clearall = False
    
def draw():
    global painting, paintmode
    
    if mouseX < 60:
        paintmode = 'select'
    
    if paintmode == 'free':
        if not painting and frameCount > 1:
            line(mouseX, mouseY, mouseX, mouseY)
            painting = True
        elif painting:
            print(frameCount)
            stroke(brushcolor)
            strokeCap(brushshape)
            strokeWeight(brushsize)
            line(pmouseX, pmouseY, mouseX, mouseY)
            
    # black panel
    noStroke()
    fill('#000000')
    rect(0, 0, 60, height)
            
    # color swatches
    fill(rainbow[0]); rect(0, 0, 30, 30)
    fill(rainbow[1]); rect(0, 30, 30, 30)
    fill(rainbow[2]); rect(0, 60, 30, 30)
    fill(rainbow[3]); rect(30, 0, 30, 30)
    fill(rainbow[4]); rect(30, 30, 30, 30)
    fill(rainbow[5]); rect(30, 60, 30, 30)
    
    # brush preview
    fill(brushcolor)
    if brushshape == ROUND:
        circle(30, 123, brushsize)
    paintmode = 'free'

    # clear button
    global clearall
    fill('#FFFFFF')
    text('clear', 10, height-12)
    
    if clearall:
        fill('#004477')
        rect(60, 0, width, height)
        clearall = False
    
def mousePressed():
    global brushcolor, brushshape, brushsize, clearall
    
    # clear button
    global clearall
    if mouseX < 60 and mouseY > height-30:
        clearall = True
        redraw
    
    if mouseButton == LEFT:
        loop()
        
        if mouseX < 30:
            if mouseY < 30:
                brushcolor = rainbow[0]
            elif mouseY < 60:
                brushcolor = rainbow[1]
            elif mouseY < 90:
                brushcolor = rainbow[2]
        elif mouseX < 60:
            if mouseY < 30:
                brushcolor = rainbow[3]
            elif mouseY < 60:
                brushcolor = rainbow[4]
            elif mouseY < 90:
                brushcolor = rainbow[5]
        
def mouseReleased():
    noLoop()
    global painting
    painting = False

def mouseWheel(e):
    print(e)
    global brushsize, paintmode
    
    paintmode = 'select'
    brushsize -= e.count
    
    if brushsize < 3:
        brushsize = 3
    if brushsize > 45:
        brushsize = 45
        
    redraw()
