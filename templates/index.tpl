<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
    <title>RDCEP::Emulator</title>
    <link rel="stylesheet" media="all" href="../static/css/emulator.css"/>
</head>
<body>
<h1 id="heading"> <span>RDCEP</span> :: Emulator</h1>
<div id="back-to-rdcep"><a href="http://www.rdcep.org/">Back to RDCEP</a></div>
<ul id="help-menu">
    <li id="display-help">Help<ul>
        <li><a target="_blank" href="#">RCP Inputs</a></li>
        <li><a target="_blank" href="#">Temperature Output</a></li>
        <li><a target="_blank" href="#">Geographic Regions</a></li>
    </ul></li>
    <li id="view-source"><a href="#">View Source</a></li>
</ul>
<section id="content">
<div id="emulator">
    <section id="intro">
    <p>
        Global Circulation Models, or GCMs, provide scientific estimates of
        future climates. They incorporate everything scientists know about
        climate from weather to the oceans to ice sheets. Our emulator provides
        a compact statistical representation of these models of future climate.
        We have &lsquo;trained&rsquo; the emulator to reproduce the output of
        the Community Climate System Model 4 GCM experiments. The emulator is
        able to reproduce the climate along four ‘Representative Concentration
        Pathways&rsquo; (RCPs), which are plausible trajectories of
        anthropogenic emissions between 2006 and 2100.
    </p>
    </section>
    <section>
        <div id="input">
            <h2>CO<sub>2</sub> Trajectory (ppm)</h2>
            <div><h3>RCP26</h3><div id="RCP26" class="input active"></div></div>
            <div><h3>RCP45</h3><div id="RCP45" class="input"></div></div>
            <div><h3>RCP60</h3><div id="RCP60" class="input"></div></div>
            <div><h3>RCP85</h3><div id="RCP85" class="input"></div></div>
        </div>
        <div id="output">
            <h2>Projected Temperature (&deg;C)</h2>
            <div></div>
        </div>
        <div id="map"></div>
    </section>
    <footer></footer>
</div>
<footer></footer>
</section>
<!--<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>-->
<script src="../static/js/indexof.js"></script>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://d3js.org/topojson.v0.min.js"></script>
<script src="http://d3js.org/d3.geo.projection.v0.min.js"></script>
<script>
    Options = window.Options || {};
    Options.active_map_region = [];
    Options.active_map_colors = [];
    Options.active_rcp = 'RCP26';
</script>
<script src="../static/js/newoutput.js"></script>
<script src="../static/js/input.js"></script>
<script src="../static/js/emulator_output.js"></script>
<script src="../static/js/emulator_input.js"></script>
<script src="../static/js/emulator_map.js"></script>
<script src="../static/js/emulator_interact.js"></script>

</body>
</html>
