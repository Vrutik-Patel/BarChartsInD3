
// TODO Math for scaling with viewport height and width 
// Also, condense chart and figure out how the zoom function works
d3.csv("./data/TRUE_Dataset2.csv", function (data) {
    let width = 1000;
    let height = 5100;
    let colorScale = d3.scale.linear()
                    .domain([0,30])//.domain([0,80])
                    .range(["cyan","orange"])

    let widthScale = d3.scale.linear()
                    .domain([-1,30])//.domain([-1, 81])
                    .range([0,width-520]); // width of the longest bar in this case

    let axis = d3.svg.axis()
                .ticks(10) // # of ticks
                .scale(widthScale);

    let canvas = d3.select("body").append("svg") // select what element to append the SVG
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform","translate(240,10)")// rotate(90)")

    canvas.selectAll("rect")
        .data(data)
        .enter()
            .append("rect")
            .attr("width",  d => d.Frequency * 15.3) // Shorthand for "width", function (d) { return d * 10;})
            .attr("height", 20)
            .attr("y", (d,i) => i * 30)
            .attr("fill", d => colorScale(d.Frequency))

    canvas.selectAll("text")
        .data(data)
        .enter()
            .append("text")
            .attr("fill", "#000")
            .attr("y", (d,i) => i * 30 + 13)
            .attr("x", -110)
            .text(d => d.URLs)

    canvas.append("g")
        .attr("transform","translate(0,220)")
        .call(axis);

})
