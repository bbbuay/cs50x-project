import os
import csv
from guidance.models import Guidance
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.conf import settings
from django.core.files import File


class Command(BaseCommand):
    help = "Command to add demo data from the specified csv file path into the database"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("file_path", type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        # get the file path
        csv_file = os.path.join(settings.BASE_DIR, options["file_path"])
        print(csv_file)

        with open(csv_file, mode="r") as file:
            reader = csv.DictReader(file)

            ncreated = 0
            for row in reader:
                img_name = row["image"]
                img_path = os.path.join('demo_data/guidance_images', img_name)

                with open(img_path, 'rb') as file:
                    image = File(file)
                    # make sure that we will use the only file name (ex. img_001.jpg) as the final destination
                    # os.path.basename: extract the only file name from img_path (data/demo_images/img_001.jpg -> img_001.jpg)
                    image.name = os.path.basename(img_path) 
                    Guidance.objects.create(
                        title = row["title"],
                        content = row["content"],
                        religion = row["religion"],
                        image = image,
                    )
                    ncreated += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully add {ncreated} demo guidances"))
