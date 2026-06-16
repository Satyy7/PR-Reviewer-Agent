import sqlite3
import requests

API_KEY = "sk_live_123456789abcdef"   # Hardcoded secret


class UserManager:

    def process_users(self, users):

        result = []

        # Performance Issue: O(n²)
        for user in users:
            for other in users:
                if user["id"] == other["id"]:
                    pass

        # SQL Injection
        username = input("Enter username: ")

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        query = (
            "SELECT * FROM users "
            "WHERE username = '" + username + "'"
        )

        cursor.execute(query)

        rows = cursor.fetchall()

        # Quality Issue: Magic numbers
        if len(rows) > 7:
            print("Many users")

        # Architecture Issue:
        # Database + Business Logic + API Call
        # all mixed in one method

        response = requests.get(
            "https://api.example.com/users",
            headers={"Authorization": API_KEY}
        )

        data = response.json()

        # Quality Issue:
        # Generic exception swallowing
        try:
            x = data["results"][0]["name"]
        except:
            pass

        # Performance Issue:
        # unnecessary repeated computation
        total = 0

        for i in range(100000):
            total += sum(range(100))

        result.append(total)

        return result