
import random
import openai
import character

class Conversation:
	def __init__(self, topic):
		self.characters = []
		self.character_map = {}
		self.prior_messages = ""
		self.topic = topic
		#self.model = "gpt-3.5-turbo"
		self.model = "gpt-4"
		self.previous_character = None
		
	def addParticipant(self, character):
		character.topic = self.topic
		self.characters.append(character)
		self.character_map[character.name] = character
		self.prior_messages += f"{character.name} enters the scene: *{character.starting_action}" + "\n"
		
	def isCharacter(self, name):
		return name in self.character_map
		
	def converse(self, who = None):
		if who in self.character_map:
			character = self.character_map[who]
		else:
			character = random.choice([c for c in self.characters if c != self.previous_character]) #choose a new character
			
		self.previous_character = character
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
		
		self.prior_messages += f"{output['name']} : {output['utterance']} *{output['action']}*" + "\n" #don't includes thoughts into the conversation history"
		#conversation_output = f"{output['name']} : {output['utterance']} ({output['thoughts']})\n"

		return output
		
	def addSceneDirection(self, direction):
		self.prior_messages += f"{direction}" + "\n"