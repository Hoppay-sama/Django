// Toggle password visibility
function togglePassword() {
    const passwordField = document.getElementById('password');
    const passwordIcon = document.querySelector('.show-password');

    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        passwordIcon.textContent = '🙈';
    } else {
        passwordField.type = 'password';
        passwordIcon.textContent = '👁';
    }
}

// Default profile data
const defaultProfile = {
    username: "John Doe",
    email: "johndoe@example.com",
    password: "password",
    phone: "1234567890",
    gender: "Male"
};

// Load profile data from localStorage or use default values
function loadProfile() {
    const savedProfile = JSON.parse(localStorage.getItem("profile-form")) || defaultProfile;

    document.getElementById('username').value = savedProfile.username;
    document.getElementById('email').value = savedProfile.email;
    document.getElementById('password').value = savedProfile.password;
    document.getElementById('phone').value = savedProfile.phone;
    document.getElementById('gender').value = savedProfile.gender;
}

// Save updated profile data to localStorage
function saveProfile() {
    const updatedProfile = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        phone: document.getElementById('phone').value,
        gender: document.getElementById('gender').value
    };

    localStorage.setItem("profile-form", JSON.stringify(updatedProfile));
    alert("Profile saved successfully!");
}

// Call loadProfile on page load
document.addEventListener("DOMContentLoaded", loadProfile);


// Switch between Profile, My Purchases, and E-Wallet
function showProfile() {
    document.getElementById('profile-section').classList.remove('hidden');
    document.getElementById('my-purchases').classList.add('hidden');
    document.getElementById('e-wallet').classList.add('hidden');
}

function showPurchases() {
    document.getElementById('profile-section').classList.add('hidden');
    document.getElementById('my-purchases').classList.remove('hidden');
    document.getElementById('e-wallet').classList.add('hidden');
}

function showEWallet() {
    document.getElementById('profile-section').classList.add('hidden');
    document.getElementById('my-purchases').classList.add('hidden');
    document.getElementById('e-wallet').classList.remove('hidden');
}

function filterOrders(status) {
    const orderList = document.querySelectorAll('.order-item');
    const tabs = document.querySelectorAll('.status-tab');

    // Highlight active tab
    tabs.forEach(tab => {
        tab.classList.remove('active');
        if (tab.textContent.toLowerCase() === status || (status === 'all' && tab.textContent.toLowerCase() === 'all')) {
            tab.classList.add('active');
        }
    });

    // Show/hide orders based on status
    orderList.forEach(order => {
        if (status === 'all' || order.getAttribute('data-status') === status) {
            order.style.display = 'block';
        } else {
            order.style.display = 'none';
        }
    });
}



// Wallet variables
let walletBalance = 0;
let transactionHistory = [];

// Load wallet data from localStorage
function loadWallet() {
    const savedBalance = localStorage.getItem('wallet-balance');
    const savedTransactions = localStorage.getItem('transaction-history');

    // Load saved balance or set to 0
    walletBalance = savedBalance ? parseFloat(savedBalance) : 0;
    document.getElementById('wallet-balance').textContent = walletBalance.toFixed(2);

    // Load saved transaction history or set to empty
    transactionHistory = savedTransactions ? JSON.parse(savedTransactions) : [];
    const historyList = document.getElementById('transaction-history');
    historyList.innerHTML = ''; // Clear existing history
    transactionHistory.forEach(transaction => {
        const li = document.createElement('li');
        li.textContent = transaction;
        historyList.appendChild(li);
    });
}

// Save wallet data to localStorage
function saveWallet() {
    localStorage.setItem('wallet-balance', walletBalance.toFixed(2));
    localStorage.setItem('transaction-history', JSON.stringify(transactionHistory));
}

// Show Add Funds Section
function showAddFunds() {
    const addFundsSection = document.getElementById('add-funds-section');
    const withdrawSection = document.getElementById('withdraw-funds-section');
    withdrawSection.classList.add('hidden'); // Hide withdraw section if open
    addFundsSection.classList.toggle('hidden'); // Toggle visibility
}

// Add funds to wallet
function addFunds() {
    const amountInput = document.getElementById('fund-amount');
    const amount = parseFloat(amountInput.value);

    if (!isNaN(amount) && amount > 0) {
        walletBalance += amount;
        document.getElementById('wallet-balance').textContent = walletBalance.toFixed(2);

        logTransaction(`Added ₱${amount.toFixed(2)} to wallet.`);
        saveWallet(); // Save updated balance and transaction history
        amountInput.value = '';

        // Hide Add Funds Section after adding funds
        document.getElementById('add-funds-section').classList.add('hidden');
        alert('Funds added successfully.');
    } else {
        alert('Please enter a valid amount.');
    }
}

// Log a transaction
function logTransaction(description) {
    transactionHistory.push(description);
    const historyList = document.getElementById('transaction-history');
    historyList.innerHTML = '';
    transactionHistory.forEach(transaction => {
        const li = document.createElement('li');
        li.textContent = transaction;
        historyList.appendChild(li);
    });
    saveWallet(); // Save the updated transaction history
}

// Pay for an order using the wallet
function payWithWallet(orderId, orderPrice) {
    if (walletBalance >= orderPrice) {
        walletBalance -= orderPrice;
        document.getElementById('wallet-balance').textContent = walletBalance.toFixed(2);

        logTransaction(`Paid ₱${orderPrice.toFixed(2)} for Order ID: ${orderId}.`);
        saveWallet(); // Save updated wallet data

        alert(`Order ${orderId} paid successfully!`);
        document.querySelector(`.order-item[data-id="${orderId}"]`).remove();
    } else {
        alert('Insufficient balance in your wallet.');
    }
}

// Show Withdraw Funds Section
function showWithdrawFunds() {
    const withdrawSection = document.getElementById('withdraw-funds-section');
    const addFundsSection = document.getElementById('add-funds-section');
    addFundsSection.classList.add('hidden'); // Hide add funds if open
    withdrawSection.classList.toggle('hidden'); // Toggle visibility
}

// Withdraw funds from wallet
function withdrawFunds() {
    const walletBalanceEl = document.getElementById('wallet-balance');
    const withdrawInput = document.getElementById('withdraw-amount');

    const withdrawAmount = parseFloat(withdrawInput.value);

    if (isNaN(withdrawAmount) || withdrawAmount <= 0) {
        alert('Please enter a valid amount to withdraw.');
        return;
    }

    if (withdrawAmount > walletBalance) {
        alert('Insufficient balance.');
        return;
    }

    walletBalance -= withdrawAmount;
    document.getElementById('wallet-balance').textContent = walletBalance.toFixed(2);

    logTransaction(`Withdrawn: ₱${withdrawAmount.toFixed(2)}`);
    saveWallet(); // Save updated balance and transaction history

    // Reset input
    withdrawInput.value = '';

    // Hide Withdraw Funds Section after withdrawing funds
    document.getElementById('withdraw-funds-section').classList.add('hidden');
    alert('Withdrawal successful.');
}

// Initialize wallet on page load
document.addEventListener('DOMContentLoaded', loadWallet);
