class TypingTest {
    constructor() {
        this.originalText = '';
        this.userInput = '';
        this.startTime = null;
        this.endTime = null;
        this.timer = null;
        this.currentIndex = 0;
        this.isTestActive = false;
        this.isTestComplete = false;
        
        this.initializeElements();
        this.bindEvents();
        this.loadNewParagraph();
    }
    
    initializeElements() {
        this.textDisplay = document.getElementById('text-display');
        this.startBtn = document.getElementById('start-btn');
        this.resetBtn = document.getElementById('reset-btn');
        this.timerDisplay = document.getElementById('timer');
        this.wpmDisplay = document.getElementById('wpm');
        this.accuracyDisplay = document.getElementById('accuracy');
        this.typedCharsDisplay = document.getElementById('typed-chars');
        this.resultsModal = new bootstrap.Modal(document.getElementById('resultsModal'));
    }
    
    bindEvents() {
        this.startBtn.addEventListener('click', () => this.startTest());
        this.resetBtn.addEventListener('click', () => this.resetTest());
        this.textDisplay.addEventListener('click', () => this.focusTextDisplay());
        this.textDisplay.addEventListener('keydown', (e) => this.handleKeyDown(e));
        this.textDisplay.addEventListener('focus', () => this.handleFocus());
        this.textDisplay.addEventListener('blur', () => this.handleBlur());
        
        // Prevent default text selection and editing
        this.textDisplay.addEventListener('selectstart', (e) => e.preventDefault());
        this.textDisplay.addEventListener('mousedown', (e) => e.preventDefault());
    }
    
    async loadNewParagraph() {
        try {
            this.textDisplay.innerHTML = `
                <div class="loading text-center py-5">
                    <i class="fas fa-spinner fa-spin fa-2x text-primary"></i>
                    <p class="mt-3 text-muted">Loading paragraph...</p>
                </div>
            `;
            
            const response = await fetch('/api/paragraph');
            const data = await response.json();
            this.originalText = data.text;
            this.displayText();
            this.resetStats();
        } catch (error) {
            console.error('Error loading paragraph:', error);
            this.textDisplay.innerHTML = `
                <div class="text-center py-5">
                    <i class="fas fa-exclamation-triangle fa-2x text-warning"></i>
                    <p class="mt-3 text-muted">Error loading paragraph. Please try again.</p>
                </div>
            `;
        }
    }
    
    displayText() {
        const chars = this.originalText.split('').map((char, index) => {
            return `<span class="char" data-index="${index}">${char === ' ' ? '&nbsp;' : char}</span>`;
        }).join('');
        
        this.textDisplay.innerHTML = chars;
        this.updateCurrentChar();
    }
    
    startTest() {
        if (this.isTestActive) return;
        
        this.isTestActive = true;
        this.isTestComplete = false;
        this.startTime = new Date();
        this.textDisplay.focus();
        this.startBtn.disabled = true;
        this.startBtn.innerHTML = '<i class="fas fa-keyboard me-2"></i>Test in Progress...';
        
        this.startTimer();
    }
    
    focusTextDisplay() {
        if (!this.isTestActive && this.originalText && !this.isTestComplete) {
            this.startTest();
        }
        this.textDisplay.focus();
    }
    
    handleBlur() {
        // Keep focus on text display during active test
        if (this.isTestActive && !this.isTestComplete) {
            setTimeout(() => {
                this.textDisplay.focus();
            }, 10);
        }
    }
    
    startTimer() {
        this.timer = setInterval(() => {
            if (!this.isTestActive) return;
            
            const elapsed = Math.floor((new Date() - this.startTime) / 1000);
            this.timerDisplay.textContent = elapsed;
            this.updateWPM();
        }, 100);
    }
    
    handleInput(inputChar) {
        if (!this.isTestActive) return;
        
        // Handle backspace
        if (inputChar === 'Backspace') {
            if (this.userInput.length > 0) {
                this.userInput = this.userInput.slice(0, -1);
                this.currentIndex = this.userInput.length;
            }
        } else if (inputChar.length === 1) {
            // Handle regular character input
            this.userInput += inputChar;
            this.currentIndex = this.userInput.length;
        }
        
        this.updateDisplay();
        this.updateStats();
        
        if (this.userInput.length >= this.originalText.length) {
            this.completeTest();
        }
    }
    
