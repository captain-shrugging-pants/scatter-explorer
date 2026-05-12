# With just a click, this package will display the light-curve and Fourier amplitude spectra of stars in your scatterplot. 

## Directly run ```demo_limited.ipynb``` for a minimal running example to see the wonders of this widget.

### Below are the relevant details.

- #### Light-curve and Fourier amplitude spectra data format
To be able to run ```demo_limited.ipynb```, the necessary data is stored in ```sample_data/LK/``` and ```sample_data/PS/``` folders. 

To customize for your own catalog of stars, you must first download their lightcurves and compute their spectra, and store them in the appropriate format. 
The filename format that ```scatter-explorer``` (this package!) works on is ```TIC-ID_author_cadence.npz```, for both the light-curves and their amplitude spectra.

For e.g., below is how you'd load a lightcurve and its spectra, 
```
star_l = np.load(sample_data/LK/103692670_SPOC_120.npz)
time, flux = star_l['time'], star_l['flux]

star_a = np.load(sample_data/PS/103692670_SPOC_120.npz)
freq, ampl = star_a['time'], star_a['flux]

```

If you're used to saving your files differently, please do modify the relevant lines in ```stellar_explorer/loaders.py```. 
I'm always used to saving in the above mentioned format. 
This is why in the  ```stellar_explorer/loaders.py``` file, you'll find 
```
def load_star(self, star: Star):
        time, flux = self.load_lightcurve(star.tic, star.pipecad)
        freq, ampl = self.load_powerspectrum(star.tic, star.pipecad)
```
where star.tic gets the TIC-ID from the dataframe, and star.pipecad gets the author_cadence from the dataframe, allowing to load the file properly.

- #### Dataframe containing various quantities to be plotted / annotated.
An appropriate dataframe containing various quantities of interest for plotting purposes should be present in the ```sample_data``` folder. 
As a trial, ```sample_data/demo_dataframe.csv``` is the dataset uploaded for this purpose. 

- #### Bonus -
Users can specify the x and y axes to be log / linear, color-code the scatterplot with custom values, etc.

More to come!
