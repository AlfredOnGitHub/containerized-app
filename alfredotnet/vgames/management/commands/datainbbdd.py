from django.core.management.base import BaseCommand
from vgames.models import vGame
import random

class Command(BaseCommand):
    info = 'Populate the DB with vGames'

    def handle(self, *args, **kwargs):

        vGame.objects.all().delete()
        titles = ["Game " + str(i) for i in range (1,101)]
        genres = ["Action", "Adventure", "RPG", "Shooter", "Strategy"]
        platforms = ["PC", "PlayStation", "XBOX", "Nintendo Switch"]

        for title in titles:
            game = vGame(
                title=title,
                genre=random.choice(genres),
                platform=random.choice(platforms),
                release_year=random.randint(2000, 2024),
                rating=round(random.uniform(1.0, 10.0), 1)
            )

            game.save()
        self.stdout.write(self.style.SUCCESS('Database populated with vGames'))