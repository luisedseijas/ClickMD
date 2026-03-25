"""
Punto de entrada de GUI - Ventana principal
============================================

Define la ventana principal de la aplicación PySide6.
"""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QSpinBox, QDoubleSpinBox
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    """
    Ventana principal de la aplicación ClickMD.
    
    Proporciona:
    - Carga de moléculas
    - Selección de potencial
    - Configuración de simulación
    - Visualización de resultados
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ClickMD - Simulación Molecular")
        self.setGeometry(100, 100, 1200, 800)
        
        # Crear widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout()
        
        # Panel izquierdo: Controles
        left_panel = self._create_left_panel()
        main_layout.addLayout(left_panel, 1)
        
        # Panel derecho: Visualización (placeholder)
        right_panel = self._create_right_panel()
        main_layout.addLayout(right_panel, 1)
        
        central_widget.setLayout(main_layout)
        
        self.statusBar().showMessage("Listo")
    
    def _create_left_panel(self):
        """Crea el panel de controles izquierdo."""
        layout = QVBoxLayout()
        
        # Título
        title = QLabel("Configuración de Simulación")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        # Botón de cargar molécula
        load_btn = QPushButton("Cargar Molécula")
        load_btn.clicked.connect(self.load_molecule)
        layout.addWidget(load_btn)
        
        # Selección de potencial
        layout.addWidget(QLabel("Potencial:"))
        self.potential_combo = QComboBox()
        self.potential_combo.addItems(["TorchANI (Red Neuronal)", "GAFF (Clásico)", "Amber (Clásico)"])
        layout.addWidget(self.potential_combo)
        
        # Temperatura
        layout.addWidget(QLabel("Temperatura (K):"))
        self.temp_spin = QDoubleSpinBox()
        self.temp_spin.setRange(0, 10000)
        self.temp_spin.setValue(298.15)
        layout.addWidget(self.temp_spin)
        
        # Duración (pasos)
        layout.addWidget(QLabel("Duración (pasos):"))
        self.time_spin = QSpinBox()
        self.time_spin.setRange(100, 10000000)
        self.time_spin.setValue(100000)
        layout.addWidget(self.time_spin)
        
        # Botón de ejecutar
        self.run_btn = QPushButton("Ejecutar Simulación")
        self.run_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-weight: bold;")
        self.run_btn.clicked.connect(self.run_simulation)
        layout.addWidget(self.run_btn)
        
        layout.addStretch()
        
        return layout
    
    def _create_right_panel(self):
        """Crea el panel de visualización derecho."""
        layout = QVBoxLayout()
        
        title = QLabel("Visualización 3D")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        # Placeholder para visualizador 3D
        placeholder = QLabel("(Visualizador 3D - en desarrollo)")
        placeholder.setMinimumHeight(600)
        placeholder.setStyleSheet("border: 1px solid #ccc; display: flex; align-items: center; justify-content: center; background-color: #f5f5f5;")
        placeholder.setAlignment(Qt.AlignCenter)
        layout.addWidget(placeholder)
        
        return layout
    
    def load_molecule(self):
        """Abre diálogo para cargar una molécula."""
        from PySide6.QtWidgets import QFileDialog
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Cargar Molécula",
            "",
            "Molecular Files (*.pdb *.sdf *.mol2);;All Files (*)"
        )
        
        if file_path:
            self.statusBar().showMessage(f"Molécula cargada: {file_path}")
    
    def run_simulation(self):
        """Ejecuta la simulación con los parámetros actuales."""
        self.statusBar().showMessage("Ejecutando simulación...")
        self.run_btn.setEnabled(False)
        
        # TODO: Implementar lógica de simulación
        print("Simulación iniciada con parámetros:")
        print(f"  Potencial: {self.potential_combo.currentText()}")
        print(f"  Temperatura: {self.temp_spin.value()} K")
        print(f"  Duración: {self.time_spin.value()} pasos")
        
        self.run_btn.setEnabled(True)
        self.statusBar().showMessage("Simulación completada")
