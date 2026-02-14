import random
import time
import sys
from colorama import Fore, Style, init


# Initialize colorama
init(autoreset=True)


class Card:
    """Represents a single playing card"""

    SUITS = ["H", "D", "S", "C"]
    SUIT_NAMES = {"H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"}
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Red suits vs black suits
    RED_SUITS = ["H", "D"]
    BLACK_SUITS = ["S", "C"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")

        self.rank = rank
        self.suit = suit

    def __str__(self):
        """String representation with color"""
        card_str = f"{self.rank}{self.suit}"

        if self.suit in self.RED_SUITS:
            return f"{Fore.RED}{card_str}{Style.RESET_ALL}"
        else:
            return f"{Fore.BLUE}{card_str}{Style.RESET_ALL}"

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def get_plain_string(self):
        """Get card string without color"""
        return f"{self.rank}{self.suit}"


class Deck:
    """Represents a deck of playing cards"""

    def __init__(self):
        self.cards = []

    def create_standard_deck(self):
        """Creates a standard 52-card deck"""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))
        return len(self.cards)

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)

    def print_deck(self):
        """Prints all cards in the deck"""
        if not self.cards:
            print("Deck is empty!")
            return

        print(f"\nDeck ({len(self.cards)} cards):")
        for i, card in enumerate(self.cards, 1):
            print(card, end="  ")
            if i % 13 == 0:
                print()  # New line after each suit
        print()

    def take_cards(self, num_cards, random_draw=False, shuffle_after=False):
        """
        Takes cards from the deck

        Args:
            num_cards: Number of cards to take
            random_draw: If True, draws randomly; if False, draws from top
            shuffle_after: If True, shuffles deck after drawing

        Returns:
            List of Card objects
        """
        if num_cards > len(self.cards):
            print(
                f"Cannot draw {num_cards} cards. Only {len(self.cards)} cards in deck."
            )
            return []

        drawn_cards = []

        if random_draw:
            for _ in range(num_cards):
                index = random.randint(0, len(self.cards) - 1)
                drawn_cards.append(self.cards.pop(index))
        else:
            for _ in range(num_cards):
                drawn_cards.append(self.cards.pop(0))

        if shuffle_after:
            self.shuffle()

        return drawn_cards

    def put_cards(self, cards_to_add, shuffle_after=False):
        """
        Puts cards into the deck

        Args:
            cards_to_add: List of Card objects to add
            shuffle_after: If True, shuffles deck after adding
        """
        self.cards.extend(cards_to_add)

        if shuffle_after:
            self.shuffle()

        return len(cards_to_add)

    def clear(self):
        """Clear all cards from deck"""
        self.cards = []

    def size(self):
        """Returns the number of cards in deck"""
        return len(self.cards)


class Hand:
    """Represents a player's hand"""

    def __init__(self, owner_name="Player"):
        self.cards = []
        self.owner_name = owner_name

    def add_cards(self, cards):
        """Add cards to hand"""
        self.cards.extend(cards)

    def remove_cards(self, num_cards):
        """Remove and return cards from hand"""
        if num_cards > len(self.cards):
            print(f"Cannot remove {num_cards} cards. Only {len(self.cards)} in hand.")
            return []

        removed = []
        for _ in range(num_cards):
            removed.append(self.cards.pop(0))
        return removed

    def clear(self):
        """Clear all cards from hand"""
        self.cards = []

    def print_hand(self):
        """Print all cards in hand"""
        if not self.cards:
            print(f"\n{self.owner_name}'s hand is empty!")
            return

        print(f"\n{self.owner_name}'s hand ({len(self.cards)} cards):")
        for card in self.cards:
            print(card, end="  ")
        print()

    def size(self):
        """Returns number of cards in hand"""
        return len(self.cards)


