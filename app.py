from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    file_type = data.get('type')

    try:
        yt = YouTube(url)
        if file_type == 'mp3':
            audio = yt.streams.filter(only_audio=True).first()
            return jsonify({"status": "success", "message": "MP3 indiriliyor!", "title": yt.title})
        elif file_type == 'mp4':
            video = yt.streams.get_highest_resolution()
            return jsonify({"status": "success", "message": "MP4 indiriliyor!", "title": yt.title})
        else:
            return jsonify({"status": "error", "message": "Geçersiz format!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
