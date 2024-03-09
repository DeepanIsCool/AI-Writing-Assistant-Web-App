from flask import Flask, render_template, request
import openai
from pyngrok import ngrok

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = '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'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_text', methods=['POST'])
def generate_text():
    # Retrieve user input from the form
    user_input = request.form['user_input']

    try:
        # Call the new method from the latest OpenAI API
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=200
        )

        # Extract the generated text from the API response
        generated_text = response.choices[0].text.strip()

        # Pass the generated text to the template for display
        return render_template('result.html', generated_text=generated_text)
    except Exception as e:
        # Handle any exceptions, such as API errors
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
    ngrok_tunnel = ngrok.connect('Hello')
    print(' * Running on', ngrok_tunnel.public_url)
    app.run()
