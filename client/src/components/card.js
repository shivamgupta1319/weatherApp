import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

export default function BasicCard(props) {

    const {current,location} = props.weatherDetails;
    console.log(current,location);
  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Typography variant="h5" component="div"   gutterBottom>
          City  =   {location.name}
        </Typography>
        <Typography variant="h5" component="div"   gutterBottom>
            Temperature in F  =   {current.temp_f}
        </Typography>
        <Typography variant="h5" component="div"   gutterBottom>
          Temperature in C  =   {current.temp_c}
        </Typography>
        <Typography variant="h5" component="div"   gutterBottom>
          Humidity  =   {current.humidity}
        </Typography>
        <Typography variant="h5" component="div"   gutterBottom>
          Weather Condition  =   {current.condition.text}
        </Typography>
        
      </CardContent>
      
    </Card>
  );
}