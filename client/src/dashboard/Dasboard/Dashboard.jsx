import {useEffect, useState} from 'react'
import styles from './Dashboard.module.css';
import Temperature from "../widgets/Temperature/Temperature.jsx";
import {menu_items} from "../../data/menu.js";

function Dashboard({onPayload, data}) {

    const [value, setValue] = useState(null)

    useEffect(() => {
        setValue(data);
    }, [data]);


  return (
    <div>
      <div className={styles.dashboard__title}>Statistic</div>

        <div className={styles.dashboard__content}>

            <Temperature data={value}/>

        </div>


    </div>
  )
}

export default Dashboard
