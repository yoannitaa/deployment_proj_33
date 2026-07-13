"""
app/utils/validation.py
--------------------------
Validasi input SECARA MANUAL
"""

import pandas as pd

# Daftar fitur yang WAJIB ada di input, sesuaikan dengan fitur model kamu
REQUIRED_FIELDS = ['claim_number','age_of_driver','gender',
                    'marital_status','safty_rating','annual_income',
                    'high_education_ind','address_change_ind','living_status',
                    'zip_code','claim_date','claim_day_of_week','accident_site',
                    'past_num_of_claims','witness_present_ind','liab_prct',
                    'channel','policy_report_filed_ind','claim_est_payout','age_of_vehicle',
                    'vehicle_category','vehicle_price','vehicle_color','vehicle_weight']


def validate_schema_consistency(data: list[dict]):
    """
    Mengecek apakah semua dictionary dalam list punya key yang sama persis.
    """

    # 1. Data harus berupa list
    if not isinstance(data, list):
        return False, f"Input harus berupa list, diterima: {type(data).__name__}", None # is_valid, msg_error, data

    # 2. List tidak boleh kosong (opsional, sesuaikan kebutuhan)
    if len(data) == 0:
        return False, "List data kosong, tidak ada yang bisa divalidasi", None # is_valid, msg_error, data

    # 3. Setiap elemen dalam list harus berupa dict
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            return False, f"Elemen index {i} bukan dictionary, tapi: {type(item).__name__}", None # # is_valid, msg_error, data

    # 4. Ambil skema (set of keys) dari dict PERTAMA sebagai acuan/reference
    reference_keys = set(data[0].keys()) 

    # 5. Bandingkan skema setiap dict lainnya terhadap acuan
    for i, item in enumerate(data):
        current_keys = set(item.keys())

        if current_keys != reference_keys:
            # Cari tahu perbedaannya secara spesifik, supaya pesan error informatif
            missing_keys = reference_keys - current_keys   # ada di acuan, tidak ada di sini
            extra_keys = current_keys - reference_keys     # ada di sini, tidak ada di acuan

            detail = []
            if missing_keys:
                detail.append(f"kekurangan key: {sorted(missing_keys)}")
            if extra_keys:
                detail.append(f"ada key tambahan yang tidak diharapkan: {sorted(extra_keys)}")

            return False, f"Skema tidak konsisten di index {i} — {', '.join(detail)}", None # is_valid, msg_error, data

    # 6. Convert kedalam dataFrame dan pastikan nama kolom sesuai
    df = pd.DataFrame(data)
    if list(df.columns) != REQUIRED_FIELDS:
        return False, f"Invalid schema. Expected {REQUIRED_FIELDS}", None # is_valid, msg_error, data

    return True, None, df # is_valid, msg_error, data