d3.csv("data.csv", function (data) {
    let width = 500;
    let height = 600;


    let colorScale = d3.scale.linear()
                    .domain([0,80])
                    .range(["blue","orange"])

    let widthScale = d3.scale.linear()
                    .domain([-1, 81])
                    .range([0,height-10]); // width of the longest bar in this case

    let axis = d3.svg.axis()
                .ticks(5) // # of ticks
                .scale(widthScale);

    let canvas = d3.select("body").append("svg") // select what element to append the SVG
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform","translate(240,10) rotate(90)")


    canvas.selectAll("rect")
        .data(data)
        .enter()
            .append("rect")
            .attr("width",  d => d.age * 10) // Shorthand for "width", function (d) { return d * 10;})
            .attr("height", 48)
            .attr("y", (d,i) => i * 60)
            .attr("fill", d => colorScale(d.age))
    
    canvas.selectAll("text")
        .data(data)
        .enter()
            .append("text")
            .attr("fill", "white")
            .attr("y", (d,i) => i * 60 + 26)
            .text(d => d.name)

    canvas.append("g")
        .attr("transform","translate(0,200)")
        .call(axis);
    
})
