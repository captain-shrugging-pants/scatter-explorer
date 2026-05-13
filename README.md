# With just a click, this package will display the light-curve and its Fourier amplitude spectrum of any star in your scatterplot. 

## Directly run ```demo_limited.ipynb``` for a minimal running example to see the wonders of this widget.

### Below are the relevant details.

- #### This package only needs ```numpy```, ```pandas```, ```matplotlib```, ```ipyml```, and ```ipywidgets```.
  If not already present, run
  ```
  conda install -c conda-forge numpy pandas matplotlib ipywidgets
  ```

- #### Light-curve and Fourier amplitude spectra data format
To be able to run ```demo_limited.ipynb```, lightcurves are stored in ```sample_data/LK/``` and their spectra in ```sample_data/PS/```. 

To customize for your own catalog of stars, you must first download their lightcurves and compute their spectra, and store them similarly. 
```scatter-explorer``` (this package!) expects filename to be ```TIC-ID_author_cadence.npz```, for both the light-curves and their amplitude spectra.

For e.g., below is how you'd load a lightcurve and its spectra, 
```
star_l = np.load(sample_data/LK/103692670_SPOC_120.npz)
time, flux = star_l['time'], star_l['flux]

star_a = np.load(sample_data/PS/103692670_SPOC_120.npz)
freq, ampl = star_a['time'], star_a['flux]

```
"SPOC" being the author, "120" stands for 120-second cadence of the lightcurve.

If you're used to saving your files differently, please do modify the relevant lines in ```stellar_explorer/loaders.py```. 
I'm always used to saving in the above mentioned format. 
This is why in the  ```stellar_explorer/loaders.py``` file, you'll find 
```
def load_star(self, star: Star):
        time, flux = self.load_lightcurve(star.tic, star.pipecad)
        freq, ampl = self.load_powerspectrum(star.tic, star.pipecad)
```
where ```star.tic``` retrieves the "TIC-ID" string, and ```star.pipecad``` retrieves the "author_cadence" string, allowing to load the file correctly.

- #### Dataframe containing various quantities to be plotted / annotated.
An appropriate dataframe containing various quantities of interest for plotting purposes should be present in the ```sample_data``` folder. 
As a trial, ```sample_data/demo_dataframe.csv``` is the dataset uploaded for this purpose. 

- #### Bonus -
Users can specify the x and y axes to be log / linear, color-code the scatterplot with custom values, etc.

More to come!
