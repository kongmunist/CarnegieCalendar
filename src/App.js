import React, { useState } from 'react';
import Search from './search';
import './App.css';

function App() {
  const [content, setContent] = useState([])

  console.log(content);

  return (
    <div className="App">
      <header className="App-header">
        <Search setContent={setContent}/>
        {/* <SearchResults content={content}/> */}
      </header>
    </div>
  );
}

export default App;
