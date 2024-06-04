"use client";

import { Card, Button, Drawer } from "flowbite-react";
import Plot from 'react-plotly.js';
import axios from "axios"; 
import React,  { useState }  from "react";
import TextTruncate from 'react-text-truncate';


export function Cards(i: any) {
  const [datas, setdata] = useState({
    g1: {"data": [], "layout": {}, "title": "", "text": ""},
  });
  axios({
    method: "GET",
    url:"http://localhost:5000/graphis"+i.i,
  }).then((response) => {
    const res = response.data
    setdata(({
      g1: res,}))
  })
  const [isOpen, setIsOpen] = useState(false);
  const handleClose = () => setIsOpen(false);

  // const truncate = function(str: any) {
  //   return str.str.length > 10 ? str.substring(0, 7) + "..." : str;
  // }

  return (
    <Card
    className="min-w-sm card-shadow card-color"
    // renderImage={() => <Image width={500} height={500} src="https://compass.uol/etc.clientlibs/compass/clientlibs/clientlib-react/resources/static/media/logo.d35fe3b1.svg" alt="image 1" />}
    >

        <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
          {datas.g1.title}
        </h5>
        <p className="font-normal text-gray-700 dark:text-gray-400">
            <TextTruncate 
              line={3}
              element="p"
              truncateText="..."
              text={datas.g1.text}
              textTruncateChild={<button className="color-read-more" onClick={() => setIsOpen(true)}>Saiba mais</button>}
            />
        </p>
        <Plot 
          data={datas.g1.data} 
          layout={datas.g1.layout}
          config={{"displayModeBar": false}}
        />
        <Button className="compass-color" onClick={() => setIsOpen(true)}>
          Veja Mais
          <svg className="-mr-1 ml-2 h-4 w-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path
              fillRule="evenodd"
              d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
              clipRule="evenodd"
            />
          </svg>
        </Button>
        <Drawer open={isOpen} onClose={handleClose} position="top">
          <Drawer.Header title="Drawer" />
          <h5 className="text-2xl font-bold center-title tracking-tight text-gray-900 dark:text-white">
            {datas.g1.title}
          </h5>
          <div className="flex gap-2">
            <Plot 
              data={datas.g1.data} 
              layout={datas.g1.layout}
              config={{"displayModeBar": false}}
            />
            <p className="font-normal text-gray-700 dark:text-gray-400">
              {datas.g1.text}
            </p>
          </div>
        </Drawer>
    </Card>
  );
}

