import './App.css';
import { useState } from 'react';

// let words = ['hello', 'word', 'programming'];
// let len = words.length;
// let test_input = 


function check_word(word) {

}

function App() {
  const [input, handleInput] = useState('');

  const handleChange = event => {
    if (event.key === 'Space') {
      check_word(event.target.value);
    }
  };

  return (
    <div className="grid place-items-center place-content-center">
      <div>
        <p className="text-rose-600">{input}<input type="file" className="fileSelector"/></p>
      </div>
      <p className="p-10">Et duis culpa irure ad sint ut est esse laboris occaecat laboris mollit.</p>
      <input type="text" className="txtarea" id="input" value={input} onKeyDown={handleChange}/>
    </div>
  );
}

export default App;
