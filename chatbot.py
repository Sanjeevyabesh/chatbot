import streamlit as st
import datetime

# Define topics, subtopics, and Q&A for Datasets
TOPICS = {
    "Machine Learning": {
        "Models": "Machine learning models include algorithms like linear regression, decision trees, and neural networks. They learn patterns from data to make predictions.",
        "Datasets": {
            "default": "Datasets are collections of data used to train and test machine learning models. Examples include the Iris dataset, MNIST, and CIFAR-10. Ask me more about datasets!",
            "what are some popular machine learning datasets?": "Popular machine learning datasets include the Iris dataset for classification, MNIST for handwritten digit recognition, CIFAR-10 for image classification, and the Boston Housing dataset for regression tasks.",
            "what is the iris dataset?": "The Iris dataset is a classic dataset for classification. It contains 150 samples of iris flowers with 4 features: sepal length, sepal width, petal length, and petal width. It has 3 classes: Setosa, Versicolor, and Virginica.",
            "what is the mnist dataset?": "The MNIST dataset contains 70,000 grayscale images of handwritten digits (0-9). Each image is 28x28 pixels, and it's widely used for training and testing image classification models.",
            "what is cifar-10?": "CIFAR-10 is a dataset for image classification with 60,000 32x32 color images across 10 classes, like cats, dogs, cars, and airplanes. It’s often used to test computer vision models.",
            "where can i find machine learning datasets?": "You can find machine learning datasets on platforms like Kaggle, UCI Machine Learning Repository, Google Dataset Search, and AWS Open Data. Many libraries like scikit-learn also provide built-in datasets.",
            "what is the boston housing dataset?": "The Boston Housing dataset is used for regression tasks. It has 506 samples with 13 features, like crime rate and average number of rooms, to predict house prices in Boston.",
            "how are datasets used in machine learning?": "Datasets are split into training, validation, and test sets. The training set teaches the model, the validation set tunes it, and the test set evaluates its performance on unseen data.",
            "what makes a good dataset for machine learning?": "A good dataset is large, diverse, and representative of the problem. It should have minimal missing values, be well-labeled, and include enough features to capture patterns"
        },
        "Training": "Training a model involves feeding it data and adjusting its parameters to minimize errors, often using techniques like gradient descent.",
        "Evaluation": "Evaluation measures a model's performance using metrics like accuracy, precision, recall, and F1-score on a test dataset.",
        "Deployment": "Deployment is the process of integrating a trained model into a production environment, like a web app or API, to make predictions on new data"
    },
    "Cricket": {
        "Datasets": {
            "default": "Cricket datasets contain match and player data for analysis, like ball-by-ball events or player stats. Ask me more about cricket datasets!",
            "what are some popular cricket datasets?": "Popular cricket datasets include Cricsheet for ball-by-ball data, IPL datasets on Kaggle, and Cricmetric for aggregated stats. They cover matches, player stats, and more.",
            "what is cricsheet?": "Cricsheet provides ball-by-ball data for various cricket formats, like Test matches, ODIs, T20Is, and leagues such as IPL and Big Bash. It’s a reliable source for detailed match data.",
            "what is the ipl dataset on kaggle?": "The IPL dataset on Kaggle includes data from Indian Premier League matches, with details like teams, winners, venues, toss decisions, and player stats from 2008 to 2020.",
            "where can i find cricket datasets?": "You can find cricket datasets on Cricsheet, Kaggle, ESPN Cricinfo, Cricbuzz, and Cricmetric. Some platforms like Cricmetric also offer downloadable CSV files.",
            "what is the ms dhoni odi dataset?": "The MS Dhoni ODI dataset, often sourced from ESPN Cricinfo, includes his One Day International career stats, like runs scored, matches played, and performance against different teams.",
            "what data is in cricmetric datasets?": "Cricmetric datasets provide aggregated stats like batting averages, strike rates, and win probabilities for players and teams, filterable by competition, club, or country.",
            "how are cricket datasets used?": "Cricket datasets are used for analytics, like predicting match outcomes, analyzing player performance, or calculating metrics such as strike rate and economy using machine learning.",
            "what makes a good cricket dataset?": "A good cricket dataset should be detailed, accurate, and up-to-date, with ball-by-ball data or player stats, minimal errors, and coverage of various formats and competitions"
        }
    },
    "Indian Politics": {
        "Datasets": {
            "default": "Indian Politics datasets include election results, politician profiles, and voter data. Ask me more about datasets in Indian Politics!",
            "what are some popular datasets for indian politics?": "Popular datasets include the Election Commission of India (ECI) election results, Lok Dhaba for Indian election data, and Kaggle’s Indian Election datasets.",
            "what is the eci election results dataset?": "The ECI election results dataset, from the Election Commission of India, contains data on national and state election outcomes, including votes, winners, and party performance.",
            "what is lok dhaba?": "Lok Dhaba, by the Trivedi Centre for Political Data, provides datasets on Indian elections since 1962, with details on candidates, constituencies, and voter turnout.",
            "where can i find indian politics datasets?": "You can find Indian Politics datasets on the Election Commission of India website, Lok Dhaba, Kaggle, and data.gov.in, which offers open government data.",
            "what is the indian election dataset on kaggle?": "The Indian Election dataset on Kaggle includes data on Lok Sabha elections, with features like candidate names, parties, votes, and constituency details.",
            "what data is in the eci party symbols dataset?": "The ECI party symbols dataset includes images of symbols for 49 national and state parties, with 931 labeled images of dimensions 180x180, often used for symbol recognition tasks.",
            "how are indian politics datasets used?": "These datasets are used to analyze election trends, predict outcomes, study voter behavior, and develop models for political analysis using machine learning.",
            "what makes a good dataset for indian politics?": "A good dataset should be comprehensive, with accurate election results, voter demographics, and party data, and should be regularly updated to reflect recent elections"
        }
    },
    "Cinema": {
        "Datasets": {
            "default": "Cinema datasets include movie ratings, box office data, and actor profiles. Ask me more about cinema datasets!",
            "what are some popular cinema datasets?": "Popular cinema datasets include the IMDb dataset, MovieLens dataset, Bollywood Movie dataset on Kaggle, and TMDB 5000 Movie Dataset.",
            "what is the imdb dataset?": "The IMDb dataset contains data on movies, including titles, genres, ratings, cast, and crew. It’s widely used for movie recommendation systems.",
            "what is the movielens dataset?": "The MovieLens dataset, created by GroupLens, includes user ratings for movies, with versions like 100K, 1M, and 20M ratings, used for collaborative filtering research.",
            "where can i find cinema datasets?": "You can find cinema datasets on Kaggle, IMDb’s public datasets, MovieLens website, and TMDB’s API for movie metadata.",
            "what is the bollywood movie dataset?": "The Bollywood Movie dataset on Kaggle includes data on Hindi films, with features like movie titles, genres, actors, directors, and box office collections.",
            "what is the tmdb 5000 movie dataset?": "The TMDB 5000 Movie Dataset contains metadata for 5,000 movies from The Movie Database, including budgets, revenues, genres, and user ratings.",
            "how are cinema datasets used?": "Cinema datasets are used for building recommendation systems, analyzing box office trends, predicting movie success, and studying audience preferences.",
            "what makes a good cinema dataset?": "A good cinema dataset should have detailed metadata, like genres, cast, and ratings, be up-to-date, and include diverse films across regions and languages"
        }
    },
    "General Questions": {
        "Datasets": {
            "default": "General datasets cover a wide range of topics, like demographics, economics, and surveys. Ask me more about general datasets!",
            "what are some popular general datasets?": "Popular general datasets include the World Bank Open Data, US Census Data, Google Public Data, and the General Social Survey (GSS).",
            "what is the world bank open data?": "World Bank Open Data provides global development data, like GDP, population, and education stats, for over 200 countries, used for economic analysis.",
            "what is the us census data?": "The US Census Data includes demographic and economic data, like population, income, and housing stats, collected every 10 years in the United States.",
            "where can i find general datasets?": "You can find general datasets on data.gov, World Bank Open Data, Google Public Data, Kaggle, and academic repositories like ICPSR.",
            "what is the general social survey?": "The General Social Survey (GSS) is a US-based survey dataset with data on social attitudes, behaviors, and demographics, collected since 1972.",
            "what is google public data?": "Google Public Data offers datasets on global topics, like unemployment rates and life expectancy, with interactive visualizations for exploration.",
            "how are general datasets used?": "General datasets are used for research, policy analysis, trend forecasting, and building models in fields like economics, sociology, and public health.",
            "what makes a good general dataset?": "A good general dataset should be reliable, well-documented, cover a broad scope, and be accessible in formats like CSV or JSON for analysis"
        }
    },
    "Frontend": {
        "HTML": "HTML is the standard markup language for creating web pages. It structures content using tags like <div>, <p>, and <h1>.",
        "CSS": "CSS is used to style web pages, controlling layout, colors, and fonts. It works with HTML to make websites visually appealing.",
        "JavaScript": "JavaScript adds interactivity to web pages, like handling events, making API calls, and updating the DOM dynamically"
    }
}

