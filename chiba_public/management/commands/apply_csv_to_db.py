from django.core.management.base import BaseCommand, CommandError
from chiba_public.models import Facility, Category
import pandas as pd

ORIGIN_COLUMNS = [
    'ページタイトル', '施設ジャンル', '施設、場所、イベントの名称（読み）', '住所', '緯度', '経度'
]

NAMED_COLUMNS = [
    'name', 'category', 'name_kana', 'address', 'latitude', 'longitude'
]


class Command(BaseCommand):
    help = 'apply csv data to db.'

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='+', type=str)

    def apply_category(self, category_names):
        current_categories = Category.objects.all().values_list('name', flat=True)
        current_categories = set(list(current_categories))
        add_names = list(category_names - current_categories)

        categories = []
        for name in add_names:
            category = Category(name=name)
            categories.append(category)
        Category.objects.bulk_create(categories)

    def generate_reversed_category_dict(self):
        categories = Category.objects.all().values_list('id', 'name')
        categories = list(categories)
        categories = map(lambda x: tuple(reversed(x)), categories)
        categories = dict(list(categories))
        return categories

    def apply_facility(self, read_data):
        categories = self.generate_reversed_category_dict()

        facilities = []
        for data in read_data.itertuples():
            if pd.isnull(data.name) or pd.isnull(data.latitude) or pd.isnull(data.longitude):
                continue
            category_id = categories[data.category]
            category = Category(id=category_id, name=data.category)
            facility = Facility(
                name=data.name, category=category, name_kana=data.name_kana, address=data.address, latitude=data.latitude, longitude=data.longitude
            )
            facilities.append(facility)
        Facility.objects.bulk_create(facilities)

    def handle(self, *args, **options):
        try:
            file_name = options['file_name'][0]

            if not file_name[-4:] == '.csv':
                raise CommandError

            read_data = pd.read_csv(file_name, usecols=ORIGIN_COLUMNS)
        except CommandError as e:
            print('command is only read csv file!')
            exit(1)

        read_data.columns = NAMED_COLUMNS
        category_names = set(read_data['category'])

        self.apply_category(category_names=category_names)

        Facility.objects.all().delete()
        self.apply_facility(read_data=read_data)

        print('operation succeeded.')
