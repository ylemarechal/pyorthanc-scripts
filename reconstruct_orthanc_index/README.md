# Reconstruct Orthanc Index

## Description

Rebuild the index through a simple external mechanism. 
This is particularly useful in distributed architectures or behind a load balancer, where you may want to initiate 
the rebuild on specific nodes without relying on the Housekeeper plugin.

## Usage

**Example :**

```bash
python reconstruct_index.py
```