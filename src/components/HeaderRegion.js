import React from 'react'
import { Container, Header } from 'semantic-ui-react'

export default function HeaderRegion (props) {
  const titleCSS = {
    fontSize: '3.5em',
    marginTop: '0.5em',
    marginBottom: '0'
  }
  const subtitleCSS = {
    marginTop: '0'
  }
  return (
    <Container text>
      <Header as="h1" size="huge" style={titleCSS}>Carnegie Calendar</Header>
      <Header as='h3' style={subtitleCSS}>Your one-stop shop for everything happening at CMU.</Header>
    </Container>
  )
}