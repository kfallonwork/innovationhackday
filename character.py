class Character:
	def __init__(self, name, description, temperature = 0.5, starting_feeling = "neutral":
		self.name = name
		self.description = description
		self.temperature = temperature
		self.ns = ns
		self.current_feeling = f"{self.name} is {starting_feeling}"
		self.last_thought = ""
		self.topic = ""
	
	def getPrompt(self, prior_conversation):
		return [{"role": "user", 
		"content": 
f"""Context: You are a character called {self.name}. 
{self.description} 
You are discussing: {self.topic}
Current feeling: {self.current_feeling}
Last thought: {self.last_thought}
Keep your answers concise and conversational.
Reply to the conversation in character.
{prior_conversation}
---
Output the response to the prompt above as json. The output should be a tuple where the tuple is in the form of {{"name" : <Name>, "utterance" : <Utterance>, "feeling" : <Feeling>, "thoughts" : <Thoughts>}}. If the conversation has come to a natural conclusion then the <Feeling> should end with "The conversation has ended."
Example output json:
{{"name" : "Alex", "utterance" : "Hello. I've been working down the mines today.", "feeling" : Bored", "thoughts" : "Working in the mines is awful. I must find a better job"}}"""}]
