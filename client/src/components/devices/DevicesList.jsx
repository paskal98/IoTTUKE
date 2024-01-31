
import styles from "./DevicesList.module.css"
import {DataTable} from "primereact/datatable";
import {Column} from "primereact/column";
import {Button} from "primereact/button";
import {Dialog} from "primereact/dialog";
import {useState} from "react";
import DeviceDetailed from "./DeviceDetailed.jsx";
import {listOfDevices} from "../../data/data.js";

function DevicesList() {

    const devices = listOfDevices;

    const [addDeviceMode,SetAddDeviceMode] = useState(false)


    return (
        <div>
            <div className={styles.device__list__top__container}>
                <div className={styles.device__header__text}>Devices List</div>
                <Button label="Add new device" icon="pi pi-plus" iconPos="left" onClick={()=> SetAddDeviceMode(true)}/>

            </div>


            <DataTable paginator rows={6} value={devices} removableSort>
                <Column field="name" header="Name" sortable></Column>
                <Column field="serialNumber" header="Serial Number" sortable></Column>
                <Column field="battery" header="Battery" sortable></Column>
                <Column field="workingTime" header="Working Time" sortable></Column>
                <Column field="activity" header="Last Activity" sortable></Column>
            </DataTable>

            <Dialog  draggable={false} visible={addDeviceMode} style={{ width: '90vw' , height:' 125.6vh'}}  onHide={() => SetAddDeviceMode(false)}>
                        <DeviceDetailed/>
            </Dialog>



        </div>
    )
}

export default DevicesList;
