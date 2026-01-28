"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favorite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style:")
print("1.Simple lines ")
print ("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter the style number (1-3): ").strip()

def generate_bio(style):
    if style == '1':
        return f"{emoji} {name} | {profession}\n💡 {passion}\n🔗 {website}"
    elif style == '2':
        return f"{emoji} {name}\n{profession}🔥\n{passion}\n{website}🔥"
    elif style == '3':
        return f"{emoji*3}\n{name} - {profession}\n{passion}\n{website}\n{emoji*3}"

bio = generate_bio(style)    

print("\nYour Stylish Bio:\n")
print("*"*50)
print(textwrap.dedent(bio)) # dedant remove any leading whitespace for better formatting
print("*"*50)

# Enter your name: Yash
# Enter your profession: Student  
# Enter your passion in one line: My passion is singing
# Enter your favorite emoji: 😂
# Enter your website: yash.com

# Choose your style:
# 1.Simple lines
# 2. Vertical flair
# 3. Emoji sandwich
# Enter the style number (1-3): 3

# Your Stylish Bio:

# **************************************************
# 😂😂😂
# Yash - Student
# My passion is singing
# yash.com
# 😂😂😂
# **************************************************

save = input("Do you want to save the bio to a .txt file? (yes/no): ").strip().lower()
if save == 'yes':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(bio)
    print(f"Bio saved to {filename}")

# Enter your name: Yash
# Enter your profession: Student
# Enter your passion in one line: My passion is singing.
# Enter your favorite emoji: 🔥
# Enter your website: yash.com

# Choose your style:
# 1.Simple lines
# 2. Vertical flair
# 3. Emoji sandwich
# Enter the style number (1-3): 3

# Your Stylish Bio:

# **************************************************
# 🔥🔥🔥
# Yash - Student
# My passion is singing.
# yash.com
# 🔥🔥🔥
# **************************************************
# Do you want to save the bio to a .txt file? (yes/no): yes
# Bio saved to yash_bio.txt (file created successfully with the bio content)