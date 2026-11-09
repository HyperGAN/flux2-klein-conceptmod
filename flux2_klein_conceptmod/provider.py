"""Lightweight installed-provider metadata; model code is loaded on creation."""
from conceptmod.contracts import BackendCapabilities
from conceptmod.providers import BackendProvider

PROVIDER = BackendProvider(
    name="klein",
    factory="flux2_klein_conceptmod.backend:KleinBackend",
    distribution="flux2-klein-conceptmod",
    capabilities=BackendCapabilities(),
)
