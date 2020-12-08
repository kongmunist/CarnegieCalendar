import React from 'react'
import { Button, Card, Header, Icon, Modal, Segment } from 'semantic-ui-react'

export default function EventModal (props) {
  const { description, summary, location, url, dateRange } = props
  const descStyle = { overflowWrap: 'break-word', wordBreak: 'break-all', whiteSpace: 'pre-wrap' }
  const textStyle = { overflowWrap: 'break-word', wordBreak: 'break-all', overflow: 'hidden', whiteSpace: 'nowrap', textOverflow: 'ellipsis' }
  return (
    <Modal
      closeIcon
      closeOnDimmerClick={true}
      dimmer='inverted'
      open={props.open}
      style={{width: '80%', height: '80%', overflow: 'scroll', textOverflow: 'ellipsis', background: 'snow'}}
    >
      <Modal.Header style={{background:'#77212E', color:'snow'}}>Event Details</Modal.Header>
      <Modal.Content style={{background:'snow'}}>
        <Modal.Description>
          <Segment>
            <Header>{summary}</Header>
            <div className='date'><Icon name="clock"/>{dateRange}</div>
            {location && <div className='location'><Icon name="map marker"/>{location}</div>}
            {url && <div className='link'>
              <Icon name="paperclip"/>
              <a className='event-href' href={url} rel='noopener noreferrer' target='_blank'>Open Link</a>
            </div>}
          </Segment>
          <p style={descStyle}>
            {description}
          </p>
        </Modal.Description>
      </Modal.Content>
    </Modal>
  )
}