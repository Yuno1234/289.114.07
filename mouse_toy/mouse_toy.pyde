rainbow = [
    '#FF0000', '#FF9900', '#FFFF00',
    '#00FF00', '#0099FF', '#6633FF'
]

sw = 7

def setup():
    size(600, 600)
    background('#004477')
    frameRate(60)
    
def draw():
    global sw
    stroke( rainbow[frameCount % len(rainbow)] )
    strokeWeight(sw)
    
    if mousePressed:
        if mouseButton == LEFT:
            line(pmouseX, pmouseY, mouseX, mouseY)
        if mouseButton == RIGHT:
            sw += 1
        if mouseButton == CENTER:
            sw = 3
            
