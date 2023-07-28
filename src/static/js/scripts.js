```javascript
// Embedding the pitch deck
function embed_deck() {
    const deckFrame = document.getElementById('interactive-deck');
    deckFrame.src = "https://elysium-pitch.pages.dev";
}

// Function for AI interaction
function interact_with_ai() {
    const aiDemo = document.getElementById('ai-character-demo');
    // Code for AI interaction goes here
}

// Function to mint NFT
function mint_nft() {
    const nftShowcase = document.getElementById('nft-wallet-showcase');
    // Code for NFT minting goes here
}

// Function to personalize AI
function personalize_ai() {
    const aiExperience = document.getElementById('personalized-ai-experience');
    // Code for AI personalization goes here
}

// Function for live minting
function live_mint() {
    const liveMinting = document.getElementById('live-minting');
    // Code for live minting goes here
}

// Function to visualize data
function visualize_data() {
    const dataVisualization = document.getElementById('data-visualization');
    // Code for data visualization goes here
}

// Event listeners for each feature
document.addEventListener('DOMContentLoaded', (event) => {
    embed_deck();
    interact_with_ai();
    mint_nft();
    personalize_ai();
    live_mint();
    visualize_data();
});
```