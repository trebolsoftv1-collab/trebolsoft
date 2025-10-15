
import { View, Text } from 'react-native';
import { useEffect, useState } from 'react';

export default function Home(){
  const [health, setHealth] = useState<string>('...');
  useEffect(()=>{
    fetch(process.env.EXPO_PUBLIC_API_BASE_URL!.replace(/\/$/, '') + '/health')
      .then(r=>r.json()).then(j=>setHealth(j.status)).catch(()=>setHealth('down'))
  },[]);
  return (
    <View style={{flex:1, alignItems:'center', justifyContent:'center'}}>
      <Text>TrebolSoft — Ruta de hoy</Text>
      <Text>API status: {health}</Text>
    </View>
  );
}
