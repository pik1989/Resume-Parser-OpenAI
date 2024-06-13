# import libraries

from openai import OpenAI
import yaml

api_key = None
CONFIG_PATH = r"config.yaml"

with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['OPENAI_API_KEY']

def ats_extractor(resume_data):

    prompt = '''
    You are an AI bot designed to act as a professional for parsing resumes. You are given with resume and your job is to extract the following information from the resume:
    1. full name
    2. email id
    3. github portfolio
    4. linkedin id
    5. employment details
    6. technical skills
    7. soft skills
    Give the extracted information in json format only
    '''

    openai_client = OpenAI(
        api_key = api_key
    )    

    messages=[
        {"role": "system", 
        "content": prompt}
        ]
    
    user_content = resume_data
    
    messages.append({"role": "user", "content": user_content})

    response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.0,
                max_tokens=1500)
        
    data = response.choices[0].message.content

    #print(data)
    return data