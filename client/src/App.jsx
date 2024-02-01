import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Header from "./components/header/Header/Header.jsx";
import { Dialog } from 'primereact/dialog';
import { Button } from 'primereact/button';
import DevicesList from "./components/devices/DevicesList.jsx";
import {menu_items} from "./data/menu.js";
import Dashboard from "./components/dashboard/Dasboard/Dashboard.jsx";



function App() {
    const [state, setState] = useState(false)
    const [page, setPage] = useState(menu_items[0])

    const [payload, setPayload] = useState([])
    const [receivedData, setReceivedData] = useState({
        air: {
            temperature : {
                inside : "-",
                outside: "-"
            },
            humidity: "-",
            comfortRate: "-"
        }
    });

    function handleOnPageChange(page){
        setPage(page)
    }

    async function handlePayload(payload) {
        console.log(payload);

        const { state, identity } = payload;

        const url = new URL(`http://localhost:4001/switch?identity=${identity}&state=${state}`);
        url.search = new URLSearchParams({ identity, state }).toString();

        try {

            const response = await fetch(url);


            if (!response.ok) {
                throw new Error(`Request failed with status: ${response.status}`);
            }

            const data = await response.json();

            console.log(data);
        } catch (error) {
            console.error("Error fetching data from /switch:", error.message);
        }
    }


    useEffect(() => {
        const eventSource = new EventSource("http://localhost:4001/rates");

        eventSource.onmessage = (event) => {
            const air = JSON.parse(event.data);
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
