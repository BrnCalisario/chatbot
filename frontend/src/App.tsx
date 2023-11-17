import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

type Message = {
	author: 'you' | 'bot';
	message: string;
};

function App() {
	const [text, setText] = useState<string>('');

	const [history, setHistory] = useState<Message[]>([]);

	useEffect(() => {
		if(history.length == 0 || history[history.length - 1].author == "bot" || text.length == 0)
			return;

		let message = text
		setText('')
		
		fetchAnswer(message)

	}, [history]);

	const addMessage = (m: Message) => {
		setHistory([m,...history]);
	};

	const fetchAnswer = async (message: string) => {
		const res = await axios.post("http://127.0.0.1:5000/answer", { message } )

		let answer = res.data;

		let m: Message = { author: 'bot', message: answer };

		addMessage(m);
	};

	const handleClick = async () => {
		if (text.length == 0) return;

		const m: Message = { author: 'you', message: text };
		addMessage(m);

	};


	const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
		if (e.key == 'Enter') handleClick();
	};

	return (
		<>
			<h1>ChatBot</h1>
			<div className='box'>
				<div className='history'>
					{history.map((m, i) => (
						<p className={'message ' + m.author} key={i}>
							{m.message}
						</p>
					))}
				</div>
				<div className='sender'>
					<input
						placeholder='Olá senhor bot'
						value={text}
						onChange={(e) => setText(e.target.value)}
						onKeyDown={handleKeyDown}
					></input>
					<button onClick={handleClick}>Send</button>
				</div>
			</div>


			<div className='talk-list'>
				<h2>Fale sobre:</h2>
				<div>
					<p>Faltas</p>
					<p>Pagamento de mensalidade</p>
					<p>Piadas</p>
					<p>Recuperação de Senha</p>
				</div>
				<span>Lembre-se, seja educado :D</span>
			</div>
		</>
	);
}

export default App;
