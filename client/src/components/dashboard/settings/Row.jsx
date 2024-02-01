import {useEffect, useState} from 'react'
import styles from './Row.module.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faBell, faHome, faLaptop, faSignOut} from '@fortawesome/free-solid-svg-icons'
import {Switch} from "@mui/material";


function Row({value, onChange,type}) {

    const [checked, setChecked] = useState(false);
    const [data, setData] = useState(false);

    useEffect(() => {
        console.log(value)
        setData(value)
        setChecked(value.isActive)
    }, [value]);

    function handleChange(checked) {
        setChecked(checked);
        onChange([value.id,type])
    }

    return (

        <div className={styles.row}>
            <div className={styles.row__label}>{!value ? '-' : data.name}</div>
            <Switch checked={checked} onChange={() => handleChange(!checked)}/>
        </div>


    )
}

export default Row
