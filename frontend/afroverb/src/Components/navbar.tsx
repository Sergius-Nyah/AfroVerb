import React from 'react'

export const Navbar = () => {
  return (
    <>
    <header>
        <div id="header">
        <div className="logo"><h3 id='logoname'>AfroVerb</h3> <img id='logo' src="/images/afro_image_1.png" alt="Logo" /></div>
        <nav>
        <a href="#Pricing" id='text'>Pricing</a>
        <button className='btn'><a href="#Login">Login</a></button>
        <button className='btn1'><a href="#traslate_page">Start Translating</a></button>
        </nav>
        </div>

    </header>
    </>
  )
}
