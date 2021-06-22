from .io import load as load, load_clusters as load_clusters
from .scripts_interface import doc2vec as doc2vec, word2clusters as word2clusters, word2phrase as word2phrase, word2vec as word2vec
from .wordclusters import WordClusters as WordClusters
from .wordvectors import WordVectors as WordVectors
from typing import Any

def parse_git(root: Any, **kwargs: Any): ...
