import { DarkThemeToggle, Flowbite } from "flowbite-react";
// import React, { Text } from 'react-native';
import React from 'react';                              

export function Initial() {
  return ( 
      <div className="flex min-h-home items-center justify-center gap-2 dark:bg-gray-800">
        <h1 className="text-3xl font-bold dark:text-white">As Enchentes no Rio Grande do Sul</h1>
        {/* <spam><h1 className="text-2xl dark:text-white">As Enchentes no Rio Grande do Sul</h1></spam>
        <spam><h1 className="text-2xl dark:text-white">As Enchentes no Rio Grande do Sul</h1></spam> */}
          <DarkThemeToggle className="display-off"/>
        <img src="https://compass.uol/etc.clientlibs/compass/clientlibs/clientlib-react/resources/static/media/logo.d35fe3b1.svg" alt="0" />
      </div>
  );
}
