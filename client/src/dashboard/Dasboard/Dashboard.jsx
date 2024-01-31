import {useEffect, useState} from 'react'
import styles from './Dashboard.module.css';
import Temperature from "../widgets/Temperature/Temperature.jsx";
import {menu_items} from "../../data/menu.js";
import Visitors from "../widgets/Visitors/Visitors.jsx";
import {dataPayload} from "../../data/data.js";


function Dashboard({onPayload, data}) {


    const [temperature, setTemperature] = useState(dataPayload.air)
    const [visitors, setVisitors] = useState(dataPayload.visitors)

    useEffect(() => {

        if (!data.air)
            setTemperature(dataPayload.air)
        else
            setTemperature(data.air)

        if (!data.visitors)
            setVisitors(dataPayload.visitors)
        else
            setVisitors(data.visitors)


    }, [data]);


  return (
    <div>
      <div className={styles.dashboard__title}>Statistic</div>

        <div className={styles.dashboard__content}>

            <Temperature data={temperature}/>
            <Visitors data={visitors}/>

        </div>


    </div>
  )
}

export default Dashboard
