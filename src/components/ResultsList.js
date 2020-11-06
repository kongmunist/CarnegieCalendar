import React from 'react'
import ResultCard from './ResultCard'
import { Grid } from 'semantic-ui-react'

export default function ResultsList (props) {
  const getEventID = event => event.description
  return (
    <Grid stackable columns={1}>
      {props.events.map(event => (
        <Grid.Column id={getEventID(event)}>
          <ResultCard event={event} />
        </Grid.Column>
      ))}

      {/* for testing purpose */}
      <Grid.Column>
          <ResultCard/>
          <ResultCard/>
      </Grid.Column>
    </Grid>
  )
}