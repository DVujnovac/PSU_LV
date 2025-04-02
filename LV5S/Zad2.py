import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import ConfusionMatrixDisplay

# Ucitavanje podataka
df = pd.read_csv('occupancy_processed.csv')

# Definicija značajki i ciljne varijable
feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)


y_pred = knn.predict(X_test_scaled)

print("Matrica zabune:")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Slobodna', 'Zauzeta'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

print("\nTočnost:", accuracy_score(y_test, y_pred))
print("\nPreciznost i odziv po klasama:")
print(classification_report(y_test, y_pred, target_names=class_names))


accuracy_list = []
k_values = range(1, 21)
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred_k = knn.predict(X_test_scaled)
    accuracy_list.append(accuracy_score(y_test, y_pred_k))

plt.figure()
plt.plot(k_values, accuracy_list, marker='o')
plt.xlabel('Broj susjeda (K)')
plt.ylabel('Točnost')
plt.title('Utjecaj broja susjeda na točnost modela')
plt.show()

knn_no_scaling = KNeighborsClassifier(n_neighbors=5)
knn_no_scaling.fit(X_train, y_train)
y_pred_no_scaling = knn_no_scaling.predict(X_test)
print("\nTočnost bez skaliranja:", accuracy_score(y_test, y_pred_no_scaling))
