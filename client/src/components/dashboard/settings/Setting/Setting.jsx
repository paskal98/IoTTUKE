import {useEffect, useState} from 'react'
import styles from './Setting.module.css';
import Row from "../Row.jsx";



function Setting({onScenario,data}) {

    const [value, setValue] = useState(null)

    useEffect(() => {
        setValue(data);
        console.log(data)
    }, [data]);

    function handleChange(change){
        onScenario(change)
    }

    return (
    <div className={styles.item}>

        <div className={styles.item__header}> {!value ? "-" : value.title} </div>

        <div className={styles.item__content}>
            {
                !value ? null : value.options.map((option,index) => {
                    return (
                        <Row key={index}
                             value={!value ? "-" : option}
                             type={value.type}
                             onChange={handleChange} />
                    )
                })
            }

        </div>

    </div>
  )
}

export default Setting
