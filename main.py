from timmy import app
import os


if __name__ == '__main__':
    while True:
        try:

            app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 4000)))
        except Exception as e:
            print(e)
            print("restart....")
