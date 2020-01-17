from gym.envs.registration import register

register(
    id='toy-stock-v0',
    entry_point='toy_stock.envs:ToyStockEnv',
)