is_gun_ready = bool(int(input('is_gun_ready: ')))
ammo_count = int(input('Input ammo_count: '))
should_fire = is_gun_ready and ammo_count > 0
print(should_fire)