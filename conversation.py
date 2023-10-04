class Conversation:
	def __init__(self, topic):
		self.characters = []
		self.prior_messages = ""
		self.topic = topic
		#self.model = "gpt-3.5-turbo"
		self.model = "gpt-4"
		
	def addParticipant(self, character):
		character.topic = self.topic
		self.characters.append(character)
		random.shuffle(self.characters)
		
	def converse(self, steps = 10):
		character = self.characters[0]
		
		print(f"Starting prompt: {self.topic}\n")
		
		for _ in range(steps):
			message_content = character.getPrompt(self.prior_messages)
			
			chat_completion = openai.ChatCompletion.create(
				model=self.model, 
				messages=message_content, 
				temperature=character.temperature, 
				presence_penalty=character.ns
			)
				
			output = eval(chat_completion['choices'][0]['message']['content'])
			
			character.last_thought = output["thoughts"]
			character.current_feeling = output["feeling"]
			
			self.prior_messages += f"{output['name']} : {output['utterance']}" #don't includes thoughts into the conversation history"
			conversation_output = f"{output['name']} : {output['utterance']} ({output['thoughts']})\n"
			print(conversation_output)
			
			character = random.choice([c for c in self.characters if c != character]) #choose a new character
			if output["thoughts"] == "The conversation has ended.":
				break
