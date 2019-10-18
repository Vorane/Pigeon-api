CREATED = "CRT"
AWAITING_FUNDS = "AWF"
INSUFFICIENT_FUNDS_FAILURE = "IFF"
READY_FOR_PROCESSING = "RFP"
RECEIVED_BY_STORE = "RBS"
IN_PROCESSING = "IPR"
AWAITING_SUBSTITUTION = "ASC"
IN_CHECKOUT = "ICH"
CANCELLED_BY_USER = "CUS"
READY_FOR_PICKUP = "RPK"
PICKED = "PKD"
NOT_PICKED = "NPK"
READY_FOR_DELIVERY = "RFD"
DELIVERY_IN_PROGRESS = "DIP"
DELIVERED = "DVD"
CANCELLED_BY_STORE = "CUT"

ORDER_STATUSES = (
    (CREATED, "Created"),
    (AWAITING_FUNDS, "Awaiting Funds"),
    (INSUFFICIENT_FUNDS_FAILURE, "Insufficient Funds Failure"),
    (READY_FOR_PROCESSING, "Ready For Processing"),
    (RECEIVED_BY_STORE, "Received By Store"),
    (IN_PROCESSING, "In Processing"),
    (AWAITING_SUBSTITUTION, "Awaiting Substitution Consent"),
    (IN_CHECKOUT, "In Checkout"),
    (CANCELLED_BY_USER, "Cancelled By User"),
    (READY_FOR_PICKUP, "Ready For Pickup"),
    (PICKED, "Picked"),
    (NOT_PICKED, "Not Picked"),
    (READY_FOR_DELIVERY, "Ready for delivery"),
    (DELIVERY_IN_PROGRESS, "Delivery in progress"),
    (DELIVERED, "Delivered"),
    (CANCELLED_BY_STORE, "Cancelled by store"),
)
