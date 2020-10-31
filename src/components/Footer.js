import React from 'react'
import { Container } from 'semantic-ui-react'

export default function HeaderRegion () {
  let footerCSS = {
    fontSize: 16, 
    color: "#FFF5EE", 
    position: "relative", 
    top:"35%", 
    textAlign: "center"
  }
  
  return (
    <Container text textAlign="center" style={footerCSS}>
      Developed by: something something
    </Container>
  )
}