import os
import tempfile
import toolsql

from ctc.db.datatypes import erc20_metadata

example_data = [
    {
        'address': '0x956f47f50a910163d8bf957cf5846d573e7f87ca',
        'symbol': 'FEI',
        'decimals': 18,
    },
    {
        'address': '0xc7283b66eb1eb5fb86327f08e1b5816b0720212b',
        'symbol': 'TRIBE',
        'decimals': 18,
    },
    {
        'address': '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640',
        'symbol': 'USDC',
        'decimals': 6,
    },
]


def get_test_db_config():
    tempdir = tempfile.mkdtemp()
    return {
        'dbms': 'sqlite',
        'path': os.path.join(tempdir, 'example.db'),
    }


def test_create_schema():
    db_config = get_test_db_config()
    db_schema = erc20_metadata.get_schema()
    toolsql.create_tables(
        db_config=db_config,
        db_schema=db_schema,
    )

    engine = toolsql.create_engine(**db_config)

    # insert data
    with engine.connect() as conn:
        with conn.begin():
            for datum in example_data:
                erc20_metadata.insert_erc20_metadata(conn=conn, **datum)

        # get data individually
        with conn.begin():
            for datum in example_data:
                actual_metadata = erc20_metadata.select_erc20_metadata(
                    conn=conn,
                    address=datum['address'],
                    row_format='dict',
                )
                for key, target_value in datum.items():
                    assert target_value == actual_metadata[key]

        # get data collectively
        with conn.begin():
            all_addresses = [datum['address'] for datum in example_data]
            actual_metadatas = erc20_metadata.select_erc20s_metadatas(
                conn=conn,
                addresses=all_addresses,
            )
            sorted_example_data = sorted(example_data, key=lambda x: x['address'])
            sorted_actual_data = sorted(actual_metadatas, key=lambda x: x['address'])
            for target, actual in zip(sorted_example_data, sorted_actual_data):
                assert target == actual
                print(target, actual)
