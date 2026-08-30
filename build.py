#!/usr/bin/env python3
import base64, json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(ROOT, 'index_template.html')

def data_uri(path):
    ext = os.path.splitext(path)[1].lower().lstrip('.')
    mime = {'jpg':'jpeg','jpeg':'jpeg','png':'png','webp':'webp','gif':'gif'}.get(ext, ext)
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    return f'data:image/{mime};base64,{b64}'

def gallery_uris(folder):
    p = os.path.join(ROOT, 'assets', folder)
    files = sorted(os.listdir(p))
    return [data_uri(os.path.join(p, fn)) for fn in files if not fn.startswith('.')]

def build(output_path, lite=False):
    with open(TEMPLATE, 'r', encoding='utf-8') as f:
        html = f.read()

    logo = data_uri(os.path.join(ROOT, 'assets', 'logo.png'))
    avatar = data_uri(os.path.join(ROOT, 'assets', 'personal', 'dawid-avatar.jpg'))

    if lite:
        gallery_data = {}
    else:
        gallery_data = {
            'komunia': gallery_uris('komunia'),
            'koszwaly': gallery_uris('koszwaly'),
            'koszwaly_combo': gallery_uris('koszwaly_combo'),
            'podolewielkie': gallery_uris('podolewielkie'),
        }

    client_logos = {
        'blessedink_tatts': data_uri(os.path.join(ROOT, 'assets', 'client-logos', 'final', 'blessed_ink.jpg')),
        'game_over_gdansk': data_uri(os.path.join(ROOT, 'assets', 'client-logos', 'final', 'game_over.jpg')),
        'holy_burger_gdansk': data_uri(os.path.join(ROOT, 'assets', 'client-logos', 'final', 'holy_burger.jpg')),
        'podolewielkie': data_uri(os.path.join(ROOT, 'assets', 'client-logos', 'final', 'podolewielkie.jpg')),
        'popierogu_koszwaly': data_uri(os.path.join(ROOT, 'assets', 'client-logos', 'final', 'koszwaly.jpg')),
        'zafishowani': data_uri(os.path.join(ROOT, 'assets', 'client-logos', 'final', 'zafishowani.jpg')),
    }

    html = html.replace('__LOGO__', logo)
    html = html.replace('__AVATAR_DAWID__', avatar)
    html = html.replace('__GALLERY_DATA__', json.dumps(gallery_data))
    html = html.replace('__CLIENT_LOGOS__', json.dumps(client_logos))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Built {output_path} ({os.path.getsize(output_path):,} bytes)')

def gallery_paths(folder):
    p = os.path.join(ROOT, 'assets', folder)
    files = sorted(os.listdir(p))
    return [f'assets/{folder}/{fn}' for fn in files if not fn.startswith('.')]

def build_web(output_path):
    """Build a version of the site that references images via relative paths
    instead of embedding them as base64 data URIs. This keeps the HTML file
    small (a few hundred KB instead of ~11MB) for uploading via tools with
    file-size limits, and for better real-world web performance (browser
    caching, parallel loading) once deployed."""
    with open(TEMPLATE, 'r', encoding='utf-8') as f:
        html = f.read()

    logo = 'assets/logo.png'
    avatar = 'assets/personal/dawid-avatar.jpg'

    gallery_data = {
        'komunia': gallery_paths('komunia'),
        'koszwaly': gallery_paths('koszwaly'),
        'koszwaly_combo': gallery_paths('koszwaly_combo'),
        'podolewielkie': gallery_paths('podolewielkie'),
    }

    client_logos = {
        'blessedink_tatts': 'assets/client-logos/final/blessed_ink.jpg',
        'game_over_gdansk': 'assets/client-logos/final/game_over.jpg',
        'holy_burger_gdansk': 'assets/client-logos/final/holy_burger.jpg',
        'podolewielkie': 'assets/client-logos/final/podolewielkie.jpg',
        'popierogu_koszwaly': 'assets/client-logos/final/koszwaly.jpg',
        'zafishowani': 'assets/client-logos/final/zafishowani.jpg',
    }

    html = html.replace('__LOGO__', logo)
    html = html.replace('__AVATAR_DAWID__', avatar)
    html = html.replace('__GALLERY_DATA__', json.dumps(gallery_data))
    html = html.replace('__CLIENT_LOGOS__', json.dumps(client_logos))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Built {output_path} ({os.path.getsize(output_path):,} bytes)')

if __name__ == '__main__':
    build(os.path.join(ROOT, 'index.html'), lite=False)
    build(os.path.join(ROOT, 'oship-agency-strona-podglad-lite.html'), lite=True)
    build_web(os.path.join(ROOT, 'index-web.html'))
