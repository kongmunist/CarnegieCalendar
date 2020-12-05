import React from 'react'

export default function Nav () {
  let footerCSS = {
    fontSize: 24, 
    color: "#FFF5EE", 
    position: "relative", 
    paddingTop: 24,
    paddingLeft: 40, 
    textAlign: "left",
    letterSpacing: 2,
    fontWeight: "bold"
  }
  
  return (
    <h1 style={footerCSS}>
      Carnegie Calendar
    </h1>
  )
}