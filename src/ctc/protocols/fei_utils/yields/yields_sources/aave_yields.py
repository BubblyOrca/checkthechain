import asyncio
import typing

from ctc import evm
from ctc import spec
from .. import yields_spec


aFEI = '0x683923db55fead99a79fa01a27eec3cb19679cc3'


async def async_get_fei_yield_data(
    block_numbers: typing.Sequence[spec.BlockNumberReference],
) -> typing.Mapping[str, yields_spec.YieldSourceData]:

    tvl_history_task = asyncio.create_task(
        async_get_aave_fei_tvl_history(block_numbers)
    )
    current_yield_task = asyncio.create_task(
        async_get_aave_fei_current_yield(block_numbers)
    )
    yield_history_task = asyncio.create_task(
        async_get_aave_fei_yield_history(block_numbers)
    )

    tvl_history = await tvl_history_task
    current_yield = await current_yield_task
    yield_history = await yield_history_task

    aave_v2: yields_spec.YieldSourceData = {
        'name': 'Aave Lending',
        'category': 'Lending',
        'platform': 'Aave',
        'staked_tokens': [yields_spec.FEI],
        'reward_tokens': [yields_spec.FEI],
        'tvl_history': tvl_history,
        'tvl_history_units': 'FEI',
        'current_yield': current_yield,
        'current_yield_units': {'Aave V2 FEI Lending': 'APY'},
        'yield_history': yield_history,
        'yield_history_units': {'Aave V2 FEI Lending': 'APY'},
    }

    return {aave_v2['name']: aave_v2}


async def async_get_aave_fei_tvl_history(block_numbers) -> list[float]:
    tvls = await evm.async_get_erc20_total_supply_by_block(
        token=aFEI,
        blocks=block_numbers,
    )
    return [float(tvl) for tvl in tvls]


async def async_get_aave_fei_current_yield(block_numbers) -> list[float]:
    return [0.01 for block in block_numbers]


async def async_get_aave_fei_yield_history(block_numbers) -> list[float]:
    return [0.01 for block in block_numbers]
