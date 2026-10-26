"""
Smart Agriculture Monitoring - GUI
----------------------------------
Desktop app (Tkinter) that trains the crop models on startup and lets you:
  * enter temperature, humidity and soil moisture with sliders
  * get predicted crop growth (cm/day) and condition (Healthy/Moderate/Stressed)
  * view a dashboard: trends, correlation heatmap, feature importance
  * browse the cleaned data table
  * load your own CSV (columns: time, field, temperature, humidity,
    soil_moisture, growth_cm_day)

Install:  pip install numpy pandas scikit-learn matplotlib
Run:      python smart_agriculture_gui.py
(Tkinter ships with Python; on Linux: sudo apt install python3-tk)
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score

FEATURES = ["temperature", "humidity", "soil_moisture"]
NUM_COLS = FEATURES + ["growth_cm_day"]
COLORS = ["#2f6f4e", "#c9822b", "#3b6fa0", "#8a5a9e"]
CONDITION_COLOR = {"Healthy": "#2f8f4e", "Moderate": "#c9822b", "Stressed": "#c0392b"}


# ----------------------------- data + model --------------------------------
def label_condition(g):
    if g >= 0.6:
        return "Healthy"
    if g >= 0.3:
        return "Moderate"
    return "Stressed"


def simulate_data(days=30, fields=("Field_A", "Field_B", "Field_C")):
    rng = np.random.default_rng(42)
    hours = days * 24
    time = pd.date_range("2026-09-01", periods=hours, freq="h")
    t = np.arange(hours)
    frames = []
    for k, field in enumerate(fields):
        temp = 27 + 6 * np.sin(2 * np.pi * (t % 24 - 9) / 24) \
            + rng.normal(0, 1, hours) + 0.8 * k
        hum = 70 - 1.4 * (temp - 27) + rng.normal(0, 3, hours)
        moist = 38 + rng.normal(0, 1.5, hours)
        for d in rng.choice(days, 6, replace=False):
            moist[d * 24:] += 6
        moist = np.clip(moist - 0.01 * t, 8, 60) - 2 * k
        growth = (0.9 - 0.012 * (temp - 26) ** 2
                  - 0.0025 * (hum - 65) ** 2 / 10
                  + 0.02 * (moist - 25) + rng.normal(0, 0.12, hours))
        frames.append(pd.DataFrame({
            "time": time, "field": field, "temperature": temp,
            "humidity": hum, "soil_moisture": moist,
            "growth_cm_day": np.clip(growth, 0, None)}))
    return pd.concat(frames, ignore_index=True)


def clean_data(raw):
    df = raw.copy()
    df["time"] = pd.to_datetime(df["time"])
    df = df.drop_duplicates(subset=["time", "field"])
    df.loc[(df["temperature"] > 50) | (df["temperature"] < -5), "temperature"] = np.nan
    df = df.sort_values(["field", "time"])
    df[NUM_COLS] = df.groupby("field")[NUM_COLS].transform(
        lambda s: s.interpolate(limit_direction="both"))
    df = df.dropna(subset=NUM_COLS)
    df["condition"] = df["growth_cm_day"].apply(label_condition)
    return df.reset_index(drop=True)


class CropModel:
    def __init__(self, df):
        self.df = df
        X, yr, yc = df[FEATURES], df["growth_cm_day"], df["condition"]
        Xtr, Xte, yrtr, yrte, yctr, ycte = train_test_split(
            X, yr, yc, test_size=0.25, random_state=42)
        self.reg = RandomForestRegressor(n_estimators=150, random_state=42, n_jobs=-1)
        self.reg.fit(Xtr, yrtr)
        self.clf = RandomForestClassifier(n_estimators=150, random_state=42, n_jobs=-1)
        self.clf.fit(Xtr, yctr)
        pred = self.reg.predict(Xte)
        self.r2 = r2_score(yrte, pred)
        self.mae = mean_absolute_error(yrte, pred)
        self.acc = accuracy_score(ycte, self.clf.predict(Xte))
        self.importance = pd.Series(self.reg.feature_importances_, index=FEATURES)

    def predict(self, temp, hum, moist):
        row = pd.DataFrame([[temp, hum, moist]], columns=FEATURES)
        growth = float(self.reg.predict(row)[0])
        proba = dict(zip(self.clf.classes_, self.clf.predict_proba(row)[0]))
        return growth, label_condition(growth), proba


# --------------------------------- GUI -------------------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Agriculture Data Monitoring")
        self.geometry("1200x720")
        self.minsize(1000, 640)
        self.configure(bg="#f6f4ec")
        self._style()
        self.model = CropModel(clean_data(simulate_data()))
        self._build()
        self.refresh_all()

    def _style(self):
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TFrame", background="#f6f4ec")
        s.configure("Card.TFrame", background="#ffffff")
        s.configure("TLabel", background="#f6f4ec", foreground="#1d2b22",
                    font=("Segoe UI", 11))
        s.configure("Card.TLabel", background="#ffffff", foreground="#1d2b22",
                    font=("Segoe UI", 11))
        s.configure("Title.TLabel", font=("Georgia", 20, "bold"),
                    foreground="#1f3a2b", background="#f6f4ec")
        s.configure("H.TLabel", font=("Georgia", 14, "bold"),
                    foreground="#1f3a2b", background="#ffffff")
        s.configure("Accent.TButton", background="#1f3a2b", foreground="#ffffff",
                    font=("Segoe UI", 11, "bold"), padding=8)
        s.map("Accent.TButton", background=[("active", "#2f6f4e")])
        s.configure("Treeview", rowheight=24)

    def _build(self):
        header = ttk.Frame(self)
        header.pack(fill="x", padx=20, pady=(14, 6))
        ttk.Label(header, text="Smart Agriculture Data Monitoring",
                  style="Title.TLabel").pack(side="left")
        ttk.Button(header, text="Load CSV", command=self.load_csv).pack(side="right")
        ttk.Button(header, text="Use simulated data",
                   command=self.use_simulated).pack(side="right", padx=8)

        body = ttk.Frame(self)
        body.pack(fill="both", expand=True, padx=20, pady=10)

        # ---- left: prediction panel
        left = ttk.Frame(body, style="Card.TFrame", padding=20)
        left.pack(side="left", fill="y")
        ttk.Label(left, text="Crop condition predictor", style="H.TLabel").pack(anchor="w")
        ttk.Label(left, text="Move the sliders to set field conditions",
                  style="Card.TLabel").pack(anchor="w", pady=(0, 12))

        self.vars = {}
        specs = [("Temperature (°C)", "temperature", 10, 45, 27),
                 ("Humidity (%)", "humidity", 20, 100, 70),
                 ("Soil moisture (%)", "soil_moisture", 5, 70, 35)]
        for label, key, lo, hi, init in specs:
            var = tk.DoubleVar(value=init)
            self.vars[key] = var
            row = ttk.Frame(left, style="Card.TFrame")
            row.pack(fill="x", pady=6)
            ttk.Label(row, text=label, style="Card.TLabel").pack(anchor="w")
            line = ttk.Frame(row, style="Card.TFrame")
            line.pack(fill="x")
            val = ttk.Label(line, text=f"{init:.1f}", style="Card.TLabel", width=6)
            ttk.Scale(line, from_=lo, to=hi, variable=var, length=240,
                      command=lambda _v, v=var, l=val: (l.config(text=f"{v.get():.1f}"),
                                                       self.predict())
                      ).pack(side="left")
            val.pack(side="left", padx=8)

        ttk.Button(left, text="Predict", style="Accent.TButton",
                   command=self.predict).pack(fill="x", pady=(16, 10))

        self.growth_lbl = tk.Label(left, text="-- cm/day", bg="#ffffff",
                                   fg="#1f3a2b", font=("Georgia", 26, "bold"))
        self.growth_lbl.pack(pady=(6, 0))
        self.cond_lbl = tk.Label(left, text="--", bg="#ffffff",
                                 font=("Segoe UI", 16, "bold"))
        self.cond_lbl.pack(pady=(0, 6))
        self.proba_lbl = ttk.Label(left, text="", style="Card.TLabel", justify="left")
        self.proba_lbl.pack(anchor="w")
        self.advice_lbl = ttk.Label(left, text="", style="Card.TLabel",
                                    wraplength=300, justify="left")
        self.advice_lbl.pack(anchor="w", pady=(10, 0))
        self.metrics_lbl = ttk.Label(left, text="", style="Card.TLabel",
                                     justify="left", foreground="#5d6b61")
        self.metrics_lbl.pack(anchor="w", side="bottom", pady=(14, 0))

        # ---- right: tabs
        tabs = ttk.Notebook(body)
        tabs.pack(side="left", fill="both", expand=True, padx=(16, 0))

        dash = ttk.Frame(tabs)
        tabs.add(dash, text="  Dashboard  ")
        self.fig = Figure(figsize=(8, 6), dpi=100, facecolor="#f6f4ec")
        self.canvas = FigureCanvasTkAgg(self.fig, master=dash)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        tbl = ttk.Frame(tabs)
        tabs.add(tbl, text="  Data table  ")
        cols = ["field", "temperature", "humidity", "soil_moisture",
                "growth_cm_day", "condition"]
        self.tree = ttk.Treeview(tbl, columns=cols, show="headings")
        for c in cols:
            self.tree.heading(c, text=c.replace("_", " ").title())
            self.tree.column(c, width=110, anchor="center")
        sb = ttk.Scrollbar(tbl, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        summ = ttk.Frame(tabs, padding=16)
        tabs.add(summ, text="  Field summary  ")
        self.summary_box = tk.Text(summ, font=("Courier New", 11), bg="#ffffff",
                                   relief="flat", padx=12, pady=12)
        self.summary_box.pack(fill="both", expand=True)

        self.status = ttk.Label(self, text="", foreground="#5d6b61")
        self.status.pack(fill="x", padx=20, pady=(0, 8))

    # ---------- actions
    def predict(self):
        g, cond, proba = self.model.predict(*(self.vars[k].get() for k in FEATURES))
        self.growth_lbl.config(text=f"{g:.2f} cm/day")
        self.cond_lbl.config(text=cond, fg=CONDITION_COLOR[cond])
        self.proba_lbl.config(text="\n".join(
            f"{k:9s} {v * 100:5.1f}%" for k, v in sorted(proba.items())))
        advice = {
            "Healthy": "Conditions look good. Keep current irrigation.",
            "Moderate": "Growth is slowing. Check soil moisture and heat.",
            "Stressed": "Crop at risk. Irrigate or shade the field now."}
        self.advice_lbl.config(text=advice[cond])

    def refresh_all(self):
        m = self.model
        self.metrics_lbl.config(
            text=f"Model R²: {m.r2:.2f}   MAE: {m.mae:.2f} cm/day\n"
                 f"Classifier accuracy: {m.acc * 100:.1f}%\n"
                 f"Rows: {len(m.df):,}")
        self.predict()
        self.draw_dashboard()
        self.fill_table()
        self.fill_summary()

    def draw_dashboard(self):
        df = self.model.df
        self.fig.clear()
        fields = list(df["field"].unique())
        col = {f: COLORS[i % len(COLORS)] for i, f in enumerate(fields)}

        ax1 = self.fig.add_subplot(221)
        daily = df.set_index("time").groupby("field")[NUM_COLS].resample("D").mean()
        for f in fields:
            g = daily.loc[f]
            ax1.plot(g.index, g["temperature"], color=col[f], label=f)
        ax1.set_title("Daily mean temperature (°C)", fontsize=10)
        ax1.legend(fontsize=7)
        ax1.tick_params(axis="x", rotation=30, labelsize=7)

        ax2 = self.fig.add_subplot(222)
        bp = ax2.boxplot([df.loc[df["field"] == f, "growth_cm_day"] for f in fields],
                         patch_artist=True, tick_labels=fields)
        for patch, f in zip(bp["boxes"], fields):
            patch.set_facecolor(col[f])
            patch.set_alpha(0.7)
        ax2.set_title("Crop growth by field (cm/day)", fontsize=10)
        ax2.tick_params(labelsize=7)

        ax3 = self.fig.add_subplot(223)
        corr = df[NUM_COLS].corr()
        im = ax3.imshow(corr, cmap="RdYlGn", vmin=-1, vmax=1)
        names = ["Temp", "Humid", "Soil", "Growth"]
        ax3.set_xticks(range(4), names, fontsize=7)
        ax3.set_yticks(range(4), names, fontsize=7)
        for i in range(4):
            for j in range(4):
                ax3.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center",
                         va="center", fontsize=8)
        ax3.set_title("Correlation heatmap", fontsize=10)

        ax4 = self.fig.add_subplot(224)
        imp = self.model.importance.sort_values()
        ax4.barh(imp.index, imp.values, color="#c9822b")
        ax4.set_title("What drives crop growth?", fontsize=10)
        ax4.tick_params(labelsize=7)

        self.fig.tight_layout()
        self.canvas.draw()

    def fill_table(self):
        self.tree.delete(*self.tree.get_children())
        for _, r in self.model.df.head(500).iterrows():
            self.tree.insert("", "end", values=(
                r["field"], f"{r['temperature']:.1f}", f"{r['humidity']:.1f}",
                f"{r['soil_moisture']:.1f}", f"{r['growth_cm_day']:.2f}",
                r["condition"]))

    def fill_summary(self):
        df = self.model.df
        s = df.groupby("field")[NUM_COLS].mean().round(2)
        counts = pd.crosstab(df["field"], df["condition"])
        self.summary_box.config(state="normal")
        self.summary_box.delete("1.0", "end")
        self.summary_box.insert("end", "Average readings per field\n\n")
        self.summary_box.insert("end", s.to_string() + "\n\n")
        self.summary_box.insert("end", "Crop condition counts\n\n")
        self.summary_box.insert("end", counts.to_string() + "\n")
        self.summary_box.config(state="disabled")

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not path:
            return
        try:
            raw = pd.read_csv(path)
            missing = {"time", "field", *NUM_COLS} - set(raw.columns)
            if missing:
                raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
            self.model = CropModel(clean_data(raw))
            self.status.config(text=f"Loaded {path}")
            self.refresh_all()
        except Exception as e:
            messagebox.showerror("Could not load file", str(e))

    def use_simulated(self):
        self.model = CropModel(clean_data(simulate_data()))
        self.status.config(text="Using simulated sensor data")
        self.refresh_all()


if __name__ == "__main__":
    App().mainloop()
