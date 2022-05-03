from urllib.request import Request, urlopen
from json import loads
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')

def GetLink(LinkType=None):
	if LinkType == None:
		LinkType = 'gpl-shared'
		try:
			LinkType = config['get']['LinkType']
		except:
			pass
	req = Request(
		'https://api.github.com/repos/BtbN/FFmpeg-Builds/releases/latest')
	try:
		res = urlopen(req)
	except:
		return []
	LatestData = loads(res.read().decode())
	LinkTypes = ['gpl-shared-vulkan', 'gpl-shared', 'gpl-vulkan',
				 'gpl', 'lgpl-shared-vulkan', 'lgpl-shared', 'lgpl-vulkan', 'lgpl']
	if not (LinkType in LinkTypes):
		raise IndexError('LinkType not support.', LinkType, LinkTypes)
	url = ''
	for asset in LatestData['assets']:
		if asset['name'].find('win64-%s.zip' % LinkType) >= 0:
			url = asset['browser_download_url']
	return url