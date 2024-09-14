from flask import (
    Blueprint,
    jsonify,
    request,
    Response,
    stream_with_context
)
from flask_login import login_required
from website.scripts.helpers import get_image_link
import requests


api = Blueprint('api', __name__)


@api.route('/get-disk-data')
@login_required
def get_files():
    dir_path = request.args.get('dir_path')
    disk_link = request.args.get('disk_link')

    query = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key=https%3A%2F%2Fdisk.yandex.ru%2Fd%2F{
        disk_link.split('/').pop()
    }'

    if dir_path != None:
        query += f'&path=%2F{dir_path[1:]}'

    response = requests.get(query)

    all_files = []

    for item in response.json()['_embedded']['items']:
        if item['type'] != 'dir':
            item['image_link'] = get_image_link(item['media_type'])
        else:
            item['image_link'] = '../static/svg/folder.svg'

        all_files.append(item)

    return jsonify({'data': all_files})


@api.route('/handle-ya-download', methods=['POST'])
def handle_ya_download():
    link = request.json.get('link')
    name = request.json.get('name')

    response = requests.get(link, stream=True)

    if response.status_code == 200:
        content_type = response.headers.get(
            'Content-Type', 'application/octet-stream'
        )

        content_disposition = response.headers.get(
            'Content-Disposition', f'attachment; filename={name}'
        )

        return Response(
            stream_with_context(response.iter_content(chunk_size=8192)),
            headers={
                'Content-Type': content_type,
                'Content-Disposition': content_disposition
            }
        )
    else:
        return "Failed to download file", 500
