import {useEffect, useState} from 'react'
import styles from './Total.module.css';
import Row from "../Row.jsx";



function Total({data}) {

    const [value, setValue] = useState(null)

    useEffect(() => {
        setValue(data);
    }, [data]);



    return (
    <div className={styles.total}>

        <Row label={"Total Energy Usage:"}
             value={!value ? "-" : value.usageElectricity}
             type={"kWh"} />

        <Row label={"Monthly Energy Usage:"}
             value={!value ? "-" : value.moneySpent}
             type={"$"} />



    </div>
  )
}

export default Total
