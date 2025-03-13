 // Import required modules
const readline = require('readline');

/**
 * Main function to execute the program steps
 */
async function main() {
    // 1. Print initial greeting
    console.log("Hello, World!");

    try {
        // 2. Get user's name with error handling
        const userName = await getNameFromUser();
        
        // 3. Greet the user by name
        greetUser(userName);
        
        // 4. Display current date and time
        showDateTime();
    } catch (error) {
        // Handle any errors that occurred during input
        console.error(`Error: ${error.message}`);
    }
}

/**
 * Asks for user's name and returns a Promise
 * @returns {Promise<string>} User's name
 */
function getNameFromUser() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    return new Promise((resolve, reject) => {
        rl.question('Please enter your name: ', (name) => {
            rl.close();
            // Check for empty input
            if (name.trim() === '') {
                reject(new Error('Name cannot be empty'));
            } else {
                resolve(name.trim());
            }
        });
    });
}

/**
 * Greets the user by name
 * @param {string} name User's name
 */
function greetUser(name) {
    console.log(`\nHello, ${name}! Welcome to our program.`);
}

/**
 * Displays current date and time
 */
function showDateTime() {
    const now = new Date();
    console.log(`Current date and time: ${now.toLocaleString()}`);
}

// Execute the main function
main();