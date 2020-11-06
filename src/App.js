import React, { useState } from 'react';
import './App.css';
import { Container, Grid } from 'semantic-ui-react'
import Nav from './components/Nav'
import HeaderRegion from './components/HeaderRegion'
import ResultsList from './components/ResultsList'
import SearchBox from './components/SearchBox'
import Footer from './components/Footer'

function App() {
  const [events, setEvents] = useState([])

  let navStyle = {
    backgroundColor: '#77212E',
    position: 'fixed',
    height: 80,
    width: '100%',
    verticalAlign: 'middle',
    zIndex: 1
  }

  let footerStyle = {
    backgroundColor: '#77212E',
    height: 100,
    width: '100%',
    bottom: 0,
    verticalAlign: 'middle'
  }

  let eventStyle = {
    backgroundColor: '#8B0000',
    height: 100,
    marginBottom: 200
  }

  return (
    <div className="App" style={{positive:"relative", minHeight:"100vh"}}>
      <Grid.Row style={navStyle}>
        <Nav/>
      </Grid.Row>

      <Container style={{paddingTop:100, marginBottom:150}}>
        <Grid centered padded style={{zindex:0}}>
          <Grid.Row>
            <HeaderRegion/>
          </Grid.Row>

          <Grid.Row>
            <SearchBox setContent={setEvents} />
          </Grid.Row>

          <Grid.Row style={{paddingTop:50}}>
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
