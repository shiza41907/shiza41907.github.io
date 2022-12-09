

def draw():
    screen.fill((0, 0, 0))
    
    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (300, 388)
        ),
        color=(35, 92, 118)
    )
    def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (300, 388)
        ),
        color=(35, 92, 118)
    )

    screen.draw.filled_rect(
        Rect(
            (62, 200),
            (30, 25)
        ),
        color=(224, 214, 68)
    )
    bird_y = 200

def update(dt):
    global bird_y
    
    bird_y += 30 * dt

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (300, 388)
        ),
        color=(35, 92, 118)
    )

    screen.draw.filled_rect(
        Rect(
            (62, bird_y),
            (30, 25)
        ),
        color=(224, 214, 68)
    )
    bird_y = 200
bird_y_speed = 0

def update(dt):
    global bird_y
    global bird_y_speed

    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (300, 388)
        ),
        color=(35, 92, 118)
    )

    screen.draw.filled_rect(
        Rect(
            (62, bird_y),
            (30, 25)
        ),
        color=(224, 214, 68)
    )
    bird_y = 200
bird_y_speed = 0

def update(dt):
    global bird_y
    global bird_y_speed

    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt

def on_key_down():
    global bird_y_speed
    
    bird_y_speed = -165

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (300, 388)
        ),
        color=(35, 92, 118)
    )

    screen.draw.filled_rect(
        Rect(
            (62, bird_y),
            (30, 25)
        ),
        color=(224, 214, 68)
    )
    bird_y = 200
bird_y_speed = 0

def update(dt):
    global bird_y
    global bird_y_speed

    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt

def on_key_down():
    global bird_y_speed

    if bird_y > 0:
        bird_y_speed = -165

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (300, 388)
        ),
        color=(35, 92, 118)
    )

    screen.draw.filled_rect(
        Rect(
            (62, bird_y),
            (30, 25)
        ),
        color=(224, 214, 68)
    )