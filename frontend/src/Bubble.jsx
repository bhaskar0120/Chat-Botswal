
import './bubble.css'

function App(props) {
    return (
     <div className={props.bot?"bubbleBot":"bubbleUser"}>
        <div className="chat">{props.text}</div>
     </div>
      );
  }
  
  export default App
  