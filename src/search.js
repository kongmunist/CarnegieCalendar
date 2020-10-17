import React, { useState } from 'react';
import { Form, Input, Button, Icon } from 'semantic-ui-react'
import { DatesRangeInput } from 'semantic-ui-calendar-react';


export default function Search() {

  const [searchQuery, setSearchQuery] = useState('');
  const [datesRange, setDatesRange] = useState('');

  const handleSubmit = () => {
    console.log(searchQuery, datesRange) // for testing purpose
    // TO-DO: parse searchQuery as a list of keywords
    // TO-DO: pass searchQuery and datesRange to API
  }

  const handleQueryChange = (_, value) => {
    setSearchQuery(value.value)
  }

  const handleDateChange = (_, {name, value}) => {
    setDatesRange(value);
  }

  const DateInput = () => (
    <DatesRangeInput
      name="datesRange"
      placeholder="From - To"
      value={datesRange}
      iconPosition="left"
      clearable={true}
      clearIcon={<Icon name="undo" color="grey"/>}
      onChange={(event, {name, value}) => handleDateChange(event, {name, value})}
    />
  )

  const formCSS = {
    width:500,
  }

  const labelCSS = {
    textAlign: 'left',
    padding: 5,
    fontSize: 20,
    fontWeight: 'bold'
  }

  const buttonCSS = {
    marginTop: 10,
    backgroundColor: 'grey',
    color: 'white'
  }

  return (
    <Form onSubmit={handleSubmit} inverted={true} size="big">
      <h1 style={labelCSS}>Search</h1>
      <Form.Field
        style={formCSS}
        control={Input}
        onChange={(e, value) => handleQueryChange(e, value)}
        placeholder='Search for one or more keyword, separated with commas.'
      />

      <h1 style={labelCSS}>Date</h1>
      <Form.Field
        style={formCSS}
        control={DateInput}
      />

      <Form.Field control={Button} style={buttonCSS}>
        <Icon name="check circle" color="white"/>
        Submit
      </Form.Field>
    </Form>
  )
}




