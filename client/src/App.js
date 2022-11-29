import React ,{useState, useEffect} from 'react'
import Plot from 'react-plotly.js';

// useState will be used as a state varaible that will contain the data from the backend. Will also be used to render data on frontend 
// useEffect will be used to fetch the backend api
function App() {

  // data is the variable and setDatat is the fucntion we can use to manipulate the state of the 'data' variable.
//   const [data, setData] = useState([{}])
//   // using useEffect to fetchg the route '/members' from the flask backend
//   // what ever the response the fetch gives us 'res' we put that reponse into a json()
//   // whatever data is inside the json we are going to put that data into the 'data' varaible using the setData functions
//   useEffect(() => {
//     fetch("/members").then(
//       res => res.json()
//     ).then(
//       data =>{
//         setData(data)
//         console.log(data)
//       }
//     )
//   }, [])

//   return (
//     <div>
//       {(typeof data.members === 'undefined') ? (
//         <p>Loading ...</p>
//         ) : (
//           data.members.map((member, i) => (
//             <p key={i}>{member}</p>  
//           ))
//           // <p> {data.members} </p>
//       )}
//     </div>
//   )
// }
  const [plot, setPlot] = useState(0);
  
  useEffect(() => {
    fetch('/plot_datautils').then(
      res => res.json()
      ).then(data => {setPlot(data);});}, []);
    // console.log(plot)
  
  return (
    <div className='content'>
    <h1>Test Plot</h1>
    <Plot data={plot.data} layout={plot.layout}/>
    </div>
  );
};

export default App
      