import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Header from "./header/Header/Header.jsx";
import { Dialog } from 'primereact/dialog';
import { Button } from 'primereact/button';
import DevicesList from "./components/devices/DevicesList.jsx";
import {menu_items} from "./data/menu.js";
import Dashboard from "./dashboard/Dasboard/Dashboard.jsx";



function App() {
    const [state, setState] = useState(false)
    const [page, setPage] = useState(menu_items[0])

    const [payload, setPayload] = useState([])
    const [receivedData, setReceivedData] = useState([])

    function handleOnPageChange(page){
        setPage(page)
    }

    function handlePayload(payload){

    }


    const [test, setTest] = useState({
        air: {
            temperature : {
                inside : 28,
                outside: 36
            },
            humidity: 34,
            comfortRate: "Low"
        }
    });

    useEffect(() => {
        const eventSource = new EventSource("http://localhost:4001/rates");

        eventSource.onmessage = (event) => {
            const air = JSON.parse(event.data);
            setTest({ ...air });
            setReceivedData({ ...air })
        };

        return () => eventSource.close();
    }, []);


  return (
    <>
        {/*<Header/>*/}
        <Header onPageChange={handleOnPageChange} page={page}/>
        <div className="view__container">
            {/*<DevicesList />*/}
            <Dashboard onPayload={handlePayload} data={receivedData}/>

        </div>



    </>
  )
}

export default App
