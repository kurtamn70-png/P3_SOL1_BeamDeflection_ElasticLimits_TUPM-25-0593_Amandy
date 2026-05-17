import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import os

class WingSparAnalysisPipeline:
    """
    Engineering Data Systems Pipeline for SOL-01: Beam Deflection.
    Pillar 3: Solid Mechanics & Stress Analysis.
    """
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.cleaned_df = None
        self.stats = {}

    def ingest_data(self):
        """Module 1: Data Ingestion with robust error handling [cite: 48, 49]"""
        try:
            print(f"Ingesting data from: {self.data_path}")
            self.df = pd.read_csv(self.data_path)
            print("Data Ingestion Successful.")
        except FileNotFoundError:
            print("Error: The dataset file was not found. Please check the path.")
        except Exception as e:
            print(f"An unexpected error occurred during ingestion: {e}")

    def clean_data(self):
        """Module 2: Automated Data Cleaning & Unique Filter [cite: 43, 52-55]"""
        if self.df is None: return
        
        try:
            # 1. Remove Duplicates [cite: 54]
            self.df.drop_duplicates(inplace=True)
            
            # 2. Handle Missing Values [cite: 53]
            self.df.ffill(inplace=True)
            
            # 3. Correct Corrupted Data Types [cite: 55]
            self.df['load_factor_g'] = pd.to_numeric(self.df['load_factor_g'], errors='coerce')
            self.df['deflection_noisy'] = pd.to_numeric(self.df['deflection_noisy'], errors='coerce')
            
            # 4. Mandatory Unique Filter Logic [cite: 43]
            # Analysis restricted to node_id 19 (Tip of the Wing Spar)
            self.cleaned_df = self.df[self.df['node_id'] == 19].copy()
            
            print(f"Cleaning Complete. Unique slice: Node 19 ({len(self.cleaned_df)} records).")
        except Exception as e:
            print(f"Error during cleaning: {e}")

    def perform_engineering_analysis(self):
        """Module 3: NumPy-based Statistical Analysis [cite: 50, 58]"""
        if self.cleaned_df is None: return
        
        data = self.cleaned_df['deflection_noisy'].values
        
        # Mandatory NumPy Calculations [cite: 50]
        self.stats['mean'] = np.mean(data)
        self.stats['median'] = np.median(data)
        self.stats['std_dev'] = np.std(data)
        self.stats['variance'] = np.var(data)
        
        # Correlation between Load and Deflection [cite: 59]
        self.stats['correlation'] = self.cleaned_df['load_factor_g'].corr(self.cleaned_df['deflection_noisy'])
        
        print("\n--- Engineering Statistics ---")
        for k, v in self.stats.items():
            print(f"{k.capitalize()}: {v:.4f}")

    def create_static_visualizations(self):
        """Module 4: Static Engineering Plots (3 Minimum) [cite: 64]"""
        if self.cleaned_df is None: return
        
        # 1. Scatter Plot: Load vs Deflection
        plt.figure(figsize=(10, 6))
        plt.scatter(self.cleaned_df['load_factor_g'], self.cleaned_df['deflection_noisy'], alpha=0.5)
        plt.title('Beam Deflection vs. Applied Load Factor')
        plt.xlabel('Load Factor (G)')
        plt.ylabel('Deflection (mm)')
        plt.grid(True)
        plt.savefig('outputs/static_load_deflection.png')
        
        # 2. Histogram: Distribution of Deflection Values [cite: 58]
        plt.figure(figsize=(10, 6))
        plt.hist(self.cleaned_df['deflection_noisy'], bins=30, color='skyblue', edgecolor='black')
        plt.title('Frequency Distribution of Wing Spar Deflection')
        plt.savefig('outputs/static_distribution.png')
        
        # 3. Boxplot: Load Stability
        plt.figure(figsize=(10, 6))
        plt.boxplot(self.cleaned_df['load_factor_g'])
        plt.title('Load Factor Variance and Outliers')
        plt.savefig('outputs/static_boxplot.png')

    def create_animations(self):
        """Module 5: Exporting Interactive HTML and Auto-playing GIF"""
        import imageio
        if self.df is None: return
        
        # --- PART A: Generate Interactive HTML ---
        spatial_samples = self.df['sample_id'].unique()[::250]
        spatial_df = self.df[self.df['sample_id'].isin(spatial_samples)].sort_values(by=['sample_id', 'node_id'])
        
        fig = px.line(spatial_df, x="x_position", y="deflection_noisy", 
                        animation_frame="sample_id",
                        range_x=[0, 3.5], range_y=[-0.15, 0.15],
                        markers=True, title="Real-Time Wing Spar Bending Profile")
        
        fig.write_html("outputs/animation_spatial_bending.html", include_plotlyjs='cdn')

        # --- PART B: Generate the GIF for the /outputs folder ---
        print("Generating GIF frames... please wait.")
        frames = []
        # Use a smaller subset for the GIF to keep file size low
        gif_samples = self.df['sample_id'].unique()[::400] 
        
        for sample in gif_samples:
            frame_df = self.df[self.df['sample_id'] == sample].sort_values(by='node_id')
            # Create a static "snapshot" for each frame
            frame_fig = px.line(frame_df, x="x_position", y="deflection_noisy", 
                                range_x=[0, 3.5], range_y=[-0.15, 0.15],
                                markers=True, title="Bending Dynamics")
            
            # Convert Plotly figure to an image in memory
            img_bytes = frame_fig.to_image(format="png")
            frames.append(imageio.v2.imread(img_bytes))

        # Save the list of images as a GIF in your outputs folder
        imageio.v2.mimsave('outputs/spatial_bending.gif', frames, fps=5, loop=0)
        print("Success: 'outputs/spatial_bending.gif' has been created.")
# Execution Entry Point
if __name__ == "__main__":
    # Ensure output directories exist for GitHub structure [cite: 88]
    os.makedirs('outputs', exist_ok=True)
    
    pipeline = WingSparAnalysisPipeline('data/wing_spar_data.csv')
    pipeline.ingest_data()
    pipeline.clean_data()
    pipeline.perform_engineering_analysis()
    pipeline.create_static_visualizations()
    pipeline.create_animations()