# RASA

## Introduction to RASA

**RASA** is an open-source conversational AI platform that allows developers to build and deploy natural language processing (NLP) based chatbots and virtual assistants. RASA is designed to handle both the natural language understanding (NLU) and the dialogue management aspects of conversational systems. It provides a flexible and customizable framework for creating context-aware and interactive conversational experiences.

### Key Features

- **Open Source:** RASA is open-source and can be freely used, modified, and extended by developers.
- **Flexibility:** RASA provides a high level of flexibility, allowing developers to customize and fine-tune the behavior of their conversational AI applications.
- **Context Management:** RASA Core maintains context and dialogue history to generate more contextually relevant responses.
- **Training:** Both RASA NLU and RASA Core are trainable, allowing developers to improve their performance with domain-specific data.
- **Multi-Channel Support:** RASA supports interactions across various channels, such as messaging platforms, websites, and more.
- **Scalability:** RASA is designed to scale, making it suitable for both small projects and large-scale applications.


## RASA Architecture Overview 

RASA is an open-source conversational AI platform that consists of two main components: RASA NLU and RASA Core. These components work together to enable the development of powerful and context-aware conversational applications.

### 1. RASA NLU (Natural Language Understanding):

**Purpose:**
- RASA NLU is responsible for understanding and extracting structured information from user messages.
- It helps in turning user inputs into structured data that can be easily understood by machines.

**Key Features:**
- **Intent Recognition:** Identifying the intention behind a user's message (e.g., "Book a Flight," "Get Weather Information").
- **Entity Extraction:** Extracting important entities or pieces of information from the user's message (e.g., Dates, Locations, Product Names).
- **Intent Classification:** Determining the primary goal or action the user wants to perform based on their input.

**Training Data:**
RASA NLU is trained on labeled examples of user messages, where intents and entities are annotated. It uses this training data to learn patterns and improve its ability to recognize intents and entities accurately.

**Pipeline Configuration:**
RASA NLU uses a pipeline-based approach for processing and interpreting user messages. A pipeline consists of different components, such as tokenizers, featurizers, and machine learning models, arranged in a sequence. Example: A typical pipeline might include a tokenizer to break the text into words, a featurizer to convert words into numerical features, and a machine learning model for intent and entity recognition

### 2. RASA Core (Now RASA Open Source):

**Purpose:**
- RASA Core is responsible for handling the dialogue flow and making decisions on how the assistant should respond to user inputs.
- It manages the conversation by predicting the next action to take based on the current state of the dialogue.

**Key Features:**
- **Dialogue Management:** Dialogue management involves predicting the next action to take in the conversation based on the user's input and the current state of the dialogue. Example: If the user asks about the weather, the dialogue manager may decide to trigger the "Get Weather" action.
- **Policy Learning:** RASA Core uses machine learning models (policies) to learn how to select actions in different situations. These policies are learned from example dialogues provided during training Example: By learning from example dialogues, RASA Core can understand when to ask for clarification, provide information, or take other actions.
- **Training Data:** Similar to RASA NLU, RASA Core is trained on example dialogues that include user inputs, system responses, and the corresponding actions taken by the assistant.

**Stories:**
Stories are example dialogues that help train the RASA Core model. They consist of user inputs, system responses, and the corresponding actions taken by the assistant. Example: A story might describe a user asking about the weather, the assistant responding with the weather information, and the action of sending the information to the user.

**Action Server:**
The Action Server is responsible for executing the actions predicted by RASA Core. These actions could include sending a message to the user, querying a database, or performing any other custom operation. Example: If the predicted action is "Get Weather," the Action Server would handle the logic to fetch the current weather from a relevant source.


## RASA SDK
The RASA SDK (Software Development Kit) is a set of tools and libraries that helps developers create and customize chatbots using the RASA framework.

**Key Components and Features of the RASA SDK:**

1. **Actions and Custom Actions:**
   - In RASA, actions are tasks that a bot can perform, such as fetching data from an external API, querying a database, or generating a response. Custom actions are user-defined actions that can be implemented using the RASA SDK.
   - The RASA SDK provides a convenient way to create custom actions by subclassing the Action class and implementing the run method. These actions can be used to execute custom code and generate dynamic responses.

