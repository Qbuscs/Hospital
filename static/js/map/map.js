function loadMap(){
  let date = new Date();
  let start = date.getTime();

  $("#map").css("display", "block");
  $("#wait-message").css("display", "block");
  $("#map-btn").css("display", "none");

  var patientsStyle = new ol.style.Style({
        image: new ol.style.Circle({
          radius: 5,
          stroke: new ol.style.Stroke({
            color: '#000',
            width: 2
          })
        })
      });

  var citiesStyle = new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgba(0,0,0,0.75)',
          width: 1
        })
      });

  var overlayGroup = new ol.layer.Group({
      title: 'Overlays',
      layers: [
      ]
  });
      
  var mousePositionControl = new ol.control.MousePosition({
    coordinateFormat: ol.coordinate.createStringXY(4),
    projection: 'EPSG:900913',
    undefinedHTML: '&nbsp;'
  });

  var osmLayer = new ol.layer.Tile({
      source: new ol.source.OSM()
  });

  var countriesLayer = new ol.layer.Image({
      title: 'Countries',
      source: new ol.source.ImageVector({
        source: countries,
        style: citiesStyle
      })
  });

  function transform_geometry(element) {
    var current_projection = new ol.proj.Projection({code: "EPSG:4326"});
    var new_projection = osmLayer.getSource().getProjection();

    element.getGeometry().transform(current_projection, new_projection);
  }

  patients_features.forEach(feature => {
    transform_geometry(feature);
  });

  var patients = new ol.source.Vector({
      features: patients_features
  });

  var patientsLayer = new ol.layer.Image({
      title: 'Patients',
      source: new ol.source.ImageVector({
        source: patients,
        style: patientsStyle
      })
  });
      
  var map = new ol.Map({
      target: 'map',
      layers: [
          new ol.layer.Group({
              'title': 'Base maps',
              layers: [
                  osmLayer,
                  countriesLayer,
              ]
          }),
          overlayGroup
      ],
      view: new ol.View({
        center: [2118452.7960550743,6879927.0580734685],
        zoom: 2.5
      })
  });
    
  function choroMap()
  {
      var choropleth = calcPointsinPolygons(patients,countries);
      overlayGroup.getLayers().push(choropleth);
      $("#wait-message").css("display", "none");
      date = new Date();
      console.log("Time [ms] = " + (date.getTime() - start));
  }

  var sourceEventListener = countries.once('change', function(e) {
    if (countries.getState() == 'ready') {
    choroMap();
    countries.un('change', sourceEventListener);
    }
  });

}