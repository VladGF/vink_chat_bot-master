import React, { useState } from 'react';
import './Chatbot.tsx.css';

const Chatbot: React.FC = () => {
  const [input, setInput] = useState<string>('');
  const [messages, setMessages] = useState<Array<{ text: string; user: boolean }>>([]);

  const chat = (userInput: string): string => {
    return 'hello';
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>): void => {
    e.preventDefault();
    if (input.trim() === '') return;
    const userMessage = { text: input, user: true };
    setMessages(prevMessages => [...prevMessages, userMessage]);
    const aiMessage = { text: '...', user: false };
    setMessages(prevMessages => [...prevMessages, aiMessage]);
    const response = chat(input);
    if (response !== '') {
      const newAiMessage = { text: response, user: false };
      setMessages(prevMessages => [...prevMessages.slice(0, -1), newAiMessage]);
    }
    setInput('');
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.user ? 'user-message' : 'ai-message'}`}>
            {message.text}
          </div>
        ))}
      </div>
      <form className="chatbot-input-form" onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={e => {
            setInput(e.target.value);
          }}
          placeholder="Type your message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default Chatbot;
