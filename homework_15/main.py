import configs
import utils


def main():
    utils.download_file('downloads/story.pdf', configs.story_url)

    utils.download_json('downloads/data.json', configs.astros_url)


if __name__ == '__main__':
    main()
