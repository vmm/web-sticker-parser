"""
    Parses the sticker metadatafiles and creates
    a JS module which can be imported to the website

    The created file contains the minimum amount of data so all
    duplicate info, like thumnail URLs are dropped out

"""
import json

# TODO: Get the paths from env
STICKER_ROOT = "https://d33e9um4nuyldw.cloudfront.net/stickers"
METADATA_FOLDER = "downloads"
METADATA_FILE = "metadata"
CONTENT_PATH = "content"
RESULT_FILE = "src/index.js"
THUMBNAIL_EXTENSION = "-thumbnail.png"

# The final object which holds the categories
# in a sorted list
sticker_json = []

# first read the original metadata file
# which contains all sticker categories
# and their order
with open("%s/%s" % (METADATA_FOLDER, METADATA_FILE)) as data_file:
    data = json.load(data_file)

packages = data.get("packages")
# Sort the packages per the sort index
packages.sort(key=lambda x: x.get("sortindex"))

for p in packages:
    category_path = p.get("path")
    category_name = p.get("name")
    sort_index = p.get("sortindex")
    category_thumbnail = "%s%s" % (category_name, THUMBNAIL_EXTENSION)

    # Read the sticker metadata file from the path
    category_file = "%s/%s/%s" %(METADATA_FOLDER, category_path, METADATA_FILE)
    with open(category_file) as data_file:
        category_data = json.load(data_file)

    # Each metadata file has a "items" list
    # which contains the filenames
    items = category_data.get("items")
    # sort them using the sort index
    items.sort(key=lambda x: x.get("sortindex"))

    # carrying the name of thumbnail and a file would
    # just double the JS file size -> just store the filename
    # and the prefix for full sized and thumbnail sized images
    first_item = items[0]
    example_name = first_item.get("name")
    file_extension = first_item.get("file")[len(example_name):]
    thumnbail_extension = first_item.get("thumbnail")[len(example_name):]

    sticker_json.append(
        {
            "name": category_name,
            "path": "%s/%s" % (category_path, CONTENT_PATH),
            "thumbnail": category_thumbnail,
            "extension": file_extension,
            "thumbnail-extension": thumnbail_extension,
            "sort-index": sort_index,
            "stickers": [
                "%s" % (item.get("name")) for item in items
            ]
        }
    )

# Return an object which holds the
# url of the stickers and the categories sorted
stickers = {
    "url": STICKER_ROOT,
    "categories": sticker_json
}

result_json = json.dumps(stickers)


# Finally create a node module out of it
ret = """var Stickers = %s

module.exports = Stickers;
""" % result_json

obj = open(RESULT_FILE, 'wb')
obj.write(ret)
obj.close
