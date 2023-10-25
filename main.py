###### -- READ THIS --#######################################################################
# You should implement the methods in the order of the numbers each method has assigned to it
# E.g start with nr #1 load_data, then move on to nr #2 the __init__-method
# This is just a recommendation, it's up to you!

# Methods in the "Menu" class will usually have a corresponding or related method in the "VideoGameDatabase" class
# This means that usually the Menu will have methods that call the methods in the VideoGameDatabase class
# Feel free to add a few more methods if needed (optional)

# The purpose of this lab is to practice on separation of concerns.
# The VideoGameDatabase class should only be responsible for handling the data, while the Menu class is responsible for the presentation logic (print, input, etc)
# The Database-class should raise exceptions when needed, and the Menu is the only responsible for handling these exceptions
# In practice, we should be able to use the Database-class with other classes that might want to use the same data
# Such as a tkinter-based app, or a web application.
############################################################################################


import pandas as pd
import json


class VideoGameDatabase:
    """
    This class is responsible for providing some simple methods for using data that stems from a video game database
    It should be reusable - this means you should never use "input()" or "print()" inside it. That is the responsibility of
    The "Menu" class defined below this class
    This class should raise exceptions (you can create custom exceptions or use built in ones) when something goes wrong 
    """

    # You could potentially provide a list of games when creating the class, but normally it should
    # attempt to load the data from the the default filename
    def __init__(self, games=None, filename="steam.json"):
        # 2
        self.video_games_df = pd.DataFrame()

    def load_data(self):
        # 1
        self.video_games_df = pd.read_json('steam.json')
        print("We fetched data")
        return self.video_games_df

        # Gammal kod som var som första labbarna.
        # with open('steam.json', 'r') as file:
        #     data = json.load(file)
        #     self.video_games = data
        #     print("We fetched data")
        # return data


        # """
        # - This method should load the video game data from the json-file
        # - It should be run ONCE when the class is created / instantiated
        # """
        # pass

    def search_game(self, word_to_search_for: str = None, app_id: int  = None) -> dict: # Här sätter jag default värden till None.
        # 4

        if word_to_search_for:
            result_df = self.video_games_df[self.video_games_df['name'].str.contains(word_to_search_for, case=False, na=False)]
            print(f"Hi, we have this/these in stock! \n {result_df}")
            return result_df[0]
        elif app_id:
            result_df = self.video_games_df[self.video_games_df['appid'] == app_id]
            print(f"Hi, we have this/these in stock! \n {result_df}")
            return result_df[0]
        else:
            if not result_df.empty:
                return result_df.iloc[0].to_dict()  # Return the first matched game as a dictionary
            else:
                raise KeyError(f"Game with word {word_to_search_for} or app_id {app_id} not found.")
            

            
            # if filtered_df == True:
            #     print(f"Hi, we have {filtered_df} in stock!")
            #     return filtered_df
            # else:
            #     print(f"We couldn't find {word_to_search_for} with appid {app_id} in stock.")
            #     return None
            
            # for game in self.video_games:
            # if game["name"].lower() == word_to_search_for.lower() and game["appid"] == app_id:
            #     filtered_df = self.video_games.loc[self.video_games['name'].str.contains('Cross', case=False, na=False)]
            #     print(f"Hi, we have {game['name']} in stock!")
            #     return game
        


        # if app_id == self.video_games["appid"]:
        #     print("Hi we got the video game in stock!")
        
        # """
        # - Should return the first video game with a "name" that either CONTAINS **or** COMPLETELY MATCHES the input word
        # - It should also be able to use an appip instead of the name for searching
        # - return the entire dictionary if it exists
        # - raise a "KeyError" exception if it did not exist
        # This method can be used both from the outside of the class AND from other methods inside the class
        # You will probably use it a lot
        # """
        # pass

    def get_price(self, game: str) -> float:
        # 6
        
        if self.video_games_df.empty:
            print("Data hasn't been loaded. Please load the data first.")
            return

        matching_rows = self.video_games_df[self.video_games_df['name'] == game]
        if matching_rows.empty:
            print(f"Couldn't find the game: {game}")
            return
        try:
            game_price = matching_rows['price'].values[0]
            print(f"Hi, this is the price of the game {game}: {game_price}")
            return game_price
        except:
            raise KeyError


        

        """
        - Should return the price of the game
        - raise a "KeyError" exception if the game did not exist
        """
        pass

    def _get_rating(self, game: dict) -> float:
        # 8

        rating_positive = self.video_games_df["positive_ratings"]
        rating_negative = self.video_games_df["negative_ratings"]

        rating_divided = float(rating_positive + rating_negative)

        if rating_divided == 0:
            return 0.0

        try: 
            rating = float(rating_positive / rating_divided)
        except ZeroDivisionError:
            ZeroDivisionError
        print(rating)
        return rating 

        """
        This is a non-public method (should never be called from outside the class)
        which should receive a game as a parameter and calculate the rating for it
        The rating should be a calculated by using the positive_ratings and negative_ratings.
        E.g rating = positive_ratings / (positive_ratings + negative_ratings)
        Return the rating as a float rounded to two decimals
        - *** DO NOT MODIFY THE ORIGINAL DATASET BY ADDING THIS AS A NEW PROPERTY, even if that makes it easier! ***
        """
        pass

    def compare_video_game_ratings(self, first_game, second_game) -> bool:
        # 9

        first_game_score = first_game._get_rating()
        second_game_score = second_game._get_rating()

        if first_game_score > second_game_score:
            return True
        elif second_game_score > first_game_score:
            return False
        elif second_game_score == first_game_score:
            print("The two games have the same rating, and the comparison could not be completed.")
        else:
            raise KeyError("Unable to complete the comparison between the two games.")

        """
        - Should based on "_get_rating" compare two game ratings (how good the game is considered by users)
        - Return True if the first game has a higher rating
        - Return False if the first game has a lower rating
        - raise a "KeyError" exception if the comparison was unable to be completed (make sure to handle it)
        """

        # Remove pass when you've added code
        pass

    def get_developer_games(self, developer: str) -> list:
        # 11

        if self.video_games_df.empty:
            print("Data hasn't been loaded. Please load the data first.")
            return []

        matching_rows = self.video_games_df[self.video_games_df['developer'] == developer]
        
        if matching_rows.empty:
            raise KeyError(f"Couldn't find any games by the developer: {developer}")
        
        game_name = matching_rows['name'].tolist()
        print(f"Games by {developer}: {game_name}")
        return game_name
        
        
        """
        - Should return a list of all games made by a developer
        - raise an exception if the developer did not exist in the dataset
        """

        # Remove pass when you've added code
        pass

    def get_game_by_genre(self, genre: str) -> list:
        # 13
        
        if self.video_games_df.empty:
            print("Data hasn't been loaded. Please load the data first.")
            return []

        matching_rows = self.video_games_df[self.video_games_df['developer'] == genre]
        
        if matching_rows.empty:
            raise KeyError(f"Couldn't find any games by the genre: {genre}")
        
        game_genre = matching_rows['name'].tolist()
        print(f"Games by genre: {genre} in this game {game_genre}")
        return game_genre
    
        """
        - Should return a list of all games with a specific genre
        - raise an exception if the genre did not exist in the dataset
        """

        # Remove pass when you've added code
        pass

    def average_owners(self, game: str) -> float:
        # 16

        

        """
        __NOT__ REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**
        - VG (Väl godkänt) REQUIREMENT ONLY

        - Should return the average number of owners for a game
        This is calculated by taking the ownership estimation span and dividing it by 2
        - raise an exception if the game did not exist
        Hint: use string-methods when you need to extract the numbers from the string
        """
        pass

    def list_latest_games(self, number_of_games_to_list) -> list:
        # 18
        """
        __NOT__ REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**
        - VG (Väl godkänt) REQUIREMENT ONLY

        This method should return a list of the latest video games ordered by release_date
        Use the datetime-module
        raise an exception of choice if something went wrong
        """

        # Remove pass when you've added code
        pass

    def popular_games(self, number_games_to_list: int) -> list:
        # 20
        """
        __NOT__ REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**
        - VG (Väl godkänt) REQUIREMENT ONLY


        - This method should return a list of X number of most popular video games
        based on the provided "number_games_to_list" parameter.
        - You should use the non-public _get_rating method to do this.
        - raise an exception (you choose yourself which one) if something went wrong

        Max number: 20
        Minimum number: 5
        Hint: sort the list & use a slice!
        """

        # Remove pass when you've added code
        pass

    # FEEL FREE TO ADD MORE METHODS IF YOU WANT / NEED TO


