select First.Name, Second.Name, First.GovernmentForm
from Country First inner join Country Second
                   on First.GovernmentForm = Second.GovernmentForm and First.Name <> Second.Name;
