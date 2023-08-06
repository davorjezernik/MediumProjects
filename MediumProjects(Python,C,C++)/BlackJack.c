#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandomCard() {
    return rand() % 13 + 1;
}

int getCardValue(int card) {
    if (card == 1) {
        return 11; // Ace
    } else if (card >= 11 && card <= 13) {
        return 10; // Face cards (King, Queen, Jack)
    } else {
        return card;
    }
}

int main() {
    int playerScore = 0;
    int dealerScore = 0;
    char choice;

    srand(time(NULL));

    printf("Welcome to Blackjack!\n");

    // Initial deal
    playerScore += getCardValue(getRandomCard());
    playerScore += getCardValue(getRandomCard());
    printf("Your cards: %d\n", playerScore);

    dealerScore += getCardValue(getRandomCard());
    printf("Dealer's face-up card: %d\n", dealerScore);

    // Player's turn
    while (1) {
        printf("Do you want to hit (h) or stand (s)? ");
        scanf(" %c", &choice);

        if (choice == 'h') {
            int card = getRandomCard();
            playerScore += getCardValue(card);
            printf("Your card: %d\n", card);

            if (playerScore > 21) {
                printf("Bust! You lose.\n");
                return 0;
            } else if (playerScore == 21) {
                printf("Blackjack! You win.\n");
                return 0;
            }
        } else if (choice == 's') {
            break;
        } else {
            printf("Invalid choice. Please enter 'h' or 's'.\n");
        }
    }

    // Dealer's turn
    while (dealerScore < 17) {
        int card = getRandomCard();
        dealerScore += getCardValue(card);
    }

    printf("Dealer's score: %d\n", dealerScore);

    // Determine the winner
    if (dealerScore > 21) {
        printf("Dealer busts! You win.\n");
    } else if (dealerScore == playerScore) {
        printf("It's a tie.\n");
    } else if (dealerScore > playerScore) {
        printf("Dealer wins.\n");
    } else {
        printf("You win!\n");
    }

    return 0;
}
