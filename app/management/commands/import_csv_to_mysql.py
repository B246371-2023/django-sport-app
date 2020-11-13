
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from app.models import Performance  # 修改 'app' 为您的应用名称
import pandas as pd

class Command(BaseCommand):
    help = 'Import CSV data into Performance model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    @transaction.atomic  # 使用数据库事务确保导入的原子性
    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']

        try:
            # 读取 CSV 文件
            df = pd.read_csv(csv_file_path)

            # 遍历 DataFrame 的每一行并创建 Performance 实例
            for index, row in df.iterrows():
                Performance.objects.create(
                    player_name=row['Name'],
                    date=datetime.strptime(row['Date (DD/MM/YYYY)'], '%d-%m-%Y').date(),
                    session=row['Session'],
                    speed=row['Speed'],
                    distance_covered=row['Distance Covered'],
                    # 以下为示例，请根据您的模型字段调整
                    step_counts=row['Step Counts'],
                    stress_levels=row['Stress Levels'],
                    hydration_status=row['Hydration Status'],
                    heart_rate=row['Heart Rate(BPM)'],
                    calorie_expenditure=row['Calorie Expenditure(kal)'],
                    sleep_quality=row['Sleep Quality'],
                    # 如果 CSV 中有字段不需要导入，或者模型中有其他需要的字段，请相应调整
                )

            self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV to database'))
        except Exception as e:
            raise CommandError(f'Error importing data from CSV: {e}')
