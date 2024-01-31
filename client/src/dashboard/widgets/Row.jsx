import {useEffect, useState} from 'react'
import styles from './Row.module.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faBell, faHome, faLaptop, faSignOut} from '@fortawesome/free-solid-svg-icons'


function Row({label, value, type}) {


    return (

        <div className={styles.row}>
            <div className={styles.row__label}>{label}</div>
            <div className={styles.row__data}>
                <div
                    className={styles.row__data__value}>{value}</div>
                <div className={styles.row__data__type}>{type}</div>
            </div>
        </div>


    )
}

export default Row
