    function calcHeatMap(pointsource)
    {
      var heatmapLayer = new ol.layer.Heatmap({
        title: 'Heatmap',
        source: pointsource,
        blur: 18,  //controls how much the values are averaged (higher values show clusters)
        radius: 10, //controls the size of individual dots
        gradient: ['#0f0', '#ff0', '#f00']  //['#00f', '#0ff', '#0f0', '#ff0', '#f00'].
      });
      return heatmapLayer;
    }
  
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
      // comment the following two lines to have the mouse position
      // be placed within the map.
      //className: 'custom-mouse-position',
      //target: document.getElementById('mouse-position'),
      undefinedHTML: '&nbsp;'
    });

    var osmLayer = new ol.layer.Tile({
        source: new ol.source.OSM()
    });

    function transform_geometry(element) {
      var current_projection = new ol.proj.Projection({code: "EPSG:4326"});
      var new_projection = osmLayer.getSource().getProjection();
  
      element.getGeometry().transform(current_projection, new_projection);
    }

    var point_feature1 = new ol.Feature({
      geometry: new ol.geom.Point([20, 54])
    });

    var point_feature2 = new ol.Feature({
      geometry: new ol.geom.Point([20, 20])
    });

    var point_feature3 = new ol.Feature({
      geometry: new ol.geom.Point([54, 54])
    });

    var point_feature4 = new ol.Feature({
      geometry: new ol.geom.Point([-2, 54])
    });

    transform_geometry(point_feature1);
    transform_geometry(point_feature2);
    transform_geometry(point_feature3);
    transform_geometry(point_feature4);

    var patients = new ol.source.Vector({
        //url: 'http://127.0.0.1:8000/static/vectors/patients.geojson', //TODO: Change that url
        //format: new ol.format.GeoJSON()
        features: [point_feature1, point_feature2, point_feature3, point_feature4]
    });

    var countries = new ol.source.Vector({
        url: 'http://127.0.0.1:8000/static/vectors/World.geojson', //TODO: Change that url
        format: new ol.format.GeoJSON()
    }); 
 
    var countriesLayer = new ol.layer.Image({
        title: 'Countries',
        source: new ol.source.ImageVector({
           source: countries,
           style: citiesStyle
        })
    });

    var patientsLayer = new ol.layer.Image({
        title: 'Patients',
        source: new ol.source.ImageVector({
           source: patients,
           style: patientsStyle
        })
    });


    var heatmap = calcHeatMap(patients);
    overlayGroup.getLayers().push(heatmap);
    
    var map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Group({
                'title': 'Base maps',
                layers: [
                    osmLayer,
                    countriesLayer,
                    //patientsLayer
                ]
            }),
            overlayGroup
        ],
        view: new ol.View({
          //center: [2068310.1055,7250493.7712], //gdansk
          center: [2118452.7960550743,6879927.0580734685],
          zoom: 2.5
        })
    });

    var layerSwitcher = new ol.control.LayerSwitcher();
    map.addControl(layerSwitcher);
    var mousePosition = new ol.control.MousePosition();
    map.addControl(mousePosition);
 
   
    function choroMap()
    {
        var choropleth = calcPointsinPolygons(patients,countries);
        overlayGroup.getLayers().push(choropleth);
    }

//===============================================================================================================================
	var sourceEventListener = countries.once('change', function(e) {
	  if (countries.getState() == 'ready') {
		console.log('GeoJSON loaded');
		choroMap();
		countries.un('change', sourceEventListener);
	  }
	});