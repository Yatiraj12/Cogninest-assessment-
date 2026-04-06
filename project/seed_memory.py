from vanna_setup import create_vanna_agent
from vanna.core.user import User


def seed_memory():
    """
    Seed Vanna memory by sending training questions to the agent.
    """

    agent, memory = create_vanna_agent()

    # Create default user (IMPORTANT: id, not user_id)
    user = User(id="default_user")

    training_questions = [
        "How many patients do we have?",
        "List all doctors and their specializations",
        "Show all appointments",
        "Show revenue by doctor",
        "Which city has the most patients?",
        "Show unpaid invoices",
        "Top 5 patients by spending",
        "Appointments by status",
        "Average treatment cost",
        "Monthly appointment count",
        "List patients from Mumbai",
        "Show overdue invoices",
        "Doctor appointment count",
        "Revenue by month",
        "Patients registered by month"
    ]

    print("Seeding memory with training questions...\n")

    for question in training_questions:
        try:
            print(f"Training on: {question}")
            response = agent.send_message(user, question)
            print("Response:", response)
            print("-" * 50)
        except Exception as e:
            print(f"Error training on question '{question}': {e}")

    print("\nMemory seeding complete.")


if __name__ == "__main__":
    seed_memory()