import React from 'react'
import { Maps } from './maps'

export const Section1 = () => {
  return (
    <>
    <div className="section">
        <div className="left_div">
            <h1>Seamless Real-Time Translation Accross Africa's Languages</h1>
            <h5>Join thousands of users overcome language barriers with ease</h5>
            <div className='button_div'>
                <button className='btn' ><a href="#Try out">Try Out Now</a></button>
                <button className='btn1'><a href="#SignUp">Set Up An Account</a></button>
            </div>
        </div>
        <div className="right_div">
            <Maps />
        </div>
    </div>
    </>
  )
}
