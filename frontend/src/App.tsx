import { useState } from 'react';
import './App.css';
import axios from 'axios';

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

	// const fetchAnswer = async (message : string) => {
	// 	const res = await axios.post("http://127.0.0.1:5000/answer", { message } )

	// 	// const { answer } = res.data;

	// 	// const answer = res.data
	// }

	const handleClick = () => {
		
		if(text.length == 0) return;
		
		const m : Message = { author : "you", message : text }
		addMessage(m)

		setText('')
	}
	
	const handleKeyDown = (e : React.KeyboardEvent<HTMLInputElement>) => {
		if(e.key == 'Enter')
			handleClick()
	}

	return (
		<>
			<h1>ChatBot</h1>
			<div className='box'>
				<div className='history'>
					{history.map((m, i) => (
						<p className={'message ' + m.author} key={i}>{m.message}</p>
					))}
				</div>
				<div className='sender'>
					<input
						placeholder='Olá senhor bot'
						value={text}
						onChange={(e) => setText(e.target.value)}
						onKeyDown={handleKeyDown}
					></input>
					<button onClick={handleClick} >Send</button>
				</div>
			</div>
		</>
	);
}

export default App;
('');
