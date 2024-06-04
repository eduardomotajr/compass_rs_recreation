"use client";

// import { DarkThemeToggle } from "flowbite-react";
import { Initial } from "./initial";
import { Cards } from "./card";
import { FooterCustom } from "./footer";
import Grid from '@mui/material/Unstable_Grid2'; // Grid version 2
import React,  { useState }  from "react";
import axios from "axios"; 


export default function Home() {
  const [datas, setdata] = useState({
    qt_cards: [],
    g1: [],
  });


  axios({
    method: "GET",
    url:"http://localhost:5000/",
  }).then((response) => {
    const res = response.data
    setdata(({
      qt_cards: res,
      g1: datas.g1,}))
  })

  // const dados = datas.teste;
  // console.log(datas.g1)
  // const dados = [1,2,3];
  // useEffect(() => {
  //   fetch("/").then((res) => 
  //     res.json().then((data) => {
  //       setdata({teste: data.teste,})
  //       console.log(data.teste)
  //     })
  //   )
  // }, []);

  
  return (
    <>    
      <div className="dark:bg-gray-800">
        <Initial />
        <Grid container spacing={1} className="card-margin-div">
          {datas.qt_cards.map((d) => (<Grid xs={4} spacing={1}><Cards i={d}/></Grid>))}
        </Grid>
        <FooterCustom />
      </div>
    </>
  );
}
