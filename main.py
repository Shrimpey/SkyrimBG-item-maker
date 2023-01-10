from pgmagick import Image, DrawableRectangle, DrawableText, Geometry, Color, DrawableList, DrawableGravity, GravityType, CompositeOperator as co

skills = "Single+Default"
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

upgradeCost = 0
enchantmentCost = 0
itemType = "Custom_Scroll"
itemTypeNumber = 1001
costSymbol = True
cost = 25

base = Image('.\Item_Blank.png')
base.font(".\Balgruf.ttf")


# Add item type symbol
typeImage = Image('.\Item_TreasureIcon_' + itemType + '.png')
base.composite(typeImage, 0, 0, co.OverCompositeOp)
# Take care of numbered quest items
if itemType == "S":
	base.fontPointsize(55)
	base.annotate(str(itemTypeNumber), Geometry(1,1,80,80), GravityType.CenterGravity, -45)


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
if costSymbol:
	priceImage = Image('.\Item_Price.png')
	base.composite(priceImage, 0, 0, co.OverCompositeOp)

	# Write item price
	base.fontPointsize(85)
	base.annotate(str(cost), Geometry(1,1,80,700), GravityType.CenterGravity)



# Add skills
if skills != "":
	skillFrameImage = Image('.\Item_Skill_'+skills+'.png')
	base.composite(skillFrameImage, 0, 0, co.OverCompositeOp)
	# Skill 1 stuff -----------------------------------------------------------------------
	# Boost bounding box
	im = Image(Geometry(81, 53), Color(skill1BoostType))
	skill1BoostRect = DrawableRectangle(0, 0, 0, 0)
	im.draw(skill1BoostRect)
	base.composite(im, 30, 400, co.OverCompositeOp)
	# Boost text
	base.fontPointsize(25)
	base.annotate(str(skill1Boost), Geometry(1,1,71,426), GravityType.CenterGravity)
	# Cost symbol
	skill1CostSymbolImage = Image('.\Symbol_'+skill1CostSymbol+'.png')
	skill1CostSymbolImage.resize('40x40')
	base.composite(skill1CostSymbolImage, 165-20, 426-20, co.OverCompositeOp)
	# Cost number
	base.fontPointsize(40)
	base.annotate(str(skill1Cost), Geometry(1,1,132,426), GravityType.CenterGravity)
	# Name text
	base.fontPointsize(25)
	base.annotate(str(skill1Name), Geometry(1,1,234,427), GravityType.CenterGravity)
	# Result symbol
	skill1ResultSymbolImage = Image('.\Symbol_'+skill1ResultSymbol+'.png')
	skill1ResultSymbolImage.resize('40x40')
	base.composite(skill1ResultSymbolImage, 324-20, 426-20, co.OverCompositeOp)
	# Result number
	base.fontPointsize(40)
	base.annotate(str(skill1Result), Geometry(1,1,297,426), GravityType.CenterGravity)
	# Damage symbol 1
	skill1ResultDamageSymbol1Image = Image('.\Symbol_'+skill1ResultDamageSymbol1+'.png')
	skill1ResultDamageSymbol1Image.resize('40x40')
	base.composite(skill1ResultDamageSymbol1Image, 395-20, 445-40, co.OverCompositeOp)
	# Damage symbol 2
	skill1ResultDamageSymbol2Image = Image('.\Symbol_'+skill1ResultDamageSymbol2+'.png')
	skill1ResultDamageSymbol2Image.resize('40x40')
	base.composite(skill1ResultDamageSymbol2Image, 431-20, 445-40, co.OverCompositeOp)
	# Damage symbol 3
	skill1ResultDamageSymbol3Image = Image('.\Symbol_'+skill1ResultDamageSymbol3+'.png')
	skill1ResultDamageSymbol3Image.resize('40x40')
	base.composite(skill1ResultDamageSymbol3Image, 468-20, 445-40, co.OverCompositeOp)
	# Damage number text
	base.fontPointsize(40)
	base.annotate(str(skill1ResultDamage), Geometry(1,1,367,426), GravityType.CenterGravity)



# Write output
base.write('output.png')
