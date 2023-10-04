import random
import openai
import character

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
		
	def converse(self):
		character = random.choice([c for c in self.characters if c != character]) #choose a new character
		
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
		
		self.prior_messages += f"{output['name']} : {output['utterance']}" + "\n" #don't includes thoughts into the conversation history"
		#conversation_output = f"{output['name']} : {output['utterance']} ({output['thoughts']})\n"
		return output
		
	def addSceneDirection(self, direction):
		self.prior_messages += f"{direction}" + "\n"