#!/usr/bin/env python3
"""
Local AI Text Analyzer
A simple, self-contained AI simulator that uses local Python logic
to analyze and classify text sentiment without any external APIs.
"""

import re
import sys
from typing import Dict, List, Tuple


class LocalAIAnalyzer:
    """
    A local AI analyzer that uses keyword matching and pattern recognition
    to simulate AI behavior for sentiment analysis.
    """
    
    def __init__(self):
        # Define sentiment keyword dictionaries with weights
        self.positive_keywords = {
            'good': 2, 'great': 3, 'excellent': 3, 'amazing': 4, 'wonderful': 3,
            'happy': 2, 'love': 3, 'fantastic': 3, 'awesome': 3, 'brilliant': 3,
            'best': 2, 'beautiful': 2, 'perfect': 3, 'enjoy': 2, 'nice': 1,
            'pleased': 2, 'delighted': 3, 'excited': 2, 'success': 2, 'win': 2
        }
        
        self.negative_keywords = {
            'bad': 2, 'terrible': 3, 'awful': 3, 'horrible': 3, 'worst': 3,
            'hate': 3, 'dislike': 2, 'sad': 2, 'angry': 2, 'upset': 2,
            'disappointed': 2, 'frustrated': 2, 'fail': 2, 'failure': 3,
            'poor': 2, 'wrong': 1, 'error': 2, 'problem': 1, 'issue': 1
        }
        
        # Pattern-based detection for emphasis
        self.emphasis_patterns = [
            r'!{2,}',  # Multiple exclamation marks
            r'\b(very|really|extremely|absolutely)\s+\w+',  # Intensifiers
        ]
    
    def preprocess_text(self, text: str) -> str:
        """
        Clean and normalize the input text.
        
        Args:
            text: Raw input string
            
        Returns:
            Cleaned lowercase string
        """
        # Convert to lowercase
        text = text.lower()
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def calculate_sentiment_score(self, text: str) -> Tuple[int, Dict[str, int]]:
        """
        Calculate sentiment score based on keyword matching.
        
        Args:
            text: Preprocessed text string
            
        Returns:
            Tuple of (total_score, breakdown_dict)
        """
        words = text.split()
        positive_score = 0
        negative_score = 0
        
        # Count positive keywords
        for word in words:
            if word in self.positive_keywords:
                positive_score += self.positive_keywords[word]
        
        # Count negative keywords
        for word in words:
            if word in self.negative_keywords:
                negative_score += self.negative_keywords[word]
        
        # Check for emphasis patterns
        for pattern in self.emphasis_patterns:
            matches = re.findall(pattern, text)
            if matches:
                # Boost the dominant sentiment if emphasis is detected
                if positive_score > negative_score:
                    positive_score += len(matches)
                elif negative_score > positive_score:
                    negative_score += len(matches)
        
        total_score = positive_score - negative_score
        
        breakdown = {
            'positive_score': positive_score,
            'negative_score': negative_score,
            'total_score': total_score
        }
        
        return total_score, breakdown
    
    def classify_sentiment(self, score: int) -> str:
        """
        Classify sentiment based on the calculated score.
        
        Args:
            score: Total sentiment score
            
        Returns:
            Sentiment classification string
        """
        if score > 3:
            return "Very Positive"
        elif score > 0:
            return "Positive"
        elif score == 0:
            return "Neutral"
        elif score > -3:
            return "Negative"
        else:
            return "Very Negative"
    
    def analyze(self, text: str) -> Dict:
        """
        Main analysis function that orchestrates the entire pipeline.
        
        Args:
            text: Raw input text to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        # Step 1: Preprocess
        cleaned_text = self.preprocess_text(text)
        
        # Step 2: Calculate sentiment
        score, breakdown = self.calculate_sentiment_score(cleaned_text)
        
        # Step 3: Classify
        sentiment = self.classify_sentiment(score)
        
        # Step 4: Compile results
        results = {
            'original_text': text,
            'cleaned_text': cleaned_text,
            'sentiment': sentiment,
            'score': score,
            'breakdown': breakdown,
            'word_count': len(cleaned_text.split())
        }
        
        return results
    
    def display_results(self, results: Dict):
        """
        Display analysis results in a formatted way.
        
        Args:
            results: Analysis results dictionary
        """
        print("\n" + "="*60)
        print("LOCAL AI TEXT ANALYZER - RESULTS")
        print("="*60)
        print(f"\nOriginal Text: {results['original_text']}")
        print(f"Word Count: {results['word_count']}")
        print(f"\nSentiment: {results['sentiment']}")
        print(f"Score: {results['score']:+d}")
        print(f"\nBreakdown:")
        print(f"  - Positive Score: {results['breakdown']['positive_score']}")
        print(f"  - Negative Score: {results['breakdown']['negative_score']}")
        print("="*60 + "\n")


def interactive_mode():
    """
    Run the analyzer in interactive mode, accepting user input.
    """
    analyzer = LocalAIAnalyzer()
    
    print("\n" + "="*60)
    print("LOCAL AI TEXT ANALYZER")
    print("="*60)
    print("\nEnter text to analyze (or 'quit' to exit):")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\n> ")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Local AI Analyzer. Goodbye!\n")
                break
            
            if not user_input.strip():
                print("Please enter some text to analyze.")
                continue
            
            # Analyze the input
            results = analyzer.analyze(user_input)
            analyzer.display_results(results)
            
        except KeyboardInterrupt:
            print("\n\nInterrupted. Exiting...\n")
            break
        except Exception as e:
            print(f"\nError: {e}\n")


def demo_mode():
    """
    Run the analyzer in demo mode with predefined examples.
    """
    analyzer = LocalAIAnalyzer()
    
    demo_texts = [
        "I absolutely love this product! It's amazing and wonderful!",
        "This is terrible and awful. I hate it so much.",
        "The weather is okay today, nothing special.",
        "What a brilliant success! We did a fantastic job!",
        "I'm very disappointed with this failure. It's the worst."
    ]
    
    print("\n" + "="*60)
    print("LOCAL AI TEXT ANALYZER - DEMO MODE")
    print("="*60 + "\n")
    
    for i, text in enumerate(demo_texts, 1):
        print(f"Example {i}:")
        results = analyzer.analyze(text)
        analyzer.display_results(results)


def main():
    """
    Main entry point for the application.
    """
    # Check command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['--demo', '-d']:
            demo_mode()
        elif arg in ['--help', '-h']:
            print("\nLocal AI Text Analyzer")
            print("\nUsage:")
            print("  python main.py           - Interactive mode")
            print("  python main.py --demo    - Demo mode with examples")
            print("  python main.py --help    - Show this help message")
            print()
        else:
            print(f"\nUnknown argument: {arg}")
            print("Use --help for usage information.\n")
    else:
        # Default to interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
