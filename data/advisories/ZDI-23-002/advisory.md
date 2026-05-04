# ZDI-23-002: Microsoft Azure Service Fabric WAagent Exposure of Resource to Wrong Sphere Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-002
- **ZDI-CAN:** ZDI-CAN-18519
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21531
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** David Fiser (Trend Micro - Project Nebula)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-002/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on Microsoft Azure. An attacker must first obtain the ability to execute high-privileged code within a container on the target system in order to exploit this vulnerability. The specific flaw exists within the WAagent daemon. The issue results from insufficient verification of the origin of requests. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21531

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
