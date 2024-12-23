# Business-intelligence-et-analyse-de-donn-es-L3
# Liens Utiles

## Outils de Développement
- [v0.dev](https://v0.dev/chat/WXCjBh2yD4Z) - Plateforme de design/développement (elle a été conçu par V0.dev, c'est un outils Ai (intelligence artificial) cliquez  pour vusualiser l'application.
- [GitHub](https://github.com) - Gestion de code source
- [VS Code](https://code.visualstudio.com) - Éditeur de code

# Seismic Activity Dashboard

## Overview
Interactive dashboard displaying recent seismic activity using Next.js, React, Recharts for graphs and Leaflet for mapping.

## Application Structure
- `pages/index.tsx`: Main logic and homepage structure 
- `components/Map.tsx`: Map display component
- `styles/`: CSS modules and global styles

## Core Features

### Data Retrieval 
- USGS API integration for recent earthquakes
- Real-time data loading with `useEffect`

### Data Visualization
1. **Events Table**
  - Details of each seismic event
  - Title, magnitude, coordinates
  
2. **Magnitude Graph**
  - Bar chart using Recharts
  - Visual magnitude comparison

3. **Interactive Map**
  - React-Leaflet implementation  
  - Magnitude-proportional markers

### Export Functionality
- CSV data download option

## Key Components

### Main Page (`index.tsx`)
```typescript
// State management & data fetching
const [seismicData, setSeismicData] = useState([]);

// API integration
useEffect(() => {
 fetchSeismicData();
}, []);

Map Component (Map.tsx)
// Interactive map implementation
const MapComponent = ({ data }) => {
  return (
    <MapContainer>
      {data.map(event => (
        <Marker position={[event.lat, event.lng]}>
          <Popup>{event.title}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

Styling

CSS Modules for component styling
Responsive Flexbox layout

Features Roadmap

 Custom data filters
 Search functionality
 UI animations
 Real-time updates
 Advanced analytics

Installation
bashCopygit clone [repository-url]
npm install
npm run dev
Dependencies

Next.js
React
Recharts
React-Leaflet
CSS Modules

Contributing

Fork repository
Create feature branch
Submit pull request

License
MIT License: open
Contact
johnbaumbilia@gmail.com

