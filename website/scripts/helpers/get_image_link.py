def get_image_link(media_type):
    if media_type == 'image':
        return '../static/svg/image.svg'
    elif media_type == 'document':
        return '../static/svg/document.svg'
    elif media_type == 'compressed':
        return '../static/svg/disk.svg'
    elif media_type == 'video':
        return '../static/svg/video.svg'
    elif media_type == 'audio':
        return '../static/svg/music.svg'
    else:
        return '../static/svg/disk.svg'
