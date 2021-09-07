let dataset1 = []; dataset1.push(["Columbus","43","OH"]); dataset1.push(["Cincinnati","12","OH"]); dataset1.push(["Dayton","43","OH"]);

let dataset2 = []; dataset2.push(["Bark","Dog"]); dataset2.push(["Honk","Car"]); dataset2.push(["Quack","Duck"]);

let result = dataset1.map(dataset1item =>{
return dataset2.filter(dataset2item => dataset2item[1][0] === dataset1item[0][0]).map(filterResultItem => filterResultItem[0]); 
});
console.log(result);