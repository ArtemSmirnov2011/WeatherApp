from modules import application, main_window

city_name = "Дніпро"

def main():
    try:
        main_window.show()
        application.exec()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main() 