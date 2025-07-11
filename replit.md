# Typing Speed Test Application

## Overview

This is a web-based typing speed test application built with Flask that allows users to practice their typing skills with randomly generated paragraphs. The application measures typing speed (WPM), accuracy, and provides real-time feedback during typing sessions.

## System Architecture

The application follows a simple client-server architecture:

- **Backend**: Flask web framework serving HTML templates and REST API endpoints
- **Frontend**: Vanilla JavaScript with Bootstrap for responsive UI
- **Deployment**: Configured for Replit with Gunicorn WSGI server
- **Data**: In-memory paragraph storage (no persistent database currently)

## Key Components

### Backend Components

1. **Flask Application** (`app.py`, `main.py`)
   - Main Flask application with basic configuration
   - Session management with secret key
   - Debug logging enabled for development

2. **Routes** (`routes.py`)
   - `/` - Main typing test page (renders HTML template)
   - `/api/paragraph` - REST API endpoint returning random paragraphs in JSON format

3. **Paragraph Service** (`routes.py`)
   - Integration with Bacon Ipsum API for dynamic paragraph generation
   - Generates random two-sentence paragraphs for each typing session
   - Robust fallback system with 10 predefined paragraphs if API fails
   - API endpoint: https://baconipsum.com/api/?type=all-meat&paras=1&sentences=2

### Frontend Components

1. **HTML Templates** (`templates/`)
   - `base.html` - Base template with Bootstrap, Font Awesome, and Google Fonts
   - `index.html` - Main typing test interface with stats display and typing area

2. **JavaScript** (`static/js/typing-test.js`)
   - `TypingTest` class handling all typing functionality
   - Real-time WPM, accuracy, and character counting
   - Timer management and test state control
   - API integration for fetching paragraphs

3. **CSS Styles** (`static/css/style.css`)
   - Modern gradient background design
   - Responsive stat cards with hover effects
   - Custom color variables and typography

## Data Flow

1. **Application Start**: User loads the main page (`/`)
2. **Paragraph Loading**: Frontend fetches random paragraph via `/api/paragraph`
3. **Test Initialization**: Text is displayed with character-by-character tracking
4. **Real-time Updates**: As user types, JavaScript updates WPM, accuracy, and timer
5. **Test Completion**: Results are calculated and displayed in modal

## External Dependencies

### Python Dependencies
- **Flask 3.1.1**: Web framework for routing and templating
- **Flask-SQLAlchemy 3.1.1**: ORM (installed but not currently used)
- **Gunicorn 23.0.0**: WSGI server for production deployment
- **psycopg2-binary 2.9.10**: PostgreSQL adapter (installed but not used)
- **email-validator 2.2.0**: Email validation utilities (not currently used)

### Frontend Dependencies (CDN)
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Font Awesome 6.4.0**: Icon library
- **Google Fonts**: Inter and JetBrains Mono fonts

## Deployment Strategy

- **Platform**: Replit with autoscale deployment target
- **Server**: Gunicorn WSGI server binding to `0.0.0.0:5000`
- **Environment**: Python 3.11 with Nix package management
- **Process Management**: Configured with reload capability for development

### Production Considerations
- Session secret should be set via environment variable
- Debug mode should be disabled in production
- Consider adding database for user progress tracking
- Implement user authentication for personalized features

## Recent Changes

- **June 25, 2025**: Integrated Bacon Ipsum API for dynamic paragraph generation
  - Replaced static paragraph list with live API calls for fresh content
  - Each typing session gets a unique random paragraph with consistent two-sentence format
  - Enhanced fallback system with 10 varied paragraphs for API reliability
  - Removed shiny text effects for cleaner appearance
  - Implemented fully dynamic text box sizing based on generated content length
  - Text box automatically adjusts from 80px to 250px based on paragraph size

- **June 25, 2025**: Enhanced End Test functionality and paragraph display
  - Added "End Test" button that appears during active typing
  - Implemented automatic score display after ending test manually
  - Auto-generates new paragraph after showing results (3-second delay)
  - Changed to single-line paragraphs (two sentences) for better display
  - Improved text box sizing to show entire paragraph clearly
  - Enhanced results modal with completion percentage tracking

- **June 25, 2025**: Dynamic text box sizing and two-line sentence format
  - Updated sentences to display in exactly two lines with line breaks
  - Made text box height dynamic based on content length
  - Improved text wrapping and responsive design
  - Enhanced readability with better font sizing
  - Text box now automatically adjusts between 100px and 200px height

- **June 25, 2025**: Complete UI overhaul with black and white shiny theme
  - Shortened paragraph length for better usability (single sentences)
  - Implemented black/white gradient theme with shiny effects
  - Improved text wrapping and container sizing
  - Enhanced button visibility and contrast
  - Added glowing text effects and shadows throughout interface
  - Fixed responsive design issues

- **June 25, 2025**: Modified typing interface to direct text interaction
  - Removed separate textarea input field
  - Users now type directly on the paragraph text
  - Text starts in dull gray color
  - Correct letters turn black when typed correctly
  - Incorrect letters glow red with animation effect
  - Improved user experience with direct text manipulation

## Changelog

- June 25, 2025. Initial setup
- June 25, 2025. Updated to direct text typing interface

## User Preferences

Preferred communication style: Simple, everyday language.