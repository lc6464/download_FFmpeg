from urllib.request import urlretrieve
import os, zipfile, re
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')


def extract(file):
	with zipfile.ZipFile(file) as zf:
		zf.extractall()
		for info in zf.infolist():
			if re.match(r'^ffmpeg-N-[^/]{25,45}/$', info.filename) != None:
				return os.rename(info.filename[:-1], 'ffmpeg')


def download(url):
	return urlretrieve(url, 'ffmpeg.zip')[0]


def IDMDownload(url):
	path = config['download']['IDMPath']
	return os.system('%s /d %s /p %s /f ffmpeg.zip /q /n' % (path, url, os.getcwd()))