# Digital Garden - click to plant, C to clear
# Drawing basics adapted from the class example:
# the_circle_purple

def setup():
    size(800, 600)
    background(245, 240, 230)


def draw():
    fill(90, 100, 80)
    textSize(16)
    text("Click to plant | C: clear | S: save image", 20, 30)


# Plant a flower at the mouse position
def mousePressed():
    if mouseY > 90:
        draw_flower(mouseX, mouseY)

def draw_flower(flower_x, flower_y):
    # Green stem
    stroke(100, 145, 95)
    strokeWeight(6)
    line(flower_x, flower_y, flower_x, flower_y + 180)
        # Green leaves
    strokeWeight(1)
    stroke(100, 145, 95)
    fill(130, 175, 110)
    ellipse(flower_x - 20, flower_y + 100, 40, 20)
    ellipse(flower_x + 20, flower_y + 130, 40, 20)

    # Pink petals
    strokeWeight(1)
    stroke(225, 145, 170)
    fill(random(150, 255), random(100, 220), random(150, 255))
    ellipse(flower_x - 25, flower_y, 50, 50)
    ellipse(flower_x + 25, flower_y, 50, 50)
    ellipse(flower_x, flower_y - 25, 50, 50)
    ellipse(flower_x, flower_y + 25, 50, 50)

    # Yellow centre
    fill(250, 215, 110)
    ellipse(flower_x, flower_y, 30, 30)


# Press C to clear the garden
def keyPressed():
    if key == 'c' or key == 'C':
        background(245, 240, 230)
    elif key == 's' or key == 'S':
        saveFrame("garden-####.png")
