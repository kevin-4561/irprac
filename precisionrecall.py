TP = 60
FP = 30
FN = 20

precision = TP / (TP + FP)
recall = TP / (TP + FN)
f_measure = 2 * (precision * recall) / (precision + recall)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F-measure (F1 Score): {f_measure:.4f}")
