
from esgfpid.defaults import ROUTING_KEY_BASIS as ROUTING_KEY_BASIS


ROUTING_KEYS = dict(
    publi_file = ROUTING_KEY_BASIS+'publication.file.orig',
    publi_file_rep = ROUTING_KEY_BASIS+'publication.file.replica',
    publi_ds = ROUTING_KEY_BASIS+'publication.dataset.orig',
    publi_ds_rep = ROUTING_KEY_BASIS+'publication.dataset.replica',
    unpubli_all = ROUTING_KEY_BASIS+'unpublication.all',
    unpubli_one = ROUTING_KEY_BASIS+'unpublication.one',
    err_add = ROUTING_KEY_BASIS+'errata.add',
    err_rem = ROUTING_KEY_BASIS+'errata.remove',
    shop_cart = ROUTING_KEY_BASIS+'cart.datasets'
)