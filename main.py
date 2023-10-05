player = {
    'name': 'nico',
    'age': 12,
    'alive': True,
	'fav_food':["🍕", "🍔"]
}
player['fav_food'].append("🍜")
print(player.get('fav_food'))
print(player['fav_food'])