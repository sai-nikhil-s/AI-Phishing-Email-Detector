import csv
import random

legitimate_templates = [
    "Hi {name}, please find the {document} attached for your review.",
    "Your {service} order has been shipped and is expected to arrive tomorrow.",
    "Reminder: your {event} is scheduled for {time}.",
    "Hi {name}, can we reschedule our meeting to {time}?",
    "Your monthly {service} statement is now available in your account.",
    "Thank you for registering for the {event}. We look forward to seeing you.",
    "Your password was changed successfully. If you made this change, no action is required.",
    "Please review the attached {document} before the meeting.",
    "Your application for {service} has been received successfully.",
    "The project report is ready for review. Please share your feedback."
]

phishing_templates = [
    "URGENT! Your {service} account will be suspended today. Click here immediately to verify your account.",
    "Your account has been compromised. Verify your password immediately using the link below.",
    "FINAL WARNING! Your account will be deleted within 24 hours unless you confirm your identity.",
    "Congratulations! You have won a {amount} prize. Send your bank details to claim your reward.",
    "Security alert! Suspicious activity was detected. Login immediately to prevent account suspension.",
    "Your payment has failed. Click the link below and enter your card details to complete the payment.",
    "Your refund is waiting. Provide your bank account information to receive the money.",
    "Urgent action required! Your email account will be permanently disabled unless you verify it now.",
    "You have been selected for an exclusive reward. Confirm your personal information to claim it.",
    "Your banking access is temporarily locked. Enter your username and password to restore access."
]

names = [
    "Rahul", "John", "Sarah", "Amit", "David",
    "Priya", "Arjun", "Michael", "Neha", "Daniel"
]

documents = [
    "meeting agenda", "project report", "assignment",
    "invoice", "presentation", "application form"
]

services = [
    "bank", "shopping", "email", "cloud",
    "subscription", "online banking"
]

events = [
    "webinar", "team meeting", "project review",
    "training session", "college seminar"
]

times = [
    "10 AM", "11 AM", "2 PM", "3 PM", "tomorrow morning"
]

amounts = [
    "$500", "$1,000", "$5,000", "₹50,000", "₹1,00,000"
]


def create_legitimate_email():
    template = random.choice(legitimate_templates)

    return template.format(
        name=random.choice(names),
        document=random.choice(documents),
        service=random.choice(services),
        event=random.choice(events),
        time=random.choice(times)
    )


def create_phishing_email():
    template = random.choice(phishing_templates)

    return template.format(
        service=random.choice(services),
        amount=random.choice(amounts)
    )


# Generate dataset
emails = []

for _ in range(100):
    emails.append([create_legitimate_email(), 0])

for _ in range(100):
    emails.append([create_phishing_email(), 1])


# Shuffle the dataset
random.shuffle(emails)


# Save dataset
with open("dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["text", "label"])

    writer.writerows(emails)


print("Dataset created successfully!")
print("Total emails:", len(emails))
print("Legitimate emails: 100")
print("Phishing emails: 100")
print("Saved as dataset.csv")
