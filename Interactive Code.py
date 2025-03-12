class LogisticSystem:
    def __init__(self):
        self.shipments = {}

    def add_shipment(self, shipment_id, destination, weight):
        if shipment_id in self.shipments:
            print(f"Shipment ID {shipment_id} already exists.")
        else:
            self.shipments[shipment_id] = {
                'destination': destination,
                'weight': weight,
                'status': 'Pending'
            }
            print(f"Shipment {shipment_id} added successfully.")

    def display_shipments(self):
        if not self.shipments:
            print("No shipments available.")
        else:
            for shipment_id, details in self.shipments.items():
                print(f"ID: {shipment_id}, Destination: {details['destination']}, Weight: {details['weight']}kg, Status: {details['status']}")

# Example usage
logistic_system = LogisticSystem()
logistic_system.add_shipment("001", "NORTH FAIRVIEW", 10)
logistic_system.display_shipments()