class CommunityCards:
    """Represents community cards visible to all players"""

    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        """Add cards to community"""
        self.cards.extend(cards)

    def clear_cards(self):
        """Clear all community cards"""
        cleared = len(self.cards)
        self.cards = []
        return cleared

    def print_cards(self):
        """Print all community cards"""
        if not self.cards:
            print("\nNo community cards on the table!")
            return

        print(f"\n{'='*50}")
        print(f"COMMUNITY CARDS ({len(self.cards)} cards):")
        print(f"{'='*50}")
        for card in self.cards:
            print(card, end="  ")
        print()
        print(f"{'='*50}")

    def size(self):
        """Returns number of community cards"""
        return len(self.cards)


class Encryptor:
    """Handles encryption and decryption of cards for opponent"""

    def __init__(self):
        self.key = random.randint(100000, 999999)

    def encrypt_cards(self, cards):
        """
        Encrypts a list of cards using simple cipher

        Returns: tuple of (encrypted_string, decryption_key)
        """
        plain_cards = [card.get_plain_string() for card in cards]
        encrypted = []

        for card_str in plain_cards:
            encrypted_card = ""
            for char in card_str:
                # Simple Caesar cipher with the key
                encrypted_card += chr(ord(char) + (self.key % 26))
            encrypted.append(encrypted_card)

        encrypted_message = ",".join(encrypted)
        return encrypted_message, self.key

    def create_decryption_message(encrypted_string, key):
        message = f"""

OPPONENT CARD DECRYPTION INSTRUCTIONS

Your encrypted cards are: {encrypted_string}

Decryption key: {key}

To decrypt your cards:
1. Split the encrypted string by commas
2. For each encrypted card, subtract the key from the ASCII value of each character
3. The result will be your cards in format: RANKS (Rank + Suit)
--------> key to subtract: {key % 26}
====================================================================================
"""
        return message


