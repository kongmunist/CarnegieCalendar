import React, { useState } from 'react';
import './App.css';
import { Container, Grid } from 'semantic-ui-react'
import HeaderRegion from './components/HeaderRegion'
import ResultsList from './components/ResultsList'
import SearchBox from './components/SearchBox'
import Footer from './components/Footer'

function App() {
  const [events, setEvents] = useState([])

  let footerStyle = {
    backgroundColor: '#77212E',
    position: 'fixed',
    height: 90,
    width: '100%',
    bottom: 0,
    verticalAlign: 'middle'
  }

  return (
    <div className="App" style={{positive:"relative", minHeight:"100vh"}}>
      <Container style={{marginBottom:150}}>
        <Grid centered padded>
          <Grid.Row>
            <HeaderRegion />
          </Grid.Row>

          <Grid.Row>
            <SearchBox setContent={setEvents} />
          </Grid.Row>

          <Grid.Row>
            <ResultsList events={events} />
          </Grid.Row>
        </Grid>
      </Container>

      <Grid.Row style={footerStyle}>
        <Footer/>
      </Grid.Row>
    </div>
  );
}

export default App;