# Function to get suggested questions for a topic's Datasets subtopic
def get_suggested_questions(topic):
    if topic in TOPICS and "Datasets" in TOPICS[topic]:
        dataset_questions = list(TOPICS[topic]["Datasets"].keys())
        # Exclude the "default" key and take the first 3 questions
        dataset_questions = [q for q in dataset_questions if q != "default"][:3]
        return dataset_questions
    return []

# Function to check if the input is relevant to the topic or subtopic
def is_relevant_input(user_input, topic, subtopic):
    user_input = user_input.lower()
    relevant_keywords = ["dataset", "data", topic.lower(), subtopic.lower()]
    return any(keyword in user_input for keyword in relevant_keywords)

# Function to get a response based on user input with improved matching
def get_response(user_input, selected_topic):
    user_input = user_input.lower().strip()
    
    # Handle casual greetings or unrelated inputs
    casual_phrases = ["what nanbaa", "hi", "hello", "hey", "how are you"]
    for phrase in casual_phrases:
        if phrase in user_input:
            return "Hey nanbaa! 😄 I can help with questions about Machine Learning, Cricket, Indian Politics, Cinema, General Questions, or Frontend topics. Try asking about datasets!"

    # First, try the selected topic from the sidebar
    if selected_topic in TOPICS:
        for subtopic, content in TOPICS[selected_topic].items():
            if subtopic.lower() in user_input or subtopic == "Datasets":  # Default to Datasets if no subtopic is mentioned
                # Check if the input is relevant to the topic or subtopic
                if not is_relevant_input(user_input, selected_topic, subtopic):
                    return "Sorry!, I don't know about it."
                if isinstance(content, dict):
                    # Try exact match first
                    if user_input in content:
                        return content[user_input]
                    # Then try partial match
                    for question, answer in content.items():
                        if question != "default":
                            question_words = set(question.lower().split())
                            user_words = set(user_input.split())
                            common_words = question_words.intersection(user_words)
                            if len(common_words) >= len(question_words) * 0.7:
                                return answer
                    # Only return the default response if the input is relevant
                    if "default" in content:
                        return content["default"]
                return content

    # If no match in selected topic, check all topics
    for topic, subtopics in TOPICS.items():
        if topic.lower() in user_input:
            for subtopic, content in subtopics.items():
                if subtopic.lower() in user_input:
                    if not is_relevant_input(user_input, topic, subtopic):
                        return "Sorry!, I don't know about it."
                    if isinstance(content, dict):
                        if user_input in content:
                            return content[user_input]
                        for question, answer in content.items():
                            if question != "default":
                                question_words = set(question.lower().split())
                                user_words = set(user_input.split())
                                common_words = question_words.intersection(user_words)
                                if len(common_words) >= len(question_words) * 0.7:
                                    return answer
                        if "default" in content:
                            return content["default"]
                    return content
            return f"I know about {topic}, but can you be more specific? Try asking about Datasets."
    
    # If the input doesn't match any topic
    return "Sorry!, I don't know about it."

