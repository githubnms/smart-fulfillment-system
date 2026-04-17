def get_inventory(db):
    return db.query(Inventory).all()