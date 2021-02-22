# Dash Starter Kit

Dash starter kit is opinionated architecture based on best practices from our collected experiences. This started kit demostrate clean architecture using app.py as global variable to share datasource and control id between components. The starter kit uses Bootstrap, datatable, modal and form component from https://dash-bootstrap-components.opensource.faculty.ai/. The service layer utilize repository pattern so it can be easily extented for testing purpose. You can split up your component and architect it as you please, see the people_list.py and people_detail.py for more info.

## Feature
* routing
* modal
* view
* api layer
* service layer
* Page 404
* Help
* Datatable
* Get Cookie data for authentication

## Installation

```bash
git clone https://github.com/jnguyen0220/dash-starter-kit.git
pip install -r requirements.txt 
python/python3 index.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)