2. **Action Server:**
   - The Action Server is a separate process that runs custom actions in response to user inputs. It communicates with the RASA Core (now RASA Open Source) server to perform actions triggered by user messages.
   - Developers need to run the Action Server alongside the RASA Core Server to handle custom actions.
  
3. **Custom Components:**
   - RASA allows developers to create custom components for different stages of the NLU (Natural Language Understanding) and dialogue management pipelines. These components can be used to extend or modify the default behavior of the RASA framework.
   - Custom components can be written in Python and integrated into the RASA pipeline to enhance the capabilities of the chatbot.
  
4. **Endpoints Configuration:**
   - The endpoints.yml file in a RASA project is used to configure various endpoints, including the endpoint for the Action Server. This file specifies the URL where the Action Server can be reached.

5. **Interactive Learning:**
   - The RASA SDK supports interactive learning, allowing developers to improve the model by providing feedback during conversations. This can be done using the RASA Interactive Command, which uses a simple interactive mode to correct and retrain the model based on user feedback.


## RASA X

**RASA X** is a tool designed to complement the RASA Open Source framework, providing a user interface for developers, product managers, and non-technical users to collaborate on the development and improvement of conversational AI models. It simplifies tasks such as training models, managing conversations, and improving the performance of your chatbot.

**Key Components and Features of the RASA X:**

1. **User Interface:**
   - RASA X provides a web-based user interface that allows users to interact with their chatbot, review conversations, and annotate training data without needing to work directly with code.

2. **Conversation Review:**
   - Users can review and annotate conversations to improve the training data and the performance of the model. This is particularly useful for fine-tuning the chatbot's responses and handling edge cases.

3. **Model Training:**
   - RASA X facilitates model training directly from the user interface. Users can train and evaluate models without having to use the command line, making it more accessible for non-technical team members.

4. **Version Control:**
   - RASA X includes version control features, allowing users to track changes to their NLU data, stories, and other configuration files. This helps in managing the evolution of the conversational AI model over time.

5. **Collaboration:**
   - RASA X supports collaboration among team members by allowing multiple users to work on the same project simultaneously. This is especially useful for teams working on chatbot development and maintenance.

6. **Integration with RASA Open Source:**
   - RASA X is tightly integrated with RASA Open Source. You can use RASA X to experiment with and improve your models, and then seamlessly transition to RASA Open Source for more advanced customization and development.



## RASA Project Structure

When initializing a RASA project, the directory structure includes the following folders and files:
```
.
|
├── actions
│   ├── __init__.py
│   └── actions.py
|
├── data
│   ├── nlu.yml
│   └── stories.yml
|
├── models
│   └── <timestamp>.tar.gz
|
├── tests
|  └── test_stories.yml
|
├── config.yml
|
├── credentials.yml
|
├── domain.yml
|
└── endpoints.yml
```

- **actions:**: This folder typically houses custom action files. Actions in RASA are executable pieces of code that respond to user messages. For instance, an action might involve calling an external API or implementing specific custom logic.
  
    - **Subfiles of "actions"**
      
      - **action.py**: This file is used to define custom actions that your chatbot can take during a conversation. Actions are the responses or behaviors your bot exhibits in response to user inputs. The action.py file serves as the implementation of these custom actions.

- **data:** This folder typically houses training data for the chatbot, including examples of user messages, intents, entities, and corresponding responses. The training data is instrumental in training both the NLU and Core models.

    - **Subfiles of "data"**

      - **nlu.yml:** This file holds training examples for the Natural Language Understanding (NLU) module of the chatbot. It includes user message examples with corresponding intents and entities, with the NLU model responsible for understanding and extracting meaning from user input.

      - **rules.yml:** The rules.yml file defines conversation rules for the chatbot. These rules specify behaviors based on certain conditions, often tied to detected intents and entities in user messages. Rules play a crucial role in directing the flow of the conversation.

      - **stories.yml:** Containing conversational stories, this file represents potential interactions between users and the chatbot. Each story comprises a sequence of user messages, bot responses, and potential actions. These stories are employed in training the RASA Core Model, which dictates the dialogue flow of the chatbot.

