from win10toast import ToastNotifier
import random

quotes = ['Thousands have lived without love, not one without water. – W.H.Auden',
'No Water. No Life. No Blue. No Green. – Sylvia Earle',
'Water is Life. Don’t Waste It.',
'Keep Calm & Drink Water.',
'Water is The Driving Force of all Nature.',
'Water is Your Best Friend for Life.',
'Pure Water is the World’s First and Foremost Medicine. – Slovakian Proverb',
'Make Water Your Primary Drink instead of Soda, Juice. Choose Pure Water throughout your day.',
'Water the Natural Remedy. Drink Your Way to Better Health.',
'Water is Life and Clean Water is Means Health. – Audrey Hepburn',
'Water is the driving force of all nature. – Leonardo da Vinci',
'Drink Pure Water. Stay Healthy.',
'Improve Your Water. Improve Your Life.',
'Drink More Water. Pure Water.',
'Water used to be fresh, pure and drinkable, now the water has lots of focal matter and bacteria. – Claudine Sierra',
'There is no small pleasure in pure water. – Ovid',
'When the well is dry, we’ll know the worth of water. – Benjamin Franklin']


i = random.randint(0, (len(quotes)-1))
toaster = ToastNotifier()
toaster.show_toast('Time to Drink',quotes[i],duration=10)
