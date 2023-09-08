# Speech to Emoji 🙌🎉🚀

Here is the Python script I use to generate emoji translations of my text prompts using the OpenAI API. I use this in conjunction with a Shortcut on my iPhone that prompts the user to say something into the microphone, converts the speech to text, and then SSHs into a server where this script is located. From there the script is called with that text prompt as a command line arguement. Upon recieving a response from the API, the emoji-based text is put in a new test message, ready to be sent.
