def detect_intent(text):
    text = text.lower()

    if "password" in text or "reset" in text:
        return "Password Reset"

    elif "order" in text and "track" in text:
        return "Order Tracking"

    elif "return" in text or "refund" in text:
        return "Return Policy"

    elif "cancel" in text:
        return "Order Cancellation"

    elif "delivery" in text or "late" in text:
        return "Delivery Issue"

    else:
        return "General Inquiry"
