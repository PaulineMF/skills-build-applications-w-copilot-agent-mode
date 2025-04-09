# Test data for populating the octofit_db database

test_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "description": "A competitive team focused on fitness."},
    {"name": "Team Beta", "description": "A fun team for casual fitness enthusiasts."},
]

test_activities = [
    {"user": "john_doe", "activity_type": "Running", "duration": 30, "calories_burned": 300},
    {"user": "jane_smith", "activity_type": "Cycling", "duration": 45, "calories_burned": 400},
]

test_leaderboard = [
    {"user": "john_doe", "points": 100},
    {"user": "jane_smith", "points": 120},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick run to start the day.", "duration": 30},
    {"name": "Evening Yoga", "description": "Relaxing yoga session.", "duration": 60},
]