class Menu:
    """
    This class is responsible for handling the specific presentation logic of the application

    This means that the menu will be responsible for:
    1. asking the user for **inputs**
    2. Responsible of the **actual menu** -
    3. **reacting** to raised exceptions and telling the user what went wrong

    The "VideoGameDatabase" class might raise exceptions, but it should be the
    responsibility of the "Menu" class to react to these errors, e.g by asking them to try again
    or telling them what went wrong
    """

    def __init__(self):
        """
        You don't need to do anything here
        - An instance of the VideoGameDatabase is created
        - We are starting the menu-flow that should give the user a choice of what to do
        """
        self.obj = VideoGameDatabase(filename="steam.json")
        self.data_loaded = False
        self.start_main_menu()

    def start_main_menu(self):
        # 3
        while True:
            print("[1] - Show summary of a game")
            print("[2] - Show price of a game")
            print("[3] - Compare game ratings")
            print("[4] - Show developer games")
            print("[5] - Export video games from a genre of choice")
            print("[6] - (VG) Latest video games summary")
            print("[7] - (VG) Game average owners")
            print("[8] - (VG) List most popular games")
            print("[q] - Quit (no dedicated method required)")

            answer = input("Please select your choise")

            if answer == "1":
                self.show_game_summary()
            elif answer == "2":
                self.show_pricing()
            elif answer == "3":
                self.compare_ratings()
            elif answer == "4":
                self.show_developer_games()
            elif answer == "5":
                self.export_games_by_genre()
            elif answer == "6":
                self.latest_games()
            elif answer == "7":
                self.analyze_owner_estimation()
            elif answer == "8":
                self.list_popular_games()
            elif answer == "q":
                self.quit()

        """
        This should start a standard flow for a menu which asks the user what to do.
        Example:

        What would you like to do?
        [1] - Show summary of a game
        [2] - Show price of a game
        [3] - Compare game ratings
        [4] - Show developer games
        [5] - Export video games from a genre of choice
        [6] - (VG) Latest video games summary
        [7] - (VG) Game average owners
        [8] - (VG) List most popular games
        [q] - Quit (no dedicated method required)
        """
        # Remove pass when you've added code



    
    def show_game_summary(self):
            
            input_word_to_search_for = input("Enter the name of the game: ").strip()
            input_app_id = int(input("Enter the app_id: "))
            self.obj.load_data()
            self.obj.search_game(input_word_to_search_for, input_app_id)
            # 5


        # """
        # - Print a simple summary of a single game chosen by name or appid
        # - Ask the user for input and handle any raised exceptions
        # - Use the relevant / corresponding method in the Database class
        # - If you want (optional), you can also add some interesting information about the game, such
        # as how the price compares to the average of all game prices, if the average playtime is high or low compared to others
        # and so forth. Only do this once you have completed the other requirements (hint: this is easy to do with pandas).

        # Hint: First use the search-method in the Database class
        # """

        # # Remove pass when you've added code
        # pass

    def show_pricing(self):
        game = input("Enter the name: ")
        self.obj.get_price(game)

        # 7
        """
        Allow the user to check the price of a specific game
        - Should ask the user for the relevant input and handle any exceptions raised
        """
        pass

    def compare_ratings(self):
        # 10

        self.compare_video_game_ratings()

        """
        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

    def show_developer_games(self):
        # 12

        input_developer = input("developer name: ")
        try: 
            self.get_developer_games(input_developer)
        except:
            raise KeyError
        

        """
        - Should be able to show all games made by a specific game developer company
        - Should use the corresponding method in the Database class to show developer games
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

    def export_games_by_genre(self):
        # 14

        input_genre = input("please enter a genre")
        exported_data = self.get_game_by_genre(input_genre)
        with open("sample.json", "w") as outfile:
            outfile.write(exported_data)
        


        """
        - Should use the corresponding method in the Database class to export games by genre
        - Should ask the user for the relevant input and handle any exceptions raised
        - Should export these games to a new json-file
        """
        # Remove pass when you've added code
        pass

    def quit(self):
        # 15

        exit()

        """
        Should quit the program
        """
        pass

    def analyze_owner_estimation(self):
        # 17
        """
        - THIS METHOD IS NOT REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**
        - VG (Väl godkänt) REQUIREMENT ONLY

        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        - Should allow the user to input a game and then show the average number of owners for that game
        """
        pass

    def latest_games(self):
        # 19
        """
        - THIS METHOD IS NOT REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**
        - VG (Väl godkänt) REQUIREMENT ONLY

        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

    def list_popular_games(self):
        # 21
        """
        - THIS METHOD IS NOT REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**
        - VG (Väl godkänt) REQUIREMENT ONLY
        
        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

    # FEEL FREE TO ADD MORE METHODS IF YOU WANT / NEED TO


if __name__ == "__main__":
    menu = Menu()
