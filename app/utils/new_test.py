def test():
    return "This is a test function for GitHub integration."

def generate_user_report(users):
    report = {
        "total_users": len(users),
        "active_users": 0,
        "inactive_users": 0,
        "premium_users": 0,
        "emails": []
    }

    for user in users:
        if user["active"]:
            report["active_users"] += 1
        else:
            report["inactive_users"] += 1

        if user.get("premium", False):
            report["premium_users"] += 1

        report["emails"].append(user["email"])

    return report

password = "123456"

query = f"SELECT * FROM users WHERE id=user_input"