
# Cover Letter Generator

Webapp for generating cover letters using LLM


![Banner](https://github.com/gerardmietek/cover_letter_llm/blob/main/webapp/static/images/banner.png)






## 🔧 How to run it?

To run this project locally, follow these steps:  
**1. Get your OpenAI API key**
     
- Sign up at OpenAI and generate you API key:  
       https://platform.openai.com/settings/organization/api-keys

- Create a file named api_key.txt in the root directory  
       of the project

- Paste your API key into that file (no quotes, no spaces)

**2. Make sure that Docker is installed on your machine**  

**3. Build and run the Docker container**
```
docker build -t app . 
docker run -dp 5000:5000 --name container app
```
**4. Go to localhost:5000/ and use the app**

## 📷 Screenshots

![App Screenshot 1](https://github.com/gerardmietek/cover_letter_llm/blob/main/webapp/static/images/screen1.png)

![App Screenshot 2](https://github.com/gerardmietek/cover_letter_llm/blob/main/webapp/static/images/screen2.png)


