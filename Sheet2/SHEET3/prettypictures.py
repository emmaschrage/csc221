from gasp import *
begin_graphics()

x = 100
y = 400
def face(x, y):
    Circle((x, y), 40)
    Circle((x + 15, y + 10), 5)
    Circle((x - 15, y + 10), 5)
    Line((x - 5, y - 10), (x, y + 10))
    Line((x - 5, y - 10), (x + 10, y - 10))
    Arc((x, y + 5), 30, 225, 315)
    Line((x - 20, y + 20), (x - 10, y + 20))
    Line((x + 25, y + 15), (x + 20, y + 20))
    Line((x - 25, y + 15), (x - 20, y + 20))
    Line((x + 20, y + 20), (x + 10, y + 20))
    Line((x - 5, y + 40), (x + 5, y + 40))
    Line((x + 5, y + 40), (x + 40, y + 20))
    Line((x + 40, y + 20), (x + 45, y - 50))
    Line((x - 5, y + 40), (x - 40, y + 20))
    Line((x - 40, y + 20), (x - 45, y - 50))
    Line((x, y - 40), (x, y - 90))
    Line((x, y - 90), (x - 30, y - 110))
    Line((x, y - 90), (x + 30, y - 110))
    Line((x, y - 65), (x - 25, y - 55))
    Line((x, y - 65), (x + 25, y - 55))

print(face(x, y))
face(200, 400)
face(300, 400)
face(400, 400)
face(500, 400)

Line((270, 440),(330, 440))
Line((280, 440), (280, 470))
Line((320, 440), (320, 470))
Line((280, 470), (320, 470))


update_when('key_pressed')
end_graphics()