- **models:** After training the chatbot, the resulting trained models are stored in this folder. These models include both the NLU model, responsible for understanding user input, and the Core model, determining the chatbot's response strategies.

- **tests:** This folder typically houses test cases for the chatbot. Thorough testing ensures that the chatbot functions as expected and adeptly handles diverse scenarios.
  
     - **Subfiles of "tests"**
       
       - **test_stories.yml:** This file typically contains test stories written in the Rasa conversation format. These stories are used for testing and evaluating the behavior of your chatbot or conversational agent. Each story represents a conversation between the user and the bot, along with the expected responses.

- **config.yml:** This file contains configuration settings for both Rasa NLU (Natural Language Understanding) and Rasa Core models. It specifies the pipeline for processing user messages and other pertinent settings related to model training.

- **credentials.yml:** This file serves as a secure repository for storing sensitive information like API keys, passwords, or other credentials essential for the chatbot. It emphasizes the importance of safeguarding such information and avoiding exposure in the codebase.

- **domain.yml:** This file outlines the domain of your chatbot, encompassing details about intents, entities, actions, and responses. Essentially, it defines what the chatbot comprehends and how it should respond to various user inputs.

- **endpoints.yml:** This file outlines the endpoints for the chatbot, such as the location of the Rasa Core server and any external services or APIs the chatbot may interact with. It aids in configuring connections between different components.


**NOTE**: Difference between **`rules.yml`** and **`stories.yml`** 

In Rasa, the rules.yml and stories.yml files are used to define the dialogue flow and behavior of the chatbot. While both files contribute to the conversation design, they serve slightly different purposes.

**rules.yml:**
  - **Purpose:** The rules.yml file is used to define explicit rules for the chatbot's behavior. Rules are more deterministic and can be seen as policy-based directives that guide the dialogue management without the need for a machine learning model.
  - **Format:** A rule in the rules.yml file consists of a condition and a set of actions. If the condition specified in the rule is met, the associated actions are executed by the chatbot.
  - **Use Cases:** Rules are useful for implementing specific behaviors, handling FAQs, or enforcing certain conversation paths based on simple conditions.

**stories.yml:**
  - **Purpose:** The stories.yml file is primarily used for training the dialogue management model. It contains example conversations or stories that demonstrate the expected flow of interactions between the user and the chatbot.
  - **Format:** A story in the stories.yml file typically consists of a sequence of user inputs and corresponding bot actions, forming a dialogue flow. Each story represents a possible conversation scenario.
  - **Training Data:** During training, Rasa's dialogue management model learns from these stories to predict the next action based on the user input.
Example stories.yml content:


## RASA Workflow: Overview

1. **User Input Processing**:
- **Rasa NLU**: Understands and extracts meaning from user inputs, identifying intents (user intentions) and entities (specific information) using machine learning models.

2. **Action Execution**:
- **Rasa Core**: Manages the conversation flow, making decisions on the chatbot's response based on user input and context. It utilizes a machine learning-based dialogue management system.

3. **Custom Action Scripts**:
- **Rasa Actions**: Developers create custom Python scripts that define the logic for specific actions the chatbot should take like querying databases, making API calls, or providing dynamic responses based on user input.

4. **Response Generation**:
- After executing the action, Rasa Core determines the bot's response based on the logic in the custom action scripts. The response is then sent back to the user, continuing the interactive conversation.



## RASA Workflow: Adding Intent and Training the Model

### Step 1: Adding Intent
**Define Intent in nlu.yaml**
- Specify the intent in the nlu.yaml file along with a balanced set of example data.
- Example:
```
- intent: nlu_fallback
  examples: |
    - what are you doing
    - tell me a joke
    - sing me a song
    - how tall are you
    - what's your favorite color

```
- Incorporate entity classification and, if necessary, regular expressions for improved entity extraction.
- Example(Without Regesx)
```
- intent: provide_name
  examples: |
    - I am [Abhishek](name)
    - My name is [Sujeet](name)
    - You can call me [Abhishek](name)
    - I go by the name [Rehman](name)
    - People call me [Amit](name)
```
- Example(With Regex)
```
- regex: account_number
  examples: |
    - \d{10,12}
- intent: account_information
  examples: |
    - my account number is [1234567891](account_number)
    - This is my account number [1234567891](account_number)
```

