import {useEffect, useState} from 'react'
import styles from './Dashboard.module.css';
import Temperature from "../widgets/Temperature/Temperature.jsx";
import {menu_items} from "../../../data/menu.js";
import Visitors from "../widgets/Visitors/Visitors.jsx";
import {dataPayload} from "../../../data/data.js";
import Item from "../widgets/Item/Item.jsx";
import DeviceSwitchable from "../devices/DeviceSwitchable/DeviceSwitchable.jsx";
import Setting from "../settings/Setting/Setting.jsx";
import Total from "../widgets/Total/Total.jsx";


function Dashboard({onScenario,onPayload, data}) {


    const [temperature, setTemperature] = useState(dataPayload.air)
    const [total, setTotal] = useState(dataPayload.total)

    const [visitors, setVisitors] = useState(dataPayload.visitors)
    const [computers, setComputers] = useState(dataPayload.computers)

    const [switchables, setSwitchables] = useState(dataPayload.switchables)

    const [settings, setSettings] = useState(dataPayload.settings)

    useEffect(() => {

        if (!data.air)
            setTemperature(dataPayload.air)
        else
            setTemperature(data.air)

        if (!data.visitors)
            setVisitors(dataPayload.visitors)
        else
            setVisitors(data.visitors)

        if (!data.computers)
            setComputers(dataPayload.computers)
        else
            setComputers(data.computers)

        if (!data.switchables)
            setSwitchables(dataPayload.switchables)
        else
            setSwitchables(data.switchables)

        if (!data.settings)
            setSettings(dataPayload.settings)
        else
            setSettings(data.settings)

        if (!data.total)
            setTotal(dataPayload.total)
        else
            setTotal(data.total)


    }, [data]);


  return (
    <div>
      <div className={styles.dashboard__title}>Statistic</div>

        <div className={styles.dashboard__content}>

            <Temperature data={temperature}/>
            <Visitors data={visitors}/>
            <Total data={total}/>
            {
                computers.map((computer,index) => {
                    return (
                        <Item key={index} data={computer} />
                    )
                })
            }


        </div>

        <div className={styles.dashboard__title}>Recently Devices</div>

        <div className={styles.dashboard__content_scrollable}>

            {
                switchables.map((device,index) => {
                    return (
                        <DeviceSwitchable key={index} data={device} onChange={onPayload}/>
                    )
                })
            }

        </div>

        <div className={styles.dashboard__title}>Settings</div>

        <div className={styles.dashboard__content_scrollable}>

            {
                settings.map((setting,index) => {
                    return (
                        <Setting key={index} data={setting} onScenario={onScenario}/>
                    )
                })
            }

        </div>

    </div>
  )
}

export default Dashboard
