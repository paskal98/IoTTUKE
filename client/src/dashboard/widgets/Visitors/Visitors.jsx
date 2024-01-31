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

        <Row label={"Visitors Today:"}
             value={!value ? "-" : value.today}
             type={"ppl"} />

        <Row label={"Visitors Week:"}
             value={!value ? "-" : value.week}
             type={"ppl"} />

        <Row label={"Visitors Month:"}
             value={!value ? "-" : value.month}
             type={"ppl"} />


    </div>
  )
}

export default Visitors
