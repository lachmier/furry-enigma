from PIL import Image
import requests
from io import BytesIO
import json
import argparse


def resize(img_height, img_width, new_width=1000):
    if img_width < img_height:
        if img_width <= 400:
            new_width = int(img_width * 2)
        else:
            new_width = img_width
        new_height = int(img_height * (new_width / img_width))
    else:
        new_height = int(img_height * (new_width / img_width))
    return (new_width, new_height)


def get_image(nr, info, width: int):
    if nr:
        api_resp = json.loads(requests.get(f"https://xkcd.com/{nr}/info.0.json").text)
    else:
        api_resp = json.loads(requests.get("https://xkcd.com/info.0.json").text)

    img_url = api_resp.get("img")

    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    new_size = resize(img.height, img.width, width)
    new_img = img.resize(new_size)
    new_img.show()

    if info:
        from pygments import highlight, lexers, formatters

        colorful_json = highlight(
            json.dumps(api_resp, sort_keys=True, indent=4),
            lexers.JsonLexer(),
            formatters.TerminalFormatter(),
        )
        print(colorful_json)
        print(new_img.size)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--get_num", required=False, default=False)
    parser.add_argument("--get_info", required=False, default=False)
    parser.add_argument("--set_width", type=int, required=False, default=1200)
    known_args, _ = parser.parse_known_args(argv)

    get_image(known_args.get_num, known_args.get_info, known_args.set_width)


if __name__ == "__main__":
    main()
