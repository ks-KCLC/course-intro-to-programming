import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("キャラクター移動")

GRAVITY = 0.5  # 重力加速度（フレームごとに加算される落下速度）
JUMP_POWER = -12  # ジャンプ初速（負 = 上向き）
CHARACTER_SIZE = 40  # キャラクターのサイズ
GROUND_Y = 400  # 地面の y 座標（キャラ下端の位置）

x = 300
y = GROUND_Y - 40  # 地面の上に配置（高さ 40px 分を引く）
vy = 0  # y 軸方向の速度
on_ground = True  # 地面に接触しているか

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # キーを押した瞬間だけジャンプ（押しっぱなしで連続ジャンプしない）
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and on_ground:
                vy = JUMP_POWER
                on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5

    # 重力を毎フレーム速度に加算
    vy += GRAVITY
    y += vy

    # 地面との衝突判定
    if y >= GROUND_Y - CHARACTER_SIZE:
        y = GROUND_Y - CHARACTER_SIZE
        vy = 0
        on_ground = True

    screen.fill(pygame.Color("black"))
    # 地面を描画
    pygame.draw.line(screen, pygame.Color("gray"), (0, GROUND_Y), (640, GROUND_Y), 2)
    # キャラクターを描画
    pygame.draw.rect(
        screen, pygame.Color("white"), (x, y, CHARACTER_SIZE, CHARACTER_SIZE)
    )
    pygame.display.update()
    clock.tick(60)

pygame.quit()