class Game:
    """Main game controller"""

    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand("Player")
        self.opponent_hand = Hand("Opponent")
        self.community_cards = CommunityCards()
        self.encryptor = Encryptor()

        # Create deck on initialization
        self.deck.create_standard_deck()

    def get_input(self, prompt):
        """Get input with cancel option"""
        print(
            f"{Fore.YELLOW}(Type 'x' or 'X' to cancel and return to menu){Style.RESET_ALL}"
        )
        user_input = input(prompt).strip()
        if user_input.lower() == "x":
            print(
                f"{Fore.CYAN}✗ Operation cancelled. Returning to menu...{Style.RESET_ALL}"
            )
            time.sleep(1)
            return None
        return user_input

    def display_menu(self):
        """Display game menu"""
        print("\n" + "=" * 50)
        print("CARD DECK GAME MENU")
        print("=" * 50)
        print("1.  Create new deck (52 cards)")
        print("2.  Shuffle deck")
        print("3.  Print deck")
        print("4.  Draw cards to my hand")
        print("5.  Put cards from my hand back to deck")
        print("6.  Print my hand")
        print("7.  Draw cards for opponent (encrypted)")
        print("8.  Print opponent hand (visible)")
        print("9.  Draw community cards")
        print("10. Print community cards")
        print("11. Clear community cards")
        print("12. Check deck size")
        print("13. Check my hand size")
        print("14. Check community cards size")
        print("15. RESET GAME")
        print("0.  Exit")
        print("=" * 50)

    def create_deck(self):
        """Create a new standard deck"""
        count = self.deck.create_standard_deck()
        print(f"\n✓ Created new deck with {count} cards!")
        time.sleep(1.5)

    def shuffle_deck(self):
        """Shuffle the deck"""
        if self.deck.size() == 0:
            print("\n✗ Deck is empty! Create a deck first.")
            time.sleep(1.5)
            return
        self.deck.shuffle()
        print("\n✓ Deck shuffled!")
        time.sleep(1.5)

    def print_deck(self):
        """Print the deck"""
        self.deck.print_deck()
        time.sleep(2)

    def draw_cards(self):
        """Draw cards to player hand"""
        if self.deck.size() == 0:
            print("\n✗ Deck is empty!")
            time.sleep(1.5)
            return

        try:
            num_input = self.get_input(
                f"How many cards to draw? (Deck has {self.deck.size()}): "
            )
            if num_input is None:
                return
            num = int(num_input)

            random_input = self.get_input("Draw randomly? (y/n): ")
            if random_input is None:
                return
            random_draw = random_input.lower() == "y"

            shuffle_input = self.get_input("Shuffle deck after drawing? (y/n): ")
            if shuffle_input is None:
                return
            shuffle_after = shuffle_input.lower() == "y"

            cards = self.deck.take_cards(num, random_draw, shuffle_after)
            if cards:
                self.player_hand.add_cards(cards)
                print(f"\n✓ Drew {len(cards)} cards to your hand!")
                print("Cards drawn:")
                for card in cards:
                    print(card, end="  ")
                print()
                time.sleep(2)

        except ValueError:
            print("\n✗ Invalid input!")
            time.sleep(1.5)

    def put_cards_back(self):
        """Put cards from player hand back to deck"""
        if self.player_hand.size() == 0:
            print("\n✗ Your hand is empty!")
            time.sleep(1.5)
            return

        try:
            num_input = self.get_input(
                f"How many cards to put back? (Hand has {self.player_hand.size()}): "
            )
            if num_input is None:
                return
            num = int(num_input)

            shuffle_input = self.get_input("Shuffle deck after adding cards? (y/n): ")
            if shuffle_input is None:
                return
            shuffle_after = shuffle_input.lower() == "y"

            cards = self.player_hand.remove_cards(num)
            if cards:
                self.deck.put_cards(cards, shuffle_after)
                print(f"\n✓ Put {len(cards)} cards back into deck!")
                time.sleep(1.5)

        except ValueError:
            print("\n✗ Invalid input!")
            time.sleep(1.5)

    def print_player_hand(self):
        """Print player's hand"""
        self.player_hand.print_hand()
        time.sleep(2)

    def draw_opponent_cards(self):
        """Draw cards for opponent with encryption"""
        if self.deck.size() == 0:
            print("\n✗ Deck is empty!")
            time.sleep(1.5)
            return

        try:
            num_input = self.get_input(
                f"How many cards for opponent? (Deck has {self.deck.size()}): "
            )
            if num_input is None:
                return
            num = int(num_input)

            random_input = self.get_input("Draw randomly? (y/n): ")
            if random_input is None:
                return
            random_draw = random_input.lower() == "y"

            shuffle_input = self.get_input("Shuffle deck after drawing? (y/n): ")
            if shuffle_input is None:
                return
            shuffle_after = shuffle_input.lower() == "y"

            cards = self.deck.take_cards(num, random_draw, shuffle_after)
            if cards:
                self.opponent_hand.add_cards(cards)
                encrypted, key = self.encryptor.encrypt_cards(cards)
                message = self.encryptor.create_decryption_message(encrypted, key)

                print(f"\n✓ Drew {len(cards)} cards for opponent!")
                print("\nCOPY THIS MESSAGE TO SEND TO OPPONENT AI:")
                print(message)
                time.sleep(3)

        except ValueError:
            print("\n✗ Invalid input!")
            time.sleep(1.5)

    def print_opponent_hand(self):
        """Print opponent's hand (visible - for testing)"""
        self.opponent_hand.print_hand()
        time.sleep(2)

    def draw_community_cards(self):
        """Draw cards to community (visible to all)"""
        if self.deck.size() == 0:
            print("\n✗ Deck is empty!")
            time.sleep(1.5)
            return

        try:
            num_input = self.get_input(
                f"How many community cards to draw? (Deck has {self.deck.size()}): "
            )
            if num_input is None:
                return
            num = int(num_input)

            random_input = self.get_input("Draw randomly? (y/n): ")
            if random_input is None:
                return
            random_draw = random_input.lower() == "y"

            shuffle_input = self.get_input("Shuffle deck after drawing? (y/n): ")
            if shuffle_input is None:
                return
            shuffle_after = shuffle_input.lower() == "y"

            cards = self.deck.take_cards(num, random_draw, shuffle_after)
            if cards:
                self.community_cards.add_cards(cards)
                print(f"\n✓ Drew {len(cards)} community cards!")
                print("\nCommunity cards drawn:")
                for card in cards:
                    print(card, end="  ")
                print()
                time.sleep(2)

        except ValueError:
            print("\n✗ Invalid input!")
            time.sleep(1.5)

    def print_community_cards(self):
        """Print all community cards"""
        self.community_cards.print_cards()
        time.sleep(2)

    def clear_community_cards(self):
        """Clear all community cards"""
        cleared = self.community_cards.clear_cards()
        print(f"\n✓ Cleared {cleared} community cards!")
        time.sleep(1.5)

    def reset_game(self):
        """Reset entire game - clear all hands, community cards, and create fresh deck"""
        print(f"\n{Fore.RED}{'='*50}")
        print("RESETTING GAME...")
        print(f"{'='*50}{Style.RESET_ALL}")

        # Clear all hands and community cards
        player_cards = self.player_hand.size()
        opponent_cards = self.opponent_hand.size()
        community_cards = self.community_cards.size()

        self.player_hand.clear()
        self.opponent_hand.clear()
        self.community_cards.clear_cards()

        # Clear and recreate deck
        self.deck.clear()
        deck_count = self.deck.create_standard_deck()

        # Create new encryptor with new key
        self.encryptor = Encryptor()

        print(f"\n{Fore.GREEN}✓ Game reset complete!")
        print(f"  - Cleared {player_cards} cards from player hand")
        print(f"  - Cleared {opponent_cards} cards from opponent hand")
        print(f"  - Cleared {community_cards} community cards")
        print(f"  - Created fresh unshuffled deck with {deck_count} cards")
        print(f"  - Generated new encryption key{Style.RESET_ALL}")

        time.sleep(2.5)

    def check_deck_size(self):
        """Check deck size"""
        print(f"\nDeck has {self.deck.size()} cards")
        time.sleep(1.5)

    def check_hand_size(self):
        """Check player hand size"""
        print(f"\nYour hand has {self.player_hand.size()} cards")
        time.sleep(1.5)

    def check_community_size(self):
        """Check community cards size"""
        print(f"\nCommunity has {self.community_cards.size()} cards")
        time.sleep(1.5)

    def run(self):
        """Main game loop"""
        print("\n" + "=" * 50)
        print("WELCOME TO THE CARD DECK GAME!")
        print("=" * 50)
        print(
            f"{Fore.GREEN}✓ A standard 52-card deck has been created!{Style.RESET_ALL}"
        )
        time.sleep(1.5)

        while True:
            self.display_menu()

            try:
                choice = input("\nEnter your choice: ").strip()

                if choice == "1":
                    self.create_deck()
                elif choice == "2":
                    self.shuffle_deck()
                elif choice == "3":
                    self.print_deck()
                elif choice == "4":
                    self.draw_cards()
                elif choice == "5":
                    self.put_cards_back()
                elif choice == "6":
                    self.print_player_hand()
                elif choice == "7":
                    self.draw_opponent_cards()
                elif choice == "8":
                    self.print_opponent_hand()
                elif choice == "9":
                    self.draw_community_cards()
                elif choice == "10":
                    self.print_community_cards()
                elif choice == "11":
                    self.clear_community_cards()
                elif choice == "12":
                    self.check_deck_size()
                elif choice == "13":
                    self.check_hand_size()
                elif choice == "14":
                    self.check_community_size()
                elif choice == "15":
                    self.reset_game()
                elif choice == "0":
                    print("\n" + "=" * 50)
                    print("Thanks for playing! Goodbye!")
                    print("=" * 50)
                    time.sleep(1)
                    break
                else:
                    print("\n✗ Invalid choice! Please try again.")
                    time.sleep(1.5)

            except KeyboardInterrupt:
                print("\n\nExiting game...")
                time.sleep(1)
                break
            except Exception as e:
                print(f"\n✗ Error: {e}")
                time.sleep(1.5)


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
