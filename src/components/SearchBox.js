import React, { useState } from 'react';
import { Form, Input, Button, Icon } from 'semantic-ui-react'
import { DatesRangeInput } from 'semantic-ui-calendar-react';


export default function SearchBox (props) {

  const [searchQuery, setSearchQuery] = useState('');
  const [datesRange, setDatesRange] = useState('');

  const handleSubmit = () => {
    props.setIsLoading(true)
    console.log('is loading')

    console.log(searchQuery, datesRange) // for testing purpose
    let dates = datesRange.split(" - ")
    let start = Date.parse(dates[0])
    let end = Date.parse(dates[1])
    console.log(start, end) // for testing purpose

    // TO-DO: pass searchQuery, start and end to API
    if (isNaN(start)) {
      start = ""
    }
    if (isNaN(end)) {
      end = ""
    }

    let api_url = `http://127.0.0.1:5050/search?search_str=${searchQuery}&start_time=${start}&end_time=${end}`;
    // TO-DO: once API is hosted, change API call, add other parameters
    // TO-DO: remind other people working on frontend to take in content as props
    fetch(api_url)
      .then(response => response.json())
      .then(data => {
        props.setEvents(data)
        props.setIsLoading(false)
      });
    console.log(api_url)
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
      dateFormat="YYYY-MM-DD"
      popupPosition="left center"
      value={datesRange}
      iconPosition="left"
      allowSameEndDate={true}
      clearable={true}
      clearIcon={<Icon name="undo" color="grey"/>}
      onChange={(event, {name, value}) => handleDateChange(event, {name, value})}
    />
  )

  const formCSS = {
    width: "100%",
    minWidth: 200,
  }

  const labelCSS = {
    textAlign: 'left',
    padding: 5,
    fontSize: 20,
    fontWeight: 'bold',
    width: "100%",
    color: "#77212E"
  }

  const buttonCSS = {
    marginTop: 20,
    backgroundColor: "#77212E",
    color: '#FFF5EE',
    height: 50,
    width: "30%",
    minWidth: 125,
    fontSize: 16,
  }

  // TO-DO: fix date range: either disable keyboard input or make it work normally
  return (
    <Form onSubmit={handleSubmit} inverted={true} size="big" style={{width: 520, padding: 20}}>
      <h1 style={labelCSS}>Search</h1>
      <Form.Field
        style={formCSS}
        control={Input}
        onChange={(e, value) => handleQueryChange(e, value)}
        placeholder='Search for space-separated keyword(s).'
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