    handleKeyDown(e) {
        if (!this.isTestActive) return;
        
        // Prevent default behavior for most keys
        e.preventDefault();
        
        // Handle special keys
        if (e.key === 'Tab' || e.key === 'Enter') {
            return;
        }
        
        // Handle input
        this.handleInput(e.key);
    }
    
    handleFocus() {
        if (!this.isTestActive && this.originalText && !this.isTestComplete) {
            this.startTest();
        }
    }
    
    updateDisplay() {
        const chars = this.textDisplay.querySelectorAll('.char');
        
        chars.forEach((char, index) => {
            char.className = 'char';
            
            if (index < this.userInput.length) {
                const userChar = this.userInput[index];
                const originalChar = this.originalText[index];
                
                if (userChar === originalChar) {
                    char.classList.add('correct');
                } else {
                    char.classList.add('incorrect');
                }
            } else if (index === this.currentIndex) {
                char.classList.add('current');
            }
        });
    }
    
    updateCurrentChar() {
        const chars = this.textDisplay.querySelectorAll('.char');
        chars.forEach((char, index) => {
            if (index === this.currentIndex) {
                char.classList.add('current');
            } else {
                char.classList.remove('current');
            }
        });
    }
    
    updateStats() {
        const typedLength = this.userInput.length;
        this.typedCharsDisplay.textContent = typedLength;
        
        // Update accuracy
        let correctChars = 0;
        for (let i = 0; i < typedLength; i++) {
            if (i < this.originalText.length && this.userInput[i] === this.originalText[i]) {
                correctChars++;
            }
        }
        
        const accuracy = typedLength > 0 ? Math.round((correctChars / typedLength) * 100) : 100;
        this.accuracyDisplay.textContent = accuracy + '%';
        
        this.updateWPM();
    }
    
    updateWPM() {
        if (!this.startTime) return;
        
        const elapsed = (new Date() - this.startTime) / 1000 / 60; // minutes
        if (elapsed <= 0) return;
        
        const wordsTyped = this.userInput.trim().split(' ').length;
        const wpm = Math.round(wordsTyped / elapsed);
        this.wpmDisplay.textContent = wpm;
    }
    
    completeTest() {
        this.isTestActive = false;
        this.isTestComplete = true;
        this.endTime = new Date();
        
        clearInterval(this.timer);
        this.textDisplay.blur();
        this.startBtn.disabled = false;
        this.startBtn.innerHTML = '<i class="fas fa-play me-2"></i>Start Test';
        
        this.showResults();
    }
    
    showResults() {
        const totalTime = (this.endTime - this.startTime) / 1000;
        const wordsTyped = this.userInput.trim().split(' ').length;
        const wpm = Math.round(wordsTyped / (totalTime / 60));
        
        let correctChars = 0;
        const typedLength = Math.min(this.userInput.length, this.originalText.length);
        
        for (let i = 0; i < typedLength; i++) {
            if (this.userInput[i] === this.originalText[i]) {
                correctChars++;
            }
        }
        
        const accuracy = typedLength > 0 ? Math.round((correctChars / typedLength) * 100) : 100;
        
        // Update modal content
        document.getElementById('final-wpm').textContent = wpm;
        document.getElementById('final-accuracy').textContent = accuracy + '%';
        document.getElementById('final-time').textContent = Math.round(totalTime);
        document.getElementById('final-chars').textContent = this.userInput.length;
        
        // Show modal
        this.resultsModal.show();
    }
    
    resetTest() {
        this.isTestActive = false;
        this.isTestComplete = false;
        this.userInput = '';
        this.currentIndex = 0;
        this.startTime = null;
        this.endTime = null;
        
        clearInterval(this.timer);
        
        this.textDisplay.blur();
        this.startBtn.disabled = false;
        this.startBtn.innerHTML = '<i class="fas fa-play me-2"></i>Start Test';
        
        this.resetStats();
        this.loadNewParagraph();
    }
    
    resetStats() {
        this.timerDisplay.textContent = '0';
        this.wpmDisplay.textContent = '0';
        this.accuracyDisplay.textContent = '100%';
        this.typedCharsDisplay.textContent = '0';
    }
}

// Initialize the typing test when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.typingTest = new TypingTest();
});

// Global function for modal button
function resetTest() {
    if (window.typingTest) {
        window.typingTest.resetTest();
    }
}
