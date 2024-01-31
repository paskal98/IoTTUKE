import {useEffect, useState} from 'react'
import styles from './Temperature.module.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faBell, faHome, faLaptop, faSignOut} from '@fortawesome/free-solid-svg-icons'

const val = {
    temperature : {
        inside : 28,
        outside: 36
    },
    humidity: 34,
    comfortRate: "Low"
}

function Temperature({data}) {

    const [value, setValue] = useState(null)

    useEffect(() => {
        setValue(data);
    }, [data]);
    


    return (
    <div className={styles.temperature}>

      <div className={styles.temperature__item}>
        <div className={styles.temperature__item__label}>Temperature Inside:</div>
        <div className={styles.temperature__item__data}>
          <div className={styles.temperature__item__data__value}>{!value ? "-" : value.air.temperature.inside}</div>
          <div className={styles.temperature__item__data__type}>°C</div>
        </div>
      </div>

        <div className={styles.temperature__item}>
            <div className={styles.temperature__item__label}>Temperature Outside:</div>
            <div className={styles.temperature__item__data}>
                <div className={styles.temperature__item__data__value}>{!value ? "-" : value.air.temperature.outside}</div>
                <div className={styles.temperature__item__data__type}>°C</div>
            </div>
        </div>

        <div className={styles.temperature__item}>
            <div className={styles.temperature__item__label}>Humidity:</div>
            <div className={styles.temperature__item__data}>
                <div className={styles.temperature__item__data__value}>{!value ? "-" : value.air.humidity}</div>
                <div className={styles.temperature__item__data__type}>%</div>
            </div>
        </div>

        <div className={styles.temperature__item}>
            <div className={styles.temperature__item__label}>Comfort rate:</div>
            <div className={styles.temperature__item__data}>
                <div className={styles.temperature__item__data__value}>{!value ? "-" : value.air.comfortRate}</div>
            </div>
        </div>

    </div>
  )
}

export default Temperature
