import {useEffect, useState} from 'react'
import styles from './DeviceSwitchable.module.css';
import socket from '../../../../images/socket.png';
import lamp from '../../../../images/lamp.png';
import def from '../../../../images/default.png';
import {Switch} from "@mui/material";

function DeviceSwitchable({data}) {

    const [value, setValue] = useState(null)
    const [checked, setChecked] = useState(false)

    useEffect(() => {
        setValue(data);
    }, [data]);

    function handleChange(checked){
        setChecked(checked)
        console.log(checked)
    }


    return (
    <div className={styles.device}>

        <div className={styles.device__icon}>
            <img className={styles.device__icon__png}  src={!value ? def : value.type==='socket' ? socket : value.type==='lamp' ? lamp : def} alt='icon'/>
        </div>

        <div  className={styles.device__content}>

            <div  className={styles.device__wrap}>

                <div  className={styles.device__content__info}>
                    <div  className={styles.device__content__info__title}>{!value ? '-' : value.name}</div>
                    <div  className={styles.device__content__info__undertitle}>{!value ? '-' : value.identity}</div>
                </div>

                <div  className={styles.device__content__switch}>
                    <div  className={styles.device__content__switch__button}>
                        <Switch checked={checked} onChange={() =>handleChange(!checked)}/>
                    </div>
                    <div  className={styles.device__content__switch__delim}></div>
                    <div  className={styles.device__content__switch__active}>{!value ? '-' : value.usageTime}</div>
                </div>

                <div  className={styles.device__content__interaction}>Last activity: <span>{!value ? '-' : value.lastActivity}</span></div>

            </div>

        </div>


    </div>
  )
}

export default DeviceSwitchable
