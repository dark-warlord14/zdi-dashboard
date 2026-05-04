# ZDI-21-1058: NETGEAR XR1000 UPnP SOAPAction Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1058
- **ZDI-CAN:** ZDI-CAN-13325
- **Date:** 2021-09-08
- **CVE:** CVE-2021-34870
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** XR1000
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1058/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of NETGEAR XR1000 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of SOAP messages. The issue results from a lack of authentication required for a privileged request. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000063967/Security-Advisory-for-a-Security-Misconfiguration-Vulnerability-on-the-XR1000-PSV-2021-0101

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-09-08 - Coordinated public release of advisory
