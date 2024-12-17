// let scene, camera, renderer;
// let currentState = '000'; // Starting state
// const stateTransition = [
//   { state: '000', X0: '000', X1: '001' },
//   { state: '001', X0: '010', X1: '011' },
//   { state: '010', X0: '001', X1: '010' },
//   { state: '011', X0: '011', X1: '111' },
//   { state: '100', X0: '100', X1: '101' },
//   { state: '101', X0: '110', X1: '111' },
//   { state: '110', X0: '100', X1: '101' },
//   { state: '111', X0: '111', X1: '000' }
// ];

// const states = ['000', '001', '010', '011', '100', '101', '110', '111']; // All possible states

// // Coordinates for each state circle
// const statePositions = {
//   '000': { x: -3, y: 2 },
//   '001': { x: -2, y: 3 },
//   '010': { x: -1, y: 2 },
//   '011': { x: 0, y: 3 },
//   '100': { x: 3, y: 2 },
//   '101': { x: 2, y: 3 },
//   '110': { x: 1, y: 2 },
//   '111': { x: 0, y: 1 }
// };

// function init() {
//   scene = new THREE.Scene();
//   camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
//   renderer = new THREE.WebGLRenderer();
//   renderer.setSize(window.innerWidth, window.innerHeight);
//   document.getElementById('stateDiagram').appendChild(renderer.domElement);

//   // Add a basic lighting to the scene
//   const light = new THREE.PointLight(0xffffff, 1, 100);
//   light.position.set(10, 10, 10);
//   scene.add(light);

//   // Add state circles for each state
//   createStateCircles();

//   camera.position.z = 5;

//   animate();
// }

// function animate() {
//   requestAnimationFrame(animate);
//   renderer.render(scene, camera);
// }

// function createStateCircles() {
//   states.forEach(state => {
//     const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // Default green color
//     const geometry = new THREE.CircleGeometry(0.5, 32);
//     const circle = new THREE.Mesh(geometry, material);
    
//     circle.position.set(statePositions[state].x, statePositions[state].y, 0);
//     circle.name = state;
    
//     scene.add(circle);
//   });
// }

// function createTransitionArrows() {
//   // Clear previous arrows
//   scene.children.forEach(child => {
//     if (child.type === 'Line') {
//       scene.remove(child);
//     }
//   });

//   states.forEach(state => {
//     const transitionState = stateTransition.find(item => item.state === state);
//     const currentCircle = scene.getObjectByName(state);

//     // Add transition arrows based on X=0 or X=1
//     ['X0', 'X1'].forEach(X => {
//       const nextState = transitionState[X];
//       if (nextState !== state) {
//         const nextCircle = scene.getObjectByName(nextState);
        
//         // Create arrow
//         const arrowMaterial = new THREE.LineBasicMaterial({ color: X === 'X0' ? 0x0000ff : 0xff0000 });
//         const points = [];
//         points.push(currentCircle.position);
//         points.push(nextCircle.position);
//         const geometry = new THREE.BufferGeometry().setFromPoints(points);
//         const arrow = new THREE.Line(geometry, arrowMaterial);
//         scene.add(arrow);
//       }
//     });
//   });
// }

// function updateState() {
//   const X = document.querySelector('input[name="X"]:checked').value; // Get X value (either 0 or 1)

//   // Find the next state based on the current state and X input
//   const nextState = stateTransition.find(item => item.state === currentState);
//   const nextStateForX = X === '0' ? nextState.X0 : nextState.X1;

//   currentState = nextStateForX; // Update the current state

//   // Update the color of the current state circle
//   updateDiagram(nextStateForX);

//   // Update the transitions (arrows)
//   createTransitionArrows();
// }

// function updateDiagram(state) {
//   // Update the color of the circle based on the next state
//   scene.children.forEach(child => {
//     if (child.type === 'Mesh' && child.name === state) {
//       child.material.color.setHex(0x0000ff); // Blue for the active state
//     } else if (child.type === 'Mesh') {
//       child.material.color.setHex(0x00ff00); // Green for inactive states
//     }
//   });
// }

// // Set up event listeners for the X input buttons
// document.getElementById('xInput0').addEventListener('click', updateState);
// document.getElementById('xInput1').addEventListener('click', updateState);

// init();
