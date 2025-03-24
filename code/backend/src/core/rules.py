# Routes the request based on classification type
def route_request(classification):
    routing_rules = {
        "Money Movement": "payment_team",
        "Fee Payment": "finance_team",
        "Adjustment": "customer_service_team",
    }
    return routing_rules.get(classification['Request Type'], "general_team")
