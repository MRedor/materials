select Name, GovernmentForm from Country
group by GovernmentForm
having max(SurfaceArea) = SurfaceArea;
