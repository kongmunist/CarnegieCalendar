import React from 'react'
import ResultCard from './ResultCard'
import { Card } from 'semantic-ui-react'

export default function ResultsList (props) {
  const getEventID = event => event.description
  return (
    <Card.Group itemsPerRow={4} stackable={true}>
      {props.events.map(event => (
        <ResultCard event={event} key={getEventID(event)} />
      ))}
    </Card.Group>
  )
}