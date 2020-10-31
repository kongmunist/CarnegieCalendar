import React from 'react'
import { Card } from 'semantic-ui-react'

export default function ResultCard (props) {
  // This is just boilerplate
  // TODO: Add functional card component
  return (
    <Card fluid>
      <Card.Content>
        <Card.Header>Generic card title</Card.Header>
        <Card.Meta>
          <span className='date'>Generic card metadata</span>
        </Card.Meta>
        <Card.Description>
          Generic card description
        </Card.Description>
      </Card.Content>
    </Card>
  )
}