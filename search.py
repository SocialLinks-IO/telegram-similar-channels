#!/usr/bin/python3
import csv
import json

from transforms.GetSimilarTelegramChannels import get_similar_channels

if __name__ == "__main__":
	channel = input('Type a username of a Telegram channel to get similar channels: ')
	result = get_similar_channels(channel)

	for c in result.chats:
		print(f'{c.username}: {c.title}')

	print(f'There were {len(result.chats)} channels found')

	with open(f'{channel}.json', 'w', encoding='utf-8') as f:
		data = [{
			'id': c.id,
			'username': '|'.join([u.username for u in c.usernames]) if c.usernames else c.username,
			'title': c.title,
			'verified': c.verified,
			'participants_count': c.participants_count,
		} for c in result.chats]

		json.dump(data, f, ensure_ascii=False, indent=4)

	print(f'Data was successfully saved to {channel}.json')

	with open(f'{channel}.csv', 'w', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(['id', 'username', 'title', 'verified', 'participants_count'])
		for c in result.chats:
			usernames = '|'.join([u.username for u in c.usernames]) if c.usernames else c.username
			writer.writerow([c.id, usernames, c.title, c.verified, c.participants_count])

	print(f'Data was successfully saved to {channel}.csv')
