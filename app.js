// App.js
//source from github: https://github.com/osu-cs340-ecampus/nodejs-starter-app/tree/main/Step%200%20-%20Setting%20Up%20Node.js
/*
    SETUP
*/
// app.js
var express = require('express');
var app = express();
app.use(express.json())
app.use(express.urlencoded({extended: true}))
const PORT = 1234;
var db = require('./database/databaseconnect'); //database required check
const { engine } = require('express-handlebars');
var exphbs = require('express-handlebars');
const { query } = require('express');
app.engine('.hbs', engine({extname: ".hbs"}));

app.set('view engine', '.hbs');              
//static file call
app.use(express.static('public'));
/*
    ROUTES
*/


// render webpages
app.get(['/', '/index', '/workouts', '/exercise', '/category', '/equipment', "/Exercises_have_Equipment", '/Exercises_have_Categories'], function(req, res) {
  let route = req.path.substring(1);

  // manipulate route string
  const capitalizeFirstLetter = str => `${str.charAt(0).toUpperCase()}${str.slice(1)}`;
  table = capitalizeFirstLetter(route);

  // get data from table
  let query1 = `SELECT * FROM ${table}`;    

  db.pool.query(query1, function(error, rows, fields) {
    
    let data = rows;

    db.pool.query(query1, (error, rows, fields) => {
        
      let data2 = rows
      return res.render(route, {data: data, data2: data})
    })
  })
});



app.post(['/add-entity-form', '/delete-entity', '/edit-entity-form'], function(req, res){


    // store operation in a variable
    let operation = req.path

    // store entity name in a variable sliced from URL string
    const entity = req.headers.referer.slice(req.headers.referer.lastIndexOf('/') + 1)  
    
    let data = req.body;
      
    // equipment_id is first 3 letters of equipment_name
    let entity_name = data['input-entity-name'];
    let entity_id = entity_name ? entity_name.substring(0, 3): '';

    // let entity_name = data['input-entity-name'];
    
    // capitalize first letter of entity for SQL query
    let table = entity.charAt(0).toUpperCase() + entity.slice(1)

    // store Create, Delete, Update queries
    let create_query = `INSERT INTO ${table}(${entity}_id, ${entity}_name) VALUES('${entity_id}', '${entity_name}')`;

    let delete_query = `DELETE FROM ${table} WHERE ${entity}_id LIKE ?`;

    let update_query = `UPDATE ${table} SET ${entity}_name = ?, ${entity}_id = ? WHERE ${entity}_id LIKE ?`;

    // check what form is being received to execute correct query
    // Create operation
    if (operation === '/add-entity-form'){ 
      db.pool.query(create_query, function(error, rows, fields){
      
        // if error print what went wrong
        if (error){
          console.log(error)
          res.sendStatus(500);
        }
        // if no error then reload webpage to show data that was added
        else
        {
        res.redirect(`/${entity}`)
        }
      })
    }

    // Delete operation
    else if (operation === '/delete-entity'){
      
      let entity_id = data.entity_id
      
      db.pool.query(delete_query, [entity_id], function(error, rows, fields) {
        if (error) {
          console.log(error);
          return res.sendStatus(500);
        }
    
        return res.redirect(`/${entity}`);
      });
    }

    // Update operation
    else if (operation === '/edit-entity-form'){

      // store updated variables
      entity_id = data['input-entity2'].substring(0, 3); 
      let new_entity_name = data['input-entity-name']; 
      let new_entity_id = new_entity_name.substring(0, 3)

      db.pool.query(update_query, [new_entity_name, new_entity_id, entity_id], function(error, rows, fields) {
        if (error) {
          console.log(error);
          return res.sendStatus(500);
        }
    
        return res.redirect(`/${entity}`);
      });
      
    }});

app.post(['/add-workout-form', '/delete-workout', '/edit-workout-form'], function(req, res){

  let operation = req.path

  let data = req.body

  let workout_name = data.workout_name
  let calorie_count = data['input-calorie-count']

  let create_query = `INSERT INTO Workouts(workout_name, calorie_count) VALUES('${workout_name}', ${calorie_count})`

  let delete_query = `DELETE FROM Workouts WHERE workout_name LIKE '${workout_name}'`

  let update_query = `UPDATE Workouts SET workout_name = ?, calorie_count = ? WHERE workout_id = ?`;

  if (operation === '/add-workout-form'){ 
    db.pool.query(create_query, function(error, rows, fields){
      
      // if error print what went wrong
      if (error){
        console.log(error)
        res.sendStatus(500);
      }
      // if no error then reload webpage to show data that was added
      else
      {
      res.redirect(`/workouts`)
      }
    })
  }

  else if (operation === '/delete-workout'){
      
    db.pool.query(delete_query, [workout_name], function(error, rows, fields) {

      if (error) {
        console.log(error);
        return res.sendStatus(500);
      }
      return res.redirect(`/workouts`);
    });
  }

  else if (operation === '/edit-workout-form'){

    let workout_id = data['input-entity2']; 
    let new_workout_name = data['input-workout-name']; 
    let new_calorie_count = data['input-calorie-count']
    db.pool.query(update_query,[new_workout_name, new_calorie_count, workout_id], function(error, rows, fields) 
      {
      // if error print what went wrong
        if (error) {
          console.log(error);
          res.sendStatus(500);
        }
        // if no error then reload webpage to show data that was added
        else {
          return res.redirect(`/workouts`);
        }})
      }})   


// listen on port 
app.listen(PORT, function(){
    console.log('Express started on http://localhost:' + PORT + '; press Ctrl-C to terminate.')
});