# Custom CSS for WhatsApp-like chat bubbles
st.markdown("""
    <style>
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 10px;
    }
    .bot-message {
        background-color: #f1f0f0;
        color: black;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        max-width: 70%;
        float: left;
        clear: both;
    }
    .user-message {
        background-color: #DCF8C6;
        color: black;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        max-width: 70%;
        float: right;
        clear: both;
    }
    .timestamp {
        font-size: 0.8em;
        color: gray;
        margin-top: 2px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Set page title
    st.title("Chatbot")

    # Sidebar with only main topics (no subtopics)
    st.sidebar.header("Topics")
    selected_topic = st.sidebar.radio("Select a topic", list(TOPICS.keys()))

    # Display suggested questions based on selected topic
    suggested_questions = get_suggested_questions(selected_topic)
    if suggested_questions:
        st.markdown(f"### Suggested Questions for {selected_topic}")
        for question in suggested_questions:
            st.write(f"- {question}")

    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "Bot", "message": "Ask me anything about Machine Learning, Cricket, Indian Politics, Cinema, General Questions, or Frontend topics!", "timestamp": datetime.datetime.now().strftime("%H:%M")}
        ]

    # Display chat history with WhatsApp-like styling
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "Bot":
            st.markdown(
                f'<div class="bot-message">{chat["message"]}<br><span class="timestamp">{chat["timestamp"]}</span></div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="user-message">{chat["message"]}<br><span class="timestamp">{chat["timestamp"]}</span></div>',
                unsafe_allow_html=True
            )
    st.markdown('</div>', unsafe_allow_html=True)

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat_history = [
            {"role": "Bot", "message": "Ask me anything about Machine Learning, Cricket, Indian Politics, Cinema, General Questions, or Frontend topics!", "timestamp": datetime.datetime.now().strftime("%H:%M")}
        ]
        st.rerun()

    # Chat input and send button aligned in a single row
    st.markdown("### Ask a Question")
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("Type a message...", key="user_input", label_visibility="collapsed")
    with col2:
        send_button = st.button("Send")

    # Process user input when the Send button is clicked
    if send_button and user_input:
        # Add user message to chat history with timestamp
        st.session_state.chat_history.append({
            "role": "You",
            "message": user_input,
            "timestamp": datetime.datetime.now().strftime("%H:%M")
        })
        
        # Get bot response using the selected topic
        bot_response = get_response(user_input, selected_topic)
        st.session_state.chat_history.append({
            "role": "Bot",
            "message": bot_response,
            "timestamp": datetime.datetime.now().strftime("%H:%M")
        })
        
        # Rerun to update the chat display
        st.rerun()

if __name__ == "__main__":
    main()