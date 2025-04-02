import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import ConfusionMatrixDisplay


df = pd.read_csv('occupancy_processed.csv')


feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


dt = DecisionTreeClassifier(max_depth=3)
dt.fit(X_train_scaled, y_train)

# Predikcija
y_pred = dt.predict(X_test_scaled)


plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True, feature_names=feature_names, class_names=class_names)
plt.show()

print("Matrica zabune:")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

print("\nTočnost:", accuracy_score(y_test, y_pred))
print("\nPreciznost i odziv po klasama:")
print(classification_report(y_test, y_pred, target_names=class_names))

depth_values = range(1, 21)
accuracy_list = []

for depth in depth_values:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train_scaled, y_train)
    y_pred_depth = dt.predict(X_test_scaled)
    accuracy_list.append(accuracy_score(y_test, y_pred_depth))


plt.figure()
plt.plot(depth_values, accuracy_list, marker='o', linestyle='-', color='b')
plt.xlabel('Dubina stabla odlučivanja')
plt.ylabel('Točnost')
plt.title('Utjecaj dubine stabla odlučivanja na točnost')
plt.grid()
plt.show()


dt_no_scaling = DecisionTreeClassifier(random_state=42)
dt_no_scaling.fit(X_train, y_train)
y_pred_no_scaling = dt_no_scaling.predict(X_test)
print("\nTočnost bez skaliranja:", accuracy_score(y_test, y_pred_no_scaling))
