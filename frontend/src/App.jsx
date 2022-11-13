import { useState } from 'react'
import './App.css'
import Bubble from './Bubble'
function App() {
  return (
    <div className='app'>
      <div className="mobile">
        <div className="dislnd">
        <div className="cameraWrapper">
        <div className="camera"></div>
        <div className="camera"></div>
        </div>  
        </div>
      <div className="screen">
        <div className="titleContainer">
          <h1 className="titleBox">Chat-Botswal</h1>
        </div>
        <div className="chatBox">
              <Bubble text="Hi my name is Lodu! I am an IITian and right now I am studing in fjsklfdsjfkdsajfkldsfjdsklfjdsflkjdsfksdjfkldsjfsklfjkdslfjdslfjdskfjdslfjdsakfljdsflkjkjlkjkljkljkljlkjkljlkjl" bot={true}/>
              <Bubble text="Hi my name is Lodu!" bot={false}/>

        </div>
        <div className="inputChatBox">
          <input type="text" name="" id="" className="inputBox" placeholder='Type here something...'/>
          <div className="submit">SEND</div>
        </div>
      </div>
    </div>
    </div>
    );
}

export default App
