import {useEffect, useState} from 'react'
import styles from './Visitors.module.css';
import Row from "../Row.jsx";



function Visitors({data}) {

    const [value, setValue] = useState(null)

    useEffect(() => {
        setValue(data);
    }, [data]);



    return (
    <div className={styles.visitors}>

        <Row label={"Total Today:"}
             value={!value ? "-" : value.today}
             type={"ppl"} />

        <Row label={"Total Week:"}
             value={!value ? "-" : value.week}
             type={"ppl"} />

        <Row label={"Total Month:"}
             value={!value ? "-" : value.month}
             type={"ppl"} />


    </div>
  )
}

export default Visitors
