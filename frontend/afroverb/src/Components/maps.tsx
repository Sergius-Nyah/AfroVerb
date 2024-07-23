import React from 'react';

export const Maps = () => {
  return (
    <>
      <div className="image-container">
        <img src="/images/afro_image_1.png" style={{ width: '636px', height: '751.564px' }} alt='African map' />
        <div id="Nigeria_map_div">
          <div className="image-container">
            <img src="/images/Ellipse 1.png" alt="Ellipse" />
            <img className="image-overlap" src="/images/Ellipse 2.png" alt="Other Ellipse" />
          </div>
          <div id="Nigerian-flag" className="stacked-image"></div>
        </div>
      </div>
      <div id="Congo_map_div">
        <div className="image-container">
          <div className="image-container">
            <img src="/images/Ellipse 1.png" style={{ width: '60%' }} alt="Ellipse" />
            <img className="image-overlap" src="/images/Ellipse 2.png" style={{ width: '50%' }} alt="Other Ellipse" />
          </div>
          <img id="Congolese_flag" src="/images/Congolese_flag.png" alt="Congolese flag" />
        </div>
      </div>
      <div id="kenya_map_div">
        <div className="image-container">
          <div className="image-container">
            <img src="/images/Ellipse 1.png" style={{ width: '70%' }} alt="Ellipse" />
            <img className="image-overlap" src="/images/Ellipse 2.png" style={{ width: '62%' }} alt="Other Ellipse" />
          </div>
          <img id="kenyan_flag" src="/images/kenyan_flag.png" alt="Kenyan flag" />
        </div>
      </div>
      <div id="woman_flag_div">
        <div id="yellowbackground1">
          <div id="woman_image"></div>
          <div id="Cameroon_map_div">
            <div className="image-container">
              <div className="image-container">
                <img src="/images/Ellipse 1.png" style={{ width: '70%' }} alt="Ellipse" />
                <img className="image-overlap" src="/images/Ellipse 2.png" style={{ width: '62%' }} alt="Other Ellipse" />
              </div>
              <img id="Cameroonian_flag" src="/images/Cameroonian_flag.png" alt="Cameroon flag" />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};