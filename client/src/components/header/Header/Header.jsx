import { useState } from 'react'
import styles from './Header.module.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faBell, faHome, faLaptop, faSignOut} from '@fortawesome/free-solid-svg-icons'
import Menu from "../Menu/Menu.jsx";

function Header({onPageChange, page}) {


  return (
    <div className={styles.header}>

        <div className={styles.logo}>
            <div className={styles.logo__name}>TUKE</div>
            <div className={styles.logo_additional}>Solaris | B526</div>
        </div>

        <Menu onPageChange={onPageChange} page={page} />

        <div className={styles.logout}><FontAwesomeIcon icon={faSignOut}/></div>

    </div>
  )
}

export default Header
