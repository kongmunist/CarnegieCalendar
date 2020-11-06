import React from 'react'
import { Container } from 'semantic-ui-react'

export default function HeaderRegion () {
  let footerCSS = {
    fontSize: 16, 
    color: "#FFF5EE", 
    position: "relative", 
    paddingTop: 37, 
    textAlign: "center",
  }
  
  return (
    <Container text style={footerCSS}>
      Developed by: Scotty Labs
    </Container>
  )
}