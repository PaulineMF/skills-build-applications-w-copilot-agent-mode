import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import *  # Import your models here

# Add test data
def populate():
    # Example: Adding a user
    user = User.objects.create_user(username='testuser', password='testpassword')
    print(f"Created user: {user.username}")

    # Example: Adding other models
    # Add your test data logic here

if __name__ == "__main__":
    print("Populating database with test data...")
    populate()
    print("Database population complete.")