### Step 2: Configuring Domain
**Define Intent, Entity, and Responses in domain.yaml**
- Add the intent, entity, and corresponding responses in the domain.yaml file.
- Example:
```
intents:
  - nlu_fallback
  - welcome
  - provide_name

entities:
  - name

responses:
  utter_welcome:
    - text: "Hello and Welcome to the Expedien eSolution. May I know your name?"
  
  utter_greet:
    - text: "Hey {name}, nice meeting you! How can I help you today?"
```
- Optionally, map entities to slots and define actions for specific intents.
- Example:
```
actions:
  - action_greet

slots:
  name:
    type: text
    mappings:
      - type: from_entity
        entity: name
```

### Step 3: Creating Stories
**Map Intent and Response in story.yaml**
- Create stories in the story.yaml file to train the bot on how to respond to specific intents.
- Example:
```
- story: BASICS
  steps:
    - intent: welcome
    - action: utter_welcome
    - intent: provide_name
    - action: action_greet
```

### Step 4: Creating Rules
**Create Rule for a Specific Intent in rules.yaml**
- Establish rules in the rules.yaml file to guide the bot's behavior based on certain conditions.
- Example:
```
- rule: Ask the user to rephrase whenever they send a message with Low NLU Confidence
  steps:
  - intent: nlu_fallback
  - action: utter_please_rephrase
```

### Step 5: Writing Custom Actions
**Write Custom Action in actions.py**
- Develop a custom action in the actions.py file to handle specific intents.
- Example:
```
class ActionGreetUser(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot("name")
        dispatcher.utter_message(template="utter_greet", name=name)
        return []
```

## Working with "config.yaml" 
The config.yaml file is indeed a key component in configuring the behavior of the RASA natural language processing (NLP) models. RASA is an open-source framework for building conversational AI applications, including chatbots and virtual assistants. The configuration file allows users to define various settings and parameters for different components of the RASA framework, such as the NLU (Natural Language Understanding) and the Core components.

A typical config.yaml file
```
## General Information
recipe: default.v1
assistant_id: placeholder_default

## NLU Configuration
language: en
pipeline:

# Tokenization and Feature Extraction
  - name: WhitespaceTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: char_wb
    min_ngram: 1
    max_ngram: 4

# Intent Classification and Entity Recognition
  - name: DIETClassifier
    epochs: 100
    constrain_similarities: true

# Entity Synonyms and Response Selection
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100
    constrain_similarities: true

# Fallback Handling
  - name: FallbackClassifier
    threshold: 0.3
    ambiguity_threshold: 0.1

# Core Configuration
policies:
  - name: MemoizationPolicy
  - name: RulePolicy
  - name: UnexpecTEDIntentPolicy
    max_history: 5
    epochs: 100
  - name: TEDPolicy
    max_history: 5
    epochs: 100
    constrain_similarities: true
```



## Natural Languages Understanding
Natural Language Understanding (NLU) is a subset of Natural Language Processing  (NLP) in Artificial Intelligence that deals with machine reading comprehension. 

### Components of NLU Used in RASA Chat Bot Training

### 1. Language Models:
  - **Definition**: Language models are computational algorithms that predict the likelihood of a sequence of words in a language. They are designed to understand and generate human language based on statistical probabilities.
  - **Usages**:
      - Text Generation: Creating coherent and contextually relevant text passages.
      - Speech Recognition: Transcribing spoken language into text.
      - Machine Translation: Translating text from one language to another.
      - Predictive Typing: Suggesting next words in text editors or email clients.
  - **Functionalities**:
      - Understanding Context: Recognizing the context in which words are used.
      - Predicting Next Words: Estimating the most likely subsequent words in a sentence.
      - Generating Text: Creating full sentences and paragraphs that are syntactically and semantically correct.
  - **How it Works**: Language models use large amounts of text data to learn language patterns. Advanced models like GPT or BERT employ neural networks, specifically transformers, which excel in capturing context over long distances in text.

