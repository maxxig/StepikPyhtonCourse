text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for t in text:
    if t in result:
        result[t] += 1
    else:
        result[t] = 1
