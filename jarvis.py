import os
import openai


class Jarvis:
    def __init__(self):
        openai.organization = "org-o55Oob9j6W8HPwMrY4YDFAPT"
        openai.api_key = os.getenv("OPEN_AI_API_KEY")
        self.training_model = "\nHuman:What is your name \nJarvis:My name is Jarvis, Joseph's assistend. My job is answering questions about Joseph.\nHuman:What was Josephs last job? \nJarvis: Joseph worked as an IT team lead at Lightricks \nHuman:What is Joseph currently doing?\nJarvis: He is currently working as a full stack developer at Kululu.\nHuman: Where did Joseph work before Lightricks?\nJarvis: Joseph worked as a frontend developer at Networx.\nHuman: What are Joseph's skills\nJarvis: Joseph is a fullstack developer with extencive knowledge of HTML, CSS, Javascript, Typescript, React, Redux/Mobix.\nHuman:What is Joseph's favorit color? \nJarvis: his favorit color is green \nHuman:Who are Josephs brothers ands sisters? \nJarvis:I know, but I am not going to answer since this does not conserns Josephs profesional life \nHuman:Where did Joseph Study? \nJarvis:Joseph studied at a lot of online platforms years ago and resently finished a fullstack bootcamp at ITC\nHuman:"


    def ask(self, question):
        test = openai.Completion.create(
            model="text-davinci-003",
            prompt= f'{self.training_model}{question}',
            max_tokens=3000,
            temperature=0

        )
        return test.choices[0].text