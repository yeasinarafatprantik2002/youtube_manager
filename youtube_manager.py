import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            videos = json.load(file)
            return videos

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_youtube_video(videos):

    print("\n" + "*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"\n{index}. Title: {video['title']}\n   Duration: {video['time']}")
    print("\n" + "*" * 70)


def add_youtube_video(videos):
    title = input("Enter the title: ")
    time = input("Enter video time: ")

    video = {"title": title, "time": time}
    videos.append(video)

    save_data(videos)


def update_youtube_video(videos):
    list_all_youtube_video(videos)
    index = int(input("Enter the video number to update: "))

    if 1 <= index <= len(videos):
        title = input("Enter the new video title: ")
        time = input("Enter the new video time: ")

        videos[index - 1] = {"title": title, "time": time}
        save_data(videos)
    else:
        print("Invalid index selected")


def delete_youtube_video(videos):
    list_all_youtube_video(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        print(f"{index}. Video deleted successfully")
        save_data(videos)
    else:
        print("Invalid video index selected")


def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube video")
        print("2. Add a youtube video")
        print("3 Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_youtube_video(videos)

            case "2":
                add_youtube_video(videos)

            case "3":
                update_youtube_video(videos)

            case "4":
                delete_youtube_video(videos)

            case "5":
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
