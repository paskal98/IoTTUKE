import {useEffect, useState} from 'react'
import styles from './Item.module.css';
import Row from "../Row.jsx";



function Item({data}) {

    const [value, setValue] = useState(null)

    useEffect(() => {
        setValue(data);
    }, [data]);


    return (
    <div className={styles.item}>

        <div className={styles.item__header}> {!value ? "-" : value.name} </div>

        <div className={styles.item__content}>
            <Row label={"Usage Time:"}
                 value={!value ? "-" : value.usageTime}
                 type={"h"} />

            <Row label={"Last Start:"}
                 value={!value ? "-" : value.usageLast}
                 type={"h ago"} />

            <Row label={"Electricity Used:"}
                 value={!value ? "-" : value.usageElectricity}
                 type={"kWh"} />

            <Row label={"Money Spent:"}
                 value={!value ? "-" : value.moneySpent}
                 type={"$"} />
        </div>

    </div>
  )
}

export default Item
