import { useState } from 'react';
import './App.css';

type Message = {
	author: 'you' | 'bot';
	message: string;
};

function App() {
	const [text, setText] = useState<string>('');

	const [history, setHistory] = useState<Message[]>([]);

	const addMessage = (m: Message) => {
		setHistory([...history, m]);
	};

	const handleClick = () => {
		let m : Message = { author : "bot", message : text }
		addMessage(m)
	}

	return (
		<>
			<h1>ChatBot</h1>
			<div className='box'>
				<div className='history'>
					{history.map((m) => (
						<p className={'message ' + m.author}>{m.message}</p>
					))}
				</div>
				<div className='sender'>
					<input
						placeholder='Olá senhor bot'
						value={text}
						onChange={(e) => setText(e.target.value)}
					></input>
					<button onClick={handleClick} >Send</button>
				</div>
			</div>
		</>
	);
}

export default App;
('');
