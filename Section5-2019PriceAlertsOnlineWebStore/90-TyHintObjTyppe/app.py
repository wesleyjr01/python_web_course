from models.alert import Alert

alert = Alert(item_id="26beafafee7e4391a02d54b54fe90d73", price_limit=2000)
alert.save_to_mongo()