### 2. Tokenizers:
  - **Definition**: Tokenizers are tools that segment text into tokens, which can be individual words, characters, or subwords, facilitating further processing.
  - **Usages**:
      - Text Preprocessing: Preparing raw text for NLP tasks.
      - Input for Language Models: Feeding structured text into language models.
      - Search Engines: Enhancing search capabilities by breaking down queries.
  - **Functionalities**:
      - Breaking Text: Dividing texts into smaller, analyzable units.
      - Handling Various Languages: Accommodating different linguistic rules and character sets.
      - Normalization: Converting text to a standard format (like lowercasing).
  - **How it Works**: Tokenizers can use simple rule-based approaches or more complex algorithms. For example, some tokenizers handle morphologically rich languages by breaking down words into stems and affixes.

### 3. Featurizers:
  - **Definition**: Featurizers are mechanisms that convert text into numerical features, enabling machine learning models to process and analyze text data.
  - **Usages**:
      - Input for Machine Learning Models: Providing structured, numerical input for algorithms.
      - Text Classification: Assisting in categorizing text into different classes.
      - Information Retrieval: Enhancing the retrieval of relevant documents.
  - **Functionalities**:
      - Vectorization: Turning text into vectors of numbers.
      - Capturing Textual Characteristics: Identifying key features like word importance.
      - Dimensionality Reduction: Reducing the complexity of text data while preserving important information.
  - **How it Works**: Techniques like Bag of Words count word occurrences, while TF-IDF measures word importance. Embeddings, on the other hand, represent words in a high-dimensional space, capturing semantic relationships.

### 4. Intent Classifiers:
  - **Definition**: Intent classifiers are AI models that determine the purpose or intention behind a user's message in conversational systems.
  - **Usages**:
      - Chatbots: Understanding user requests to provide accurate responses.
      - Virtual Assistants: Helping assistants like Siri or Alexa comprehend user queries.
      - Customer Support: Automating responses to customer inquiries.
  - **Functionalities**:
      - Intent Recognition: Identifying the user's goal from their input.
      - Dialogue Management: Assisting in the logical flow of conversation.
      - Personalization: Tailoring responses based on identified intents.
  - **How it Works**: These classifiers are trained on examples of text with labeled intents. They use algorithms like decision trees, support vector machines, or neural networks to learn patterns associated with different intents.

### 5. Entity Extractors:
  - **Definition**: Entity extractors identify and extract specific pieces of information, known as entities, from text.
  - **Usages**:
      - Information Extraction: Pulling out names, dates, and other details from documents.
      - Data Analysis: Assisting in analyzing and organizing large volumes of text data.
      - Chatbots: Extracting relevant information from user inputs.
  - **Functionalities**:
      - Named Entity Recognition: Identifying entities like people, organizations, and locations.
      - Contextual Understanding: Interpreting the context in which entities appear.
      - Entity Disambiguation: Differentiating between entities with similar names.
  - **How it Works**: They might use linguistic rules to identify patterns or machine learning models trained on annotated text data to recognize and classify entities.

### 6. Selectors:
  - **Definition**: Selectors are decision-making components in chatbots that choose the most suitable response or action in a conversation.
  - **Usages**:
      - Dialogue Management: Controlling the flow of conversation in interactive systems.
      - Response Generation: Selecting appropriate responses in chatbots.
      - Action Determination: Deciding on actions in response to user inputs.
  - **Functionalities**:
      - Context Handling: Considering the context of the conversation for response selection.
      - Prioritizing Responses: Choosing the most relevant response from a set of possibilities.
      - Learning User Preferences: Adapting responses based on user interaction history.
  - **How it Works**: Simple selectors might use rule-based logic, while advanced systems employ machine learning to analyze conversation history and context to select responses.

**These components together create sophisticated systems capable of understanding and interacting with human language in a nuanced and effective way.**