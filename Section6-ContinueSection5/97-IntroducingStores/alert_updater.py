from models.alert import Alert

alerts = Alert.get_all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")
