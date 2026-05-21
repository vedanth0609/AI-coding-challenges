# Local AI Text Analyzer

A simple, self-contained Python project that simulates AI behavior using only local logic—no external APIs, no network requests, no dependencies beyond the Python standard library.

## Overview

This project demonstrates basic natural language processing concepts through a sentiment analysis tool that classifies text as positive, negative, or neutral using keyword matching, pattern recognition, and weighted scoring.

## Features

- **Sentiment Analysis**: Classifies text into five categories: Very Positive, Positive, Neutral, Negative, Very Negative
- **Keyword Weighting**: Uses weighted dictionaries for nuanced sentiment detection
- **Pattern Recognition**: Detects emphasis through punctuation and intensifier words
- **Interactive Mode**: Real-time text analysis via terminal input
- **Demo Mode**: Pre-built examples showcasing the analyzer's capabilities

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional installation needed—uses standard library only

## Usage

### Interactive Mode (Default)
Run the analyzer and enter text to analyze in real-time:

```bash
python main.py
```

Type your text when prompted, and the analyzer will display:
- Original text
- Word count
- Sentiment classification
- Sentiment score
- Breakdown of positive/negative scores

Type `quit`, `exit`, or `q` to exit.

### Demo Mode
Run with predefined examples to see the analyzer in action:

```bash
python main.py --demo
```

### Help
View usage information:

```bash
python main.py --help
```

## How It Works

The Local AI Analyzer uses a rule-based approach to simulate AI behavior:

1. **Text Preprocessing**: Converts text to lowercase and normalizes whitespace
2. **Keyword Matching**: Scans text for positive and negative keywords from weighted dictionaries
3. **Pattern Detection**: Identifies emphasis patterns (multiple exclamation marks, intensifiers like "very" or "really")
4. **Score Calculation**: Computes a sentiment score by summing positive and negative keyword weights
5. **Classification**: Maps the final score to a sentiment category:
   - Score > 3: Very Positive
   - Score > 0: Positive
   - Score = 0: Neutral
   - Score > -3: Negative
   - Score ≤ -3: Very Negative

### Example

Input: `"I absolutely love this product! It's amazing and wonderful!"`

Analysis:
- Positive keywords detected: "love" (3), "amazing" (4), "wonderful" (3)
- Emphasis pattern detected: "!!!" adds bonus points
- Total score: +8
- Classification: Very Positive

## Project Structure

```
.
├── .gitignore          # Git ignore patterns
├── main.py             # Main application code
├── requirements.txt    # Dependencies (empty - uses stdlib)
└── README.md           # This file
```

## Code Highlights

- **LocalAIAnalyzer Class**: Core analysis engine with modular methods
- **Type Hints**: Full type annotations for better code clarity
- **Error Handling**: Graceful handling of user input and edge cases
- **Clean Architecture**: Separated concerns (preprocessing, scoring, classification, display)

## Limitations

This is a simplified demonstration of AI concepts using rule-based logic. It does not:
- Understand context or sarcasm
- Handle complex sentence structures
- Learn or adapt from new data
- Compare to modern machine learning models

For production sentiment analysis, consider libraries like NLTK, spaCy, or transformer-based models.

## License

This project is open source and available for educational purposes.

## Author

Created as a beginner-friendly introduction to AI concepts using pure Python.
