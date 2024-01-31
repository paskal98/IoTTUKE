import { useState } from 'react'
import styles from './Menu.module.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faBell, faHome, faLaptop} from '@fortawesome/free-solid-svg-icons'
import {menu_items} from "../../data/menu.js";

function Menu({onPageChange, page}) {

    const [selected, setSelected] = useState(menu_items[0])


    function handleSelected(selected) {
        onPageChange(selected);
        setSelected(selected)
    }


  return (
    <>

        <div className={styles.menu}>
            <div className={selected===menu_items[0] ? `${styles.menu__item_active} ${styles.menu__item}` : styles.menu__item}
                 onClick={() => handleSelected(menu_items[0])}>
                <div className={styles.menu__item__icon}><FontAwesomeIcon icon={faHome}/></div>
                <div className={styles.menu__item__name}>Dashboard</div>
            </div>

            <div className={selected===menu_items[1] ? `${styles.menu__item_active} ${styles.menu__item}` : styles.menu__item}
                 onClick={() => handleSelected(menu_items[1])}>
                <div className={styles.menu__item__icon}><FontAwesomeIcon icon={faLaptop}/></div>
                <div className={styles.menu__item__name}>Devices</div>
            </div>

            <div className={selected===menu_items[2] ? `${styles.menu__item_active} ${styles.menu__item}` : styles.menu__item}
                 onClick={() => handleSelected(menu_items[2])}>
                <div className={styles.menu__item__icon}><FontAwesomeIcon icon={faBell}/></div>
                <div className={styles.menu__item__name}>Alerts</div>
            </div>
        </div>

    </>
  )
}

export default Menu
