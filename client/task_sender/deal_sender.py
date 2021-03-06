import logging.config

from client.task_sender.service.deal import DealConfig, send_deals_to_miner
from common.config import read_config

logging.basicConfig(level=logging.INFO)


def send_deals(config_path, miner_id, task_name=None, metadata_csv_path=None, deal_list=None, task_uuid=None):
    config = read_config(config_path)
    from_wallet = config['sender']['wallet']
    max_price = config['sender']['max_price']
    is_verified = config['sender']['is_verified']
    epoch_interval_hours = config['sender']['start_epoch_hours']
    output_dir = config['sender']['output_dir']

    deal_config = DealConfig(miner_id, from_wallet, max_price, is_verified, epoch_interval_hours)

    if deal_list:
        return send_deals_to_miner(deal_config, output_dir, task_name=task_name, deal_list=deal_list, task_uuid=task_uuid)
    elif metadata_csv_path:
        return send_deals_to_miner(deal_config, output_dir, csv_file_path=metadata_csv_path, task_uuid=task_uuid)
    else:
        logging.error("no valid deal list or metadata_csv provided")
