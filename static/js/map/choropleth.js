  var maxPointsperPolygon = 0;
  
  function makeGradientColor(color1, color2, percent)
  {
    var newColor = {};

    function makeChannel(a, b) {
        return(a + Math.round((b-a)*(percent/100)));
    }

    function makeColorPiece(num) {
        num = Math.min(num, 255);   // not more than 255
        num = Math.max(num, 0);     // not less than 0
        var str = num.toString(16);
        if (str.length < 2) {
            str = "0" + str;
        }
        return(str);
    }

    newColor.r = makeChannel(color1.r, color2.r);
    newColor.g = makeChannel(color1.g, color2.g);
    newColor.b = makeChannel(color1.b, color2.b);
    newColor.cssColor = "#" + 
                        makeColorPiece(newColor.r) + 
                        makeColorPiece(newColor.g) + 
                        makeColorPiece(newColor.b);
    return(newColor);
  }


  function choroplethStyleFunction(feature, resolution)
  {
    var value = feature.get('REMARKS_2');
    var maxValue = maxPointsperPolygon;
    var percentage = Math.round((value/maxValue)*100);
    var featureColor = null;

    //create linear gradient:
    var red = {r:255, g:0, b:0};      //100%
    var yellow = {r:255, g:255, b:0}; //50%
    var green = {r:0, g:255, b:0}     //0%
   
    if (percentage>50)
    {
        featureColor = makeGradientColor(yellow, red, Math.round(((percentage-50)/50)*100));
    }
    else
    {
        featureColor = makeGradientColor(green, yellow, Math.round(((percentage)/50)*100));
    }

    return [new ol.style.Style({
        fill: new ol.style.Fill({
          color: [featureColor.r, featureColor.g, featureColor.b, 0.5]
        }),
        stroke: new ol.style.Stroke({
          color: '#000000'
        })
    })];
  }

  function calcPointsinPolygons(pointsource,polygonsource)
  {
 // point in polygon:
    var parser = new jsts.io.olParser();
    var pointFeatures = pointsource.getFeatures();
    var polygonFeatures = polygonsource.getFeatures();

    var jstsPoints = [];  //= parser.read(pointsource);
    var jstsPolygons = []; //= parser.read(polygonsource);

    //convert OL geometry to JSTS geometry:
    for (var i=0; i<polygonFeatures.length;i++)
    {
        jstsPolygons[i]=parser.read(polygonFeatures[i].getGeometry());
        //alert(jstsPolygons[i]);
    }

    for (var i=0; i<pointFeatures.length;i++)
    {
        jstsPoints[i]=parser.read(pointFeatures[i].getGeometry());
    }

    //count points in polygons:
    var numPointsinPolys = new Array(jstsPolygons.length);
    var maxPoints = 0;
    var pointsMatched = 0;
    for (var i=0; i<jstsPolygons.length;i++)
    {
        numPointsinPolys[i]=0;
        for (var j=0; j<jstsPoints.length;j++)
        {
            if (jstsPolygons[i].contains(jstsPoints[j]))
            {
                // jstsPoints[j].coordinate = new jsts.geom.Coordinate();
                numPointsinPolys[i]+=1;
                pointsMatched += 1;
            }
        }
        //save results:
        //polygonFeatures[i].U.REMARKS_2=numPointsinPolys[i]; //here we place the value for the district
        polygonFeatures[i].set('REMARKS_2',numPointsinPolys[i]); //here we place the value for the district
        if (numPointsinPolys[i]>maxPoints)
            maxPoints=numPointsinPolys[i];
    }


    maxPointsperPolygon=maxPoints;

    //save results:  (unnecessarily slows down computations)
/*
    for (var i=0; i<polygonFeatures.length;i++)
    {
        polygonFeatures[i].U.REMARKS_2=numPointsinPolys[i];
        polygonFeatures[i].U.CC_2=maxPoints; //here we place the max value for all districts
    }
*/
    //display results: (need to apply styling to resultlayer!!) 
    var polygonresult = new ol.source.Vector({
        features: polygonFeatures
    });

    var resultlayer = new ol.layer.Image({
        title: 'Choropleth',
        source: new ol.source.ImageVector({
           source: polygonresult,
           style: choroplethStyleFunction
        })
    });

    //map.addLayer(resultlayer);
    return resultlayer;
  }
