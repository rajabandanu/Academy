# Snake Game (Pygame)

A short walkthrough of the Snake Game code built with Python + Pygame.

## How It Works

### 1. Initial Setup
```python
pygame.init()
frame_size_x = 720
frame_size_y = 480
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
fps_controller = pygame.time.Clock()
```
Creates a 720x480 window and a clock to control the FPS (frames per second).

### 2. Snake & Apple Variables
```python
snake_pos = [100, 50]              # snake head position
snake_body = [[100,50],[90,50],[80,50]]  # body segments (list of [x,y])
apple_pos = [...]                  # random apple position, snapped to multiples of 10
apple_spawn = True                 # whether the apple needs to respawn
```
Every segment and position moves in steps of 10 pixels, keeping everything aligned to a grid.

### 3. Direction Handling
```python
if change_to == 'UP' and direction != 'DOWN':
    direction = 'UP'
```
`change_to` is set from keyboard input, but only applied to `direction` if it isn't the opposite of the current direction — this stops the snake from instantly reversing into itself.

### 4. Movement
```python
if direction == 'UP':
    snake_pos[1] -= 10
```
The head position updates according to the current direction, 10 pixels per step.

### 5. Eating the Apple
```python
snake_body.insert(0, list(snake_pos))
if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
    apple_spawn = False
    score += 1
else:
    snake_body.pop()
```
A new head segment is always inserted at the front. If the head lands on the apple → the body grows (the tail is *not* popped) and the score increases. If not → the tail segment is removed, so the snake's length stays the same (creating the "movement" effect).

### 6. Rendering
```python
for pos in snake_body:
    pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
pygame.draw.rect(game_window, red, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10))
```
Each body segment is drawn as a 10x10 green square, and the apple as a red square.

### 7. Score Display
```python
score_font = pygame.font.SysFont('Arial', 20)
score_surface = score_font.render(str(score), True, white)
game_window.blit(score_surface, score_rect)
```
The score is shown at the top of the screen.

### 8. Input & Quitting
```python
if event.key == pygame.K_ESCAPE:
    pygame.event.post(pygame.event.Event(pygame.QUIT))
```
Arrow keys control movement, ESC quits the game (by posting a QUIT event).

---

## ⚠️ Things That Still Need Fixing

The code **already runs** and the snake can move and eat apples, but a few key pieces — typically standard in a snake game — are still missing:

1. **No collision detection (game over).**
   Right now the snake can:
   - Hit a wall → it just keeps going (position goes negative or past the screen edge, so the snake "disappears" from view but the game doesn't stop).
   - Hit its own body → not detected at all.

   You'd want to add something like:
   ```python
   def game_over():
       # check screen boundaries
       if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
           return True
       if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
           return True
       # check self-collision
       for block in snake_body[1:]:
           if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
               return True
       return False
   ```
   Then call it every loop iteration, and if it returns `True`, show the final score and call `pygame.quit(); sys.exit()`.

2. **The apple can spawn on top of the snake's own body** — there's no check to prevent the apple from appearing where the snake already is.

3. **`print(change_to)` inside the loop** — this is just leftover debug code and will print hundreds of lines to the console every second. Best removed in the final version.

4. **Render order vs. event polling** — the code currently draws the frame first and checks events at the end of the loop. This is usually fine for a simple game, but it's more common to poll events at the **start** of the loop so input feels more responsive.

Let me know if you'd like help adding the game-over feature and the apple/body-overlap check to make it a complete, playable version.
