
from flask import Flask, render_template, request, send_file
import pandas as pd
import ipaddress

app = Flask(__name__)

def calculate_vlsm(initial_ip, networks):
    networks.sort(key=lambda x: x['hosts_needed'], reverse=True)
    result = []
    current_ip = ipaddress.IPv4Address(initial_ip)

    for network in networks:
        hosts_needed = network['hosts_needed']
        subnet_mask = 32
        while (2 ** (32 - subnet_mask)) < hosts_needed:
            subnet_mask -= 1

        network_address = ipaddress.IPv4Network(f"{current_ip}/{subnet_mask}", strict=False)
        broadcast_address = network_address.broadcast_address
        usable_range = f"{network_address.network_address + 1} - {broadcast_address - 1}"
        subnet_mask_dec = str(network_address.netmask)

        wildcard_octets = [str(255 - int(o)) for o in subnet_mask_dec.split('.')]
        wildcard = ".".join(wildcard_octets)

        result.append({
            "Name": network['name'],
            "Network": str(network_address.network_address),
            "Range": usable_range,
            "Broadcast": str(broadcast_address),
            "Subnet Mask": subnet_mask_dec,
            "Slash": f"/{subnet_mask}",
            "Wildcard": wildcard
        })

        current_ip = broadcast_address + 1

    df = pd.DataFrame(result)
    output_file = "vlsm_result.xlsx"
    df.to_excel(output_file, index=False)
    return result, output_file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_networks = int(request.form['num_networks'])
        initial_ip = request.form['initial_ip']

        networks = []
        for i in range(num_networks):
            name = request.form.get(f'name_{i}')
            hosts_needed = int(request.form.get(f'hosts_{i}'))
            networks.append({'name': name, 'hosts_needed': hosts_needed})

        result, file_path = calculate_vlsm(initial_ip, networks)
        return render_template('result.html', result=result, file_path=file_path)

    return render_template('index.html')

@app.route('/download')
def download():
    return send_file('vlsm_result.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
