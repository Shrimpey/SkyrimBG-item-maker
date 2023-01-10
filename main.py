from pgmagick import Image, DrawableRectangle, DrawableText, Geometry, Color, DrawableList, DrawableGravity, GravityType, CompositeOperator as co
import requests
import os.path
from os import path


skill1Name = "Test"
skill1Cost = 1
skill1CostSymbol = "Stamina"
skill1Result = 2
skill1ResultSymbol = "Triangle"
skill1ResultDamage = 5
skill1ResultDamageSymbol1 = "Heavy"
skill1ResultDamageSymbol2 = "Light"
skill1ResultDamageSymbol3 = "Magic"
skill1Boost = "Destr."
skill1BoostType = "Blue"

skill2Name = "Test"
skill2Cost = 1
skill2CostSymbol = "Stamina"
skill2Result = 2
skill2ResultSymbol = "Triangle"
skill2ResultDamage = 5
skill2ResultDamageSymbol1 = "Heavy"
skill2ResultDamageSymbol2 = "Light"
skill2ResultDamageSymbol3 = "Magic"
skill2Boost = "Destr."
skill2BoostType = "Blue"

skill3Name = "Test"
skill3Cost = 1
skill3CostSymbol = "Stamina"
skill3Result = 2
skill3ResultSymbol = "Triangle"
skill3ResultDamage = 5
skill3ResultDamageSymbol1 = "Heavy"
skill3ResultDamageSymbol2 = "Light"
skill3ResultDamageSymbol3 = "Magic"
skill3Boost = "Destr."
skill3BoostType = "Blue"

upgradeCost = 2
enchantmentCost = 1
lootType = "Custom_Scroll"
itemType = "Spell"
itemName = "Ebony\nBattleaxe"
itemPictureURL = "https://images.uesp.net/8/8d/SR-icon-spell-Heal.png"
specialLootNumber = 1001
cost = 25

armorHeavy = 0
armorLight = 1
armorMagic = 1

itemDescription = "Regenerate 1 Mana\nper Combat Turn"

base = Image('.\Item_Blank.png')
base.font(".\Balgruf.ttf")

# Handle item image
tempItemName = itemName.replace('\n', '_')
if not path.exists('./temp/' + str(tempItemName) + '.jpg'):
	itemPictureData = requests.get(itemPictureURL).content
	with open('./temp/' + str(tempItemName) + '.jpg', 'wb') as handler:
		handler.write(itemPictureData)
itemPicture = Image('./temp/' + str(tempItemName) + '.jpg')
itemPicture.resize('240x240')
base.composite(itemPicture, 150, 170, co.OverCompositeOp)

# Add loot type symbol
typeImage = Image('.\Item_TreasureIcon_' + lootType + '.png')
base.composite(typeImage, 0, 0, co.OverCompositeOp)
# Take care of numbered quest items
if lootType == "S":
	base.fontPointsize(55)
	base.annotate(str(specialLootNumber), Geometry(1,1,80,80), GravityType.CenterGravity, -45)


# Add item type symbol
itemTypeImage = Image('.\Item_Type_' + itemType + '.png')
base.composite(itemTypeImage, 0, 0, co.OverCompositeOp)

# Add item name
base.fontPointsize(50)
base.fillColor("White")
base.annotate(itemName, Geometry(1,1,260,90), GravityType.CenterGravity)
base.fillColor("Black")

# Add enchantment/upgrade costs
enchantmentCostImage = Image('.\Item_EnchantmentCost.png')
upgradeCostImage = Image('.\Item_EnchantmentUpgradeCost.png')
if upgradeCost > 0:
	base.composite(upgradeCostImage, 0, 0, co.OverCompositeOp)
	base.fontPointsize(55)
	base.annotate(str(enchantmentCost), Geometry(1,1,420,686), GravityType.CenterGravity)
	base.fontPointsize(55)
	base.annotate(str(upgradeCost), Geometry(1,1,460,715), GravityType.CenterGravity)
elif enchantmentCost > 0:
	base.composite(enchantmentCostImage, 0, 0, co.OverCompositeOp)
	base.fontPointsize(65)
	base.annotate(str(enchantmentCost), Geometry(1,1,432,700), GravityType.CenterGravity)


# Add price symbol
if cost > 0:
	priceImage = Image('.\Item_Price.png')
	base.composite(priceImage, 0, 0, co.OverCompositeOp)

	# Write item price
	base.fontPointsize(85)
	base.annotate(str(cost), Geometry(1,1,80,700), GravityType.CenterGravity)



# Add skills
if skill1Name != "":
	skills = "Single"
	if skill2Name != "":
		skills = "Double"
	if skill3Name != "":
		skills = "Triple"
	skillFrameImage = Image('.\Item_Skill_'+skills+'.png')
	base.composite(skillFrameImage, 0, 0, co.OverCompositeOp)

	# Skill 1 stuff -----------------------------------------------------------------------
	skillYVal = 426
	# Boost bounding box
	im = Image(Geometry(81, 53), Color(skill1BoostType))
	skill1BoostRect = DrawableRectangle(0, 0, 0, 0)
	im.draw(skill1BoostRect)
	base.composite(im, 30, skillYVal - 26, co.OverCompositeOp)
	# Boost text
	base.fontPointsize(25)
	base.annotate(str(skill1Boost), Geometry(1,1,71,skillYVal), GravityType.CenterGravity)
	# Cost symbol
	skill1CostSymbolImage = Image('.\Symbol_'+skill1CostSymbol+'.png')
	skill1CostSymbolImage.resize('40x40')
	base.composite(skill1CostSymbolImage, 165-20, skillYVal-20, co.OverCompositeOp)
	# Cost number
	base.fontPointsize(40)
	base.annotate(str(skill1Cost), Geometry(1,1,132,skillYVal), GravityType.CenterGravity)
	# Name text
	base.fontPointsize(25)
	base.annotate(str(skill1Name), Geometry(1,1,234,skillYVal), GravityType.CenterGravity)
	# Result symbol
	skill1ResultSymbolImage = Image('.\Symbol_'+skill1ResultSymbol+'.png')
	skill1ResultSymbolImage.resize('40x40')
	base.composite(skill1ResultSymbolImage, 324-20, skillYVal-20, co.OverCompositeOp)
	# Result number
	base.fontPointsize(40)
	base.annotate(str(skill1Result), Geometry(1,1,297,skillYVal), GravityType.CenterGravity)
	# Damage symbol 1
	skill1ResultDamageSymbol1Image = Image('.\Symbol_'+skill1ResultDamageSymbol1+'.png')
	skill1ResultDamageSymbol1Image.resize('40x40')
	base.composite(skill1ResultDamageSymbol1Image, 395-20, skillYVal - 20, co.OverCompositeOp)
	# Damage symbol 2
	skill1ResultDamageSymbol2Image = Image('.\Symbol_'+skill1ResultDamageSymbol2+'.png')
	skill1ResultDamageSymbol2Image.resize('40x40')
	base.composite(skill1ResultDamageSymbol2Image, 431-20, skillYVal - 20, co.OverCompositeOp)
	# Damage symbol 3
	skill1ResultDamageSymbol3Image = Image('.\Symbol_'+skill1ResultDamageSymbol3+'.png')
	skill1ResultDamageSymbol3Image.resize('40x40')
	base.composite(skill1ResultDamageSymbol3Image, 468-20, skillYVal - 20, co.OverCompositeOp)
	# Damage number text
	base.fontPointsize(40)
	base.annotate(str(skill1ResultDamage), Geometry(1,1,367,skillYVal), GravityType.CenterGravity)


	# Skill 2 stuff -----------------------------------------------------------------------
	if skill2Name != "":
		skillYVal = 488
		# Boost bounding box
		im = Image(Geometry(81, 53), Color(skill2BoostType))
		skill2BoostRect = DrawableRectangle(0, 0, 0, 0)
		im.draw(skill2BoostRect)
		base.composite(im, 30, skillYVal - 26, co.OverCompositeOp)
		# Boost text
		base.fontPointsize(25)
		base.annotate(str(skill2Boost), Geometry(1,1,71,skillYVal), GravityType.CenterGravity)
		# Cost symbol
		skill2CostSymbolImage = Image('.\Symbol_'+skill2CostSymbol+'.png')
		skill2CostSymbolImage.resize('40x40')
		base.composite(skill2CostSymbolImage, 165-20, skillYVal-20, co.OverCompositeOp)
		# Cost number
		base.fontPointsize(40)
		base.annotate(str(skill2Cost), Geometry(1,1,132,skillYVal), GravityType.CenterGravity)
		# Name text
		base.fontPointsize(25)
		base.annotate(str(skill2Name), Geometry(1,1,234,skillYVal), GravityType.CenterGravity)
		# Result symbol
		skill2ResultSymbolImage = Image('.\Symbol_'+skill2ResultSymbol+'.png')
		skill2ResultSymbolImage.resize('40x40')
		base.composite(skill2ResultSymbolImage, 324-20, skillYVal-20, co.OverCompositeOp)
		# Result number
		base.fontPointsize(40)
		base.annotate(str(skill2Result), Geometry(1,1,297,skillYVal), GravityType.CenterGravity)
		# Damage symbol 1
		skill2ResultDamageSymbol1Image = Image('.\Symbol_'+skill2ResultDamageSymbol1+'.png')
		skill2ResultDamageSymbol1Image.resize('40x40')
		base.composite(skill2ResultDamageSymbol1Image, 395-20, skillYVal - 20, co.OverCompositeOp)
		# Damage symbol 2
		skill2ResultDamageSymbol2Image = Image('.\Symbol_'+skill2ResultDamageSymbol2+'.png')
		skill2ResultDamageSymbol2Image.resize('40x40')
		base.composite(skill2ResultDamageSymbol2Image, 431-20, skillYVal - 20, co.OverCompositeOp)
		# Damage symbol 3
		skill2ResultDamageSymbol3Image = Image('.\Symbol_'+skill2ResultDamageSymbol3+'.png')
		skill2ResultDamageSymbol3Image.resize('40x40')
		base.composite(skill2ResultDamageSymbol3Image, 468-20, skillYVal - 20, co.OverCompositeOp)
		# Damage number text
		base.fontPointsize(40)
		base.annotate(str(skill2ResultDamage), Geometry(1,1,367,skillYVal), GravityType.CenterGravity)



	# Skill 3 stuff -----------------------------------------------------------------------
	if skill3Name != "":
		skillYVal = 550
		# Boost bounding box
		im = Image(Geometry(81, 53), Color(skill3BoostType))
		skill3BoostRect = DrawableRectangle(0, 0, 0, 0)
		im.draw(skill3BoostRect)
		base.composite(im, 30, skillYVal - 26, co.OverCompositeOp)
		# Boost text
		base.fontPointsize(25)
		base.annotate(str(skill3Boost), Geometry(1,1,71,skillYVal), GravityType.CenterGravity)
		# Cost symbol
		skill3CostSymbolImage = Image('.\Symbol_'+skill3CostSymbol+'.png')
		skill3CostSymbolImage.resize('40x40')
		base.composite(skill3CostSymbolImage, 165-20, skillYVal-20, co.OverCompositeOp)
		# Cost number
		base.fontPointsize(40)
		base.annotate(str(skill3Cost), Geometry(1,1,132,skillYVal), GravityType.CenterGravity)
		# Name text
		base.fontPointsize(25)
		base.annotate(str(skill3Name), Geometry(1,1,234,skillYVal), GravityType.CenterGravity)
		# Result symbol
		skill3ResultSymbolImage = Image('.\Symbol_'+skill3ResultSymbol+'.png')
		skill3ResultSymbolImage.resize('40x40')
		base.composite(skill3ResultSymbolImage, 324-20, skillYVal-20, co.OverCompositeOp)
		# Result number
		base.fontPointsize(40)
		base.annotate(str(skill3Result), Geometry(1,1,297,skillYVal), GravityType.CenterGravity)
		# Damage symbol 1
		skill3ResultDamageSymbol1Image = Image('.\Symbol_'+skill3ResultDamageSymbol1+'.png')
		skill3ResultDamageSymbol1Image.resize('40x40')
		base.composite(skill3ResultDamageSymbol1Image, 395-20, skillYVal - 20, co.OverCompositeOp)
		# Damage symbol 2
		skill3ResultDamageSymbol2Image = Image('.\Symbol_'+skill3ResultDamageSymbol2+'.png')
		skill3ResultDamageSymbol2Image.resize('40x40')
		base.composite(skill3ResultDamageSymbol2Image, 431-20, skillYVal - 20, co.OverCompositeOp)
		# Damage symbol 3
		skill3ResultDamageSymbol3Image = Image('.\Symbol_'+skill3ResultDamageSymbol3+'.png')
		skill3ResultDamageSymbol3Image.resize('40x40')
		base.composite(skill2ResultDamageSymbol3Image, 468-20, skillYVal - 20, co.OverCompositeOp)
		# Damage number text
		base.fontPointsize(40)
		base.annotate(str(skill3ResultDamage), Geometry(1,1,367,skillYVal), GravityType.CenterGravity)


