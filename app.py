import os
import json
import glob
from flask import Flask, render_template


app = Flask(__name__)


def convert_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)

@app.route('/')
def index():
    path = 'Stanford_Speech_to_Text_Dump/*'
    all_files = glob.glob(path)
    data = []
    for file in all_files:
        file_name = os.path.basename(file)
        split_data = file_name.split('.')
        split_title = split_data[0].split('[')
        youtube_link = split_title[-1].replace(']', '')
        title = split_title[0]
        data.append([title, youtube_link, file_name])

    return render_template('index.html', data=data)




@app.route('/transcripts/<string:json_file>')
def get_transcript(json_file):
    json_file = f'Stanford_Speech_to_Text_Dump/{json_file}'
    f = open(json_file)
    res = json.load(f)

    audio_segments = res['segments']
    file_name = os.path.basename(json_file)
    split_data = file_name.split('.')
    split_title = split_data[0].split('[')
    youtube_link = split_title[-1].replace(']', '')
    title = split_title[0]
    data = []
    for i in range(len(audio_segments)):
        start_audio = audio_segments[i]['start']
        end_audio = audio_segments[i]['end']
        transcribed_text = audio_segments[i]['text']
        data.append([convert_time(start_audio), convert_time(end_audio), transcribed_text,  start_audio])
    return render_template('transcripts.html', data=data, title=title, youtube_link=youtube_link)


if __name__ == "__main__":
	app.run(port=8000)