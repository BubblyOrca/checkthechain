from ... import binary_utils
from .. import rpc_backends
from .. import rpc_coding
from .. import rpc_spec


def eth_block_number(provider=None, decode_result=True):
    result = rpc_backends.rpc_call(
        method='eth_blockNumber',
        parameters=[],
        provider=provider,
    )
    if decode_result:
        result = binary_utils.convert_binary_format(result, 'integer')
    return result


def eth_get_block_by_hash(
    block_hash,
    include_full_transactions=False,
    provider=None,
    decode_result=True,
    snake_case_result=True,
):
    encoded_block_hash = binary_utils.convert_binary_format(
        block_hash, 'prefix_hex'
    )

    parameters = [encoded_block_hash, include_full_transactions]
    result = rpc_backends.rpc_call(
        method='eth_getBlockByHash',
        parameters=parameters,
        provider=provider,
    )

    if decode_result:
        quantities = rpc_spec.rpc_block_quantities
        result = rpc_coding.decode_rpc_map(result, quantities=quantities)

    if snake_case_result:
        result = rpc_coding.rpc_keys_to_snake_case(result)

    return result


def eth_get_block_by_number(
    block_number,
    include_full_transactions=True,
    decode_result=True,
    provider=None,
    snake_case_result=True,
):

    encoded_block_number = rpc_coding.encode_rpc_block(block_number)

    parameters = [encoded_block_number, include_full_transactions]
    result = rpc_backends.rpc_call(
        method='eth_getBlockByNumber',
        parameters=parameters,
        provider=provider,
    )

    if decode_result:
        quantities = rpc_spec.rpc_block_quantities
        result = rpc_coding.decode_rpc_map(result, quantities=quantities)

    if snake_case_result:
        result = rpc_coding.rpc_keys_to_snake_case(result)

    return result


def eth_get_uncle_count_by_block_hash(
    block_hash, provider=None, decode_result=True
):
    encoded_block_hash = binary_utils.convert_binary_format(
        block_hash, 'prefix_hex'
    )
    result = rpc_backends.rpc_call(
        method='eth_getUncleCountByBlockHash',
        parameters=[encoded_block_hash],
        provider=provider,
    )
    if decode_result:
        result = binary_utils.convert_binary_format(result, 'integer')
    return result


def eth_get_uncle_count_by_block_number(
    block_number, provider=None, decode_result=True
):
    encoded_block_number = rpc_coding.encode_rpc_block(block_number)
    result = rpc_backends.rpc_call(
        method='eth_getUncleCountByBlockNumber',
        parameters=[encoded_block_number],
        provider=provider,
    )
    if decode_result:
        result = binary_utils.convert_binary_format(result, 'integer')
    return result


def eth_get_uncle_by_block_hash_and_index(
    block_hash,
    uncle_index,
    provider=None,
    decode_result=True,
    snake_case_result=True,
):

    encoded_block_hash = binary_utils.convert_binary_format(
        block_hash, 'prefix_hex'
    )
    encoded_uncle_index = binary_utils.convert_binary_format(
        uncle_index, 'prefix_hex'
    )

    result = rpc_backends.rpc_call(
        method='eth_getUncleByBlockHashAndIndex',
        parameters=[encoded_block_hash, encoded_uncle_index],
        provider=provider,
    )

    if decode_result:
        quantities = rpc_spec.rpc_block_quantities
        result = rpc_coding.decode_rpc_map(result, quantities=quantities)

    if snake_case_result:
        result = rpc_coding.rpc_keys_to_snake_case(result)

    return result


def eth_get_uncle_by_block_number_and_index(
    block_number,
    uncle_index,
    provider=None,
    decode_result=True,
    snake_case_result=True,
):

    encoded_block_number = rpc_coding.encode_rpc_block(block_number)
    encoded_uncle_index = binary_utils.convert_binary_format(
        uncle_index, 'prefix_hex'
    )

    result = rpc_backends.rpc_call(
        method='eth_getUncleByBlockNumberAndIndex',
        parameters=[encoded_block_number, encoded_uncle_index],
        provider=provider,
    )

    if decode_result:
        quantities = rpc_spec.rpc_block_quantities
        result = rpc_coding.decode_rpc_map(result, quantities=quantities)

    if snake_case_result:
        result = rpc_coding.rpc_keys_to_snake_case(result)

    return result

