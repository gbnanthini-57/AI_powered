def analyze_incident(incident):
    """
    TEMPORARY MOCK.
    Team Member 1 will replace the internals of this function with real AI logic.
    The function name and return structure must stay the same so nothing else breaks.
    """
    return {
        "root_cause": "Null reference: 'user' object is null when accessing 'user.email'",
        "affected_files": ["src/routes/checkout.js"],
        "explanation": "The checkout endpoint attempts to access the 'email' property on a 'user' object without first checking if 'user' exists, causing a TypeError when the user is not found.",
        "patch": "if (user) {\n  sendConfirmation(user.email);\n} else {\n  return res.status(400).json({ error: 'User not found' });\n}",
    }