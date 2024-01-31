import {useEffect, useState} from 'react'
import styles from './Temperature.module.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faBell, faHome, faLaptop, faSignOut} from '@fortawesome/free-solid-svg-icons'
import Row from "../Row.jsx";


function Temperature({data}) {

    const [value, setValue] = useState(null)

    useEffect(() => {
        setValue(data);
    }, [data]);
    


    return (
    <div className={styles.temperature}>

        <Row label={"Temperature Inside:"}
             value={!value ? "-" : value.temperature.inside}
             type={"°C"} />

        <Row label={"Temperature Outside:"}
             value={!value ? "-" : value.temperature.outside}
             type={"°C"} />

        <Row label={"Humidity:"}
             value={!value ? "-" : value.humidity}
             type={"%"} />

        <Row label={"Comfort Rate:"}
             value={!value ? "-" : value.comfortRate}
             type={""} />


    </div>
  )
}

export default Temperature
