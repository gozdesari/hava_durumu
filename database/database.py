import boto3
import uuid
from decimal import Decimal

REGION = "eu-north-1"

dynamodb = boto3.resource("dynamodb", region_name=REGION)

weather_data_table = dynamodb.Table("weather_data")
weather_analysis_table = dynamodb.Table("weather_analysis")


def insert_data(data):
    weather_data_table.put_item(
        Item={
            "id": str(uuid.uuid4()),
            "city": data["city"],
            "temperature": Decimal(str(data["temperature"])),
            "humidity": int(data["humidity"]),
            "wind_speed": Decimal(str(data["wind_speed"])),
            "timestamp": data["timestamp"]
        }
    )


def get_last_temperatures(limit=5):
    response = weather_data_table.scan()
    items = response.get("Items", [])

    items = sorted(items, key=lambda x: x["timestamp"], reverse=True)

    temps = []
    for item in items[:limit]:
        temps.append(float(item["temperature"]))

    return temps


def insert_analysis(avg_temp, max_temp, warning, analysis_time):
    weather_analysis_table.put_item(
        Item={
            "id": str(uuid.uuid4()),
            "average_temperature": Decimal(str(avg_temp)),
            "max_temperature": Decimal(str(max_temp)),
            "warning": warning,
            "analysis_time": analysis_time
        }
    )