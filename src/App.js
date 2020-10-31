import React, { useState } from 'react';
import './App.css';
import { Container, Grid } from 'semantic-ui-react'
import HeaderRegion from './components/HeaderRegion'
import ResultsList from './components/ResultsList'
import SearchBox from './components/SearchBox'

function App() {
  const [events, setEvents] = useState([])

  // Temporary -- just so we can see the search component
  // TODO: Actually make this look decent
  const searchRowCSS = {
    backgroundColor: '#282c34',
    color: 'white',
    borderRadius: '2em'
  }

  return (
    <div className="App">
      <Container>
        <Grid centered padded>
          <Grid.Row>
            <HeaderRegion />
          </Grid.Row>
          <Grid.Row style={searchRowCSS}>
            <SearchBox setContent={setEvents} />
          </Grid.Row>
          <Grid.Row>
            <ResultsList events={events} />
          </Grid.Row>
        </Grid>
      </Container>
    </div>
  );
}

export default App;