# Armor symbols
heavyArmorImage = Image('.\Symbol_Heavy.png')
lightArmorImage = Image('.\Symbol_Light.png')
magicArmorImage = Image('.\Symbol_Magic.png')
heavyArmorImage.resize('50x50')
lightArmorImage.resize('50x50')
magicArmorImage.resize('50x50')
base.fillColor("White")
if armorHeavy > 0:
	base.fontPointsize(45)
	base.annotate(str(armorHeavy), Geometry(1,1,150,700), GravityType.CenterGravity)
	base.composite(heavyArmorImage, 188-25, 700-25, co.OverCompositeOp)
if armorLight > 0:
	base.fontPointsize(45)
	base.annotate(str(armorLight), Geometry(1,1,238,700), GravityType.CenterGravity)
	base.composite(lightArmorImage, 275-25, 700-25, co.OverCompositeOp)
if armorMagic > 0:
	base.fontPointsize(45)
	base.annotate(str(armorMagic), Geometry(1,1,310,700), GravityType.CenterGravity)
	base.composite(magicArmorImage, 349-25, 700-25, co.OverCompositeOp)

# Item description
base.fontPointsize(27)
if skill3Name != "":
	base.annotate(str(itemDescription), Geometry(1,1,250,628), GravityType.CenterGravity)
elif skill2Name != "":
	base.annotate(str(itemDescription), Geometry(1,1,250,593), GravityType.CenterGravity)
else:
	base.annotate(str(itemDescription), Geometry(1,1,250,550), GravityType.CenterGravity)
base.fillColor("Black")

# Write output
base.write('./temp/output.png')
