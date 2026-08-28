if (user) {
  sendConfirmation(user.email);
} else {
  return res.status(400).json({ error: 'User not found' });